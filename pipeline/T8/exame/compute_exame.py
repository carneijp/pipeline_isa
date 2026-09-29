from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import itertools
from worker_compute_exame import main as worker

def main():
    client = dataRequest.ELASTICSEARCH_CONNECTION
    print(client.cluster.health())
    print(client.ping())

    index_name = maestro.getELKIndexValue("exames")
    if maestro.get_must_update_all_patients() == '1':
        create_query = """
            DROP TABLE IF EXISTS isa_exame;
            CREATE UNLOGGED TABLE isa_exame (
                id TEXT,
                patient_id INTEGER,
                exame TEXT,
                item_exame TEXT,
                dthr_pedido TIMESTAMP,
                dthr_entrega TIMESTAMP,
                resultado TEXT,
                tipo_atendimento TEXT,
                ordem_amostra TEXT,
                data_assinatura TIMESTAMP,
                ordem TEXT,
                criterio TEXT,
                gmr TEXT,
                company_code TEXT,
                company_id TEXT,
                positivo TEXT,
                pcr_covid TEXT
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
                    # front busca "exames" por paciente_id (term); demais campos so sao retornados
                    "dynamic": "strict",
                    "properties": {
                        "id": {"type": "keyword", "index": False, "doc_values": False},
                        "exame": {"type": "text", "index": False},
                        "item_exame": {"type": "text", "index": False},
                        "dthr_pedido": {"type": "date", "index": False, "doc_values": False},
                        "dthr_entrega": {"type": "date", "index": False, "doc_values": False},
                        "resultado": {"type": "text", "index": False},
                        "positivo": {"type": "keyword", "index": False, "doc_values": False},
                        "ordem": {"type": "keyword", "index": False, "doc_values": False},
                        "criterio": {"type": "keyword", "index": False, "doc_values": False},
                        "gmr": {"type": "keyword", "index": False, "doc_values": False},
                        "paciente_id": {"type": "integer"},
                    }
                }
            )
            maestro.wait_for_index_health(client, index_name)
    else:
        # Drop local table
        dataRequest.execute("DELETE FROM isa_exame WHERE patient_id in (select distinct record_id from patients_to_update)", isLocal= True)

        # Drop ELK index
        df = dataRequest.get_data(queryText= f"SELECT distinct record_id FROM patients_to_update", chunck= None)
        pcts_ids = df['record_id'].tolist()

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
            print(f"Deletados {resp['deleted']} exames do lote de {len(lote)} pacientes. Total deletados até agora: {total}")
        print(f"Deletados {total} exames no total para {len(pcts_ids)} pacientes.")
    
    append_query = """
        SELECT 
            s.*, 
            c.company_code, 
            c.hospital_id as company_id
        FROM "imparare2_isa_exame_gmr" s
        LEFT JOIN imparare_patient_company_treatment c 
            ON s.patient_id = c.record_id
            AND s.dthr_pedido between c.attendance_date AND c.discharge_date
            AND c.company_code IS NOT null
        WHERE s.resultado is not null;
    """

    df_iterator = dataRequest.get_data(queryText= append_query)

    with Pool(4) as pool:
        for _ in pool.imap_unordered(worker, zip(df_iterator, itertools.repeat(index_name))):
            pass

if __name__ == "__main__":
    main()
