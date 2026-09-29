from ImpararePackage import dataRequest
from ImpararePackage import maestro
import pandas as pd
import threading
from multiprocessing import Pool, cpu_count
import itertools

def worker(args: tuple[pd.DataFrame, str]):
    c, index_name = args
    c = maestro.incrise_by_n_hours(df= c, arrayColumns= ["dthr_criacao", "dthr_procedimento", "dthr_fim_procedimento"], hours= 3)
    c = maestro.remove_columns(df= c, column= "id_cirurgia")
    c = maestro.to_float(df= c, arrayColumns= ["tempo_cirurgia"])

    def elk_upload(c: pd.DataFrame, index_name: str):
        client = dataRequest.ELASTICSEARCH_CONNECTION
       
        c["paciente_id"] = c["patient_id"]
        c = maestro.keep_columns(df= c, arrayColumns= [
            "id",
            "perfil",
            "dthr_criacao",
            "dthr_procedimento",
            "dthr_fim_procedimento",
            "tempo_cirurgia",
            "texto_cirurgia",
            "paciente_id",
            "nome_medico",
            "nome_procedimentos"
         ])
        actions = maestro.generate_actions(c, index_name)
        maestro.bulk_upload_with_retry(client, actions, context="procedimento", thread_count=1)

    print("Iniciando uploads!")
    table = "isa_procedimento"
    job = threading.Thread(target= elk_upload, args=(c.copy(), index_name))
    job_3 = threading.Thread(target=dataRequest.set_data_on_sql, args=(c, table), kwargs={"if_exists": "append", "isLocal": True})
    
    jobs = [
        job, 
        job_3
    ]
    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()
        
def main():
    client = dataRequest.ELASTICSEARCH_CONNECTION
    print(client.cluster.health())
    print(client.ping())

    index_name = maestro.getELKIndexValue("procedimentos")
    if maestro.get_must_update_all_patients() == '1':
        create_query = """
            DROP TABLE IF EXISTS isa_procedimento;
            CREATE UNLOGGED TABLE isa_procedimento (
                id TEXT,
                perfil TEXT,
                patient_id INTEGER,
                dthr_criacao DATE,
                dthr_procedimento TIMESTAMP,
                dthr_fim_procedimento TIMESTAMP,
                tempo_cirurgia FLOAT,
                texto_cirurgia TEXT,
                nome_medico TEXT,
                nome_procedimentos TEXT,
                tipo_atendimento TEXT,
                ordem TEXT,
                criterio TEXT,
                company_code TEXT,
                company_id TEXT
            );
        """
        dataRequest.execute(create_query, isLocal= True)
        dataRequest.execute(create_query, isLocal= False)
        client.options(ignore_status=[400, 404]).indices.delete(index=index_name)
        
        if not client.indices.exists(index=index_name):
            print("Criando index", index_name)
            client.indices.create(
                index=index_name,
                settings={
                    "index": {
                        "max_result_window": 100000,
                        "number_of_shards": 1,
                        "number_of_replicas": 0,
                        "refresh_interval": "30s",
                        "translog": {
                            "durability": "async",
                            "sync_interval": "30s"
                        }
                    }
                },
                mappings={
                    # front busca "procedimentos" por paciente_id (term); demais campos so sao retornados
                    "dynamic": "strict",
                    "properties": {
                        "id": {"type": "keyword", "index": False, "doc_values": False},
                        "perfil": {"type": "keyword", "index": False, "doc_values": False},
                        "dthr_criacao": {"type": "date", "index": False, "doc_values": False},
                        "dthr_procedimento": {"type": "date", "index": False, "doc_values": False},
                        "dthr_fim_procedimento": {"type": "date", "index": False, "doc_values": False},
                        "tempo_cirurgia": {"type": "float", "index": False, "doc_values": False},
                        "texto_cirurgia": {"type": "text", "index": False},
                        "paciente_id": {"type": "integer"},
                        "nome_medico": {"type": "keyword", "index": False, "doc_values": False},
                        "nome_procedimentos": {"type": "text", "index": False},
                    }
                }
            )
            maestro.wait_for_index_health(client, index_name)

    else:
        # Drop local table
        dataRequest.execute("DELETE FROM isa_procedimento WHERE patient_id in (select distinct record_id from patients_to_update)", isLocal= True)
        
        #Busca IDS para deleção
        df = dataRequest.get_data(queryText= f"SELECT distinct record_id FROM patients_to_update", chunck= None)
        pcts_ids = df['record_id'].tolist()

        # Drop ELK index
        def chunks(seq, n):
            """Yield successive n-sized chunks from seq."""
            for i in range(0, len(seq), n):
                yield seq[i:i + n]

        total= 0
        for lote in chunks(pcts_ids, 1000):
            resp = client.delete_by_query(
                index= index_name,
                query= {
                    "terms": {
                        "paciente_id": lote
                    }
                },
                conflicts= "proceed",
                refresh= True,
                slices= "auto"
            )
            total += resp['deleted']
            print(f"Deletados {resp['deleted']} procedimentos do lote de {len(lote)} pacientes. Total deletados até agora: {total}")
        print(f"Deletados {total} procedimentos no total para {len(pcts_ids)} pacientes.")
    
    append_query = """
        SELECT 
            s.patient_id::text || ' ' || s.dthr_procedimento::text as id,
            s.perfil as perfil,
            s.patient_id:: integer as patient_id,
            null::date as dthr_criacao,
            s.dthr_procedimento::timestamp as dthr_procedimento, 
            s.dthr_fim_procedimento::timestamp as dthr_fim_procedimento,
            s.tempo_de_cirurgia:: float as tempo_cirurgia,
            s.texto_cirurgia:: text as texto_cirurgia,
            s.nome_medico:: text as nome_medico,
            s.nome_procedimento:: text as nome_procedimentos,
            s.tipo_atendimento:: text as tipo_atendimento,
            null as ordem,
            null as criterio, 
            c.company_code, 
            c.hospital_id as company_id  
        FROM "imparare2_cirurgias_union_gamb" s
        LEFT JOIN imparare_patient_company_treatment c 
            ON s.patient_id = c.record_id
            AND s.dthr_procedimento between c.attendance_date AND c.discharge_date
            AND c.company_code IS NOT null;
    """
    df_iterator = dataRequest.get_data(queryText= append_query)

    with Pool(4) as pool:
        for _ in pool.imap_unordered(worker, zip(df_iterator, itertools.repeat(index_name))):
            pass


if __name__ == "__main__":
    main()