from ImpararePackage import dataRequest
from ImpararePackage import maestro
import pandas as pd
import threading
from multiprocessing import Pool, cpu_count
import itertools

def worker(args: tuple[pd.DataFrame, str]):
    c, index_name = args

    def elk_upload(c: pd.DataFrame, index_name: str):
        client = dataRequest.ELASTICSEARCH_CONNECTION
        c["paciente_id"] = c["patient_id"]
        c = maestro.keep_columns(df= c, arrayColumns= [
            "id",
            "codigo_prescricao",
            "dthr_prescricao",
            "medicamento",
            "dose",
            "unidade",
            "frequencia",
            "via",
            "paciente_id",
        ])
        actions = maestro.generate_actions(c, index_name)
        maestro.bulk_upload_with_retry(client, actions, context="medicamento", thread_count=1)

    print("Iniciando uploads!")
    table = "isa_medicamento"
    
    jobs = [
        threading.Thread(target= elk_upload, args=(c.copy(), index_name)), 
        threading.Thread(target=dataRequest.set_data_on_sql, args=(c, table), kwargs={"if_exists": "append", "isLocal": True})
    ]
    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()


def main():
    client = dataRequest.ELASTICSEARCH_CONNECTION
    print(client.cluster.health())
    print(client.ping())

    index_name = maestro.getELKIndexValue("medicamentos")
    if maestro.get_must_update_all_patients() == '1':
        create_query = """
            DROP TABLE IF EXISTS isa_medicamento;
            CREATE UNLOGGED TABLE isa_medicamento (
                id TEXT,
                patient_id INTEGER,
                codigo_prescricao INTEGER,
                dthr_prescricao TIMESTAMP,
                medicamento TEXT,
                dose TEXT,
                unidade TEXT,
                frequencia TEXT,
                via TEXT,
                tipo_atendimento TEXT,
                ordem TEXT,
                criterio TEXT,
                company_code TEXT,
                company_id TEXT
            );
        """
        dataRequest.execute(create_query, isLocal= False)
        dataRequest.execute(create_query, isLocal= True)
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
                    # front busca "medicamentos" por paciente_id (term); demais campos so sao retornados
                    "dynamic": "strict",
                    "properties": {
                        "id": {"type": "keyword", "index": False, "doc_values": False},
                        "codigo_prescricao": {"type": "integer", "index": False, "doc_values": False},
                        "dthr_prescricao": {"type": "date", "index": False, "doc_values": False},
                        "medicamento": {"type": "text", "index": False},
                        "dose": {"type": "keyword", "index": False, "doc_values": False},
                        "unidade": {"type": "keyword", "index": False, "doc_values": False},
                        "frequencia": {"type": "keyword", "index": False, "doc_values": False},
                        "via": {"type": "keyword", "index": False, "doc_values": False},
                        "paciente_id": {"type": "integer"},
                    }
                }
            )
            maestro.wait_for_index_health(client, index_name)
    else:
        # Drop local table
        dataRequest.execute("DELETE FROM isa_medicamento WHERE patient_id in (select distinct record_id from patients_to_update)", isLocal= True)
        
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
            print(f"Deletados {resp['deleted']} medicamentos do lote de {len(lote)} pacientes. Total deletados até agora: {total}")
        print(f"Deletados {total} medicamentos no total para {len(pcts_ids)} pacientes.")


    append_query= """
       SELECT 
            md5(registro::varchar||cd_pre_med::varchar||dthr_prescricao::varchar||antibiotico::varchar||dose::varchar||"tipo_atendimento"::varchar) as id, 
            "registro" as patient_id, 
            "cd_pre_med" as codigo_prescricao,
            DTHR_PRESCRICAO as dthr_prescricao, 
            ANTIBIOTICO as medicamento,
            dose,
            unidade,
            frequencia,
            via,
            "tipo_atendimento",
            null as ordem,
            null as criterio,
            c.company_code, 
            c.hospital_id as company_id
        FROM "imparare2_prescricoes_followup_stacked" s
        LEFT JOIN imparare_patient_company_treatment c 
            ON s.registro = c.record_id
            AND s.dthr_prescricao between c.attendance_date 
            AND c.discharge_date
            AND c.company_code IS NOT null;
    """

    df_iterator = dataRequest.get_data(queryText= append_query)

    with Pool(4) as pool:
        for _ in pool.imap_unordered(worker, zip(df_iterator, itertools.repeat(index_name))):
            pass

if __name__ == "__main__":
    main()