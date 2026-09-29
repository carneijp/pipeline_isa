from ImpararePackage import dataRequest
from ImpararePackage import maestro
import pandas as pd
import threading
from multiprocessing import Pool, cpu_count
import itertools

def worker(args: tuple[pd.DataFrame, str]):
    c, index_name = args

    novosNomes = {
        "registro": "id",
        "dt_nascimento_parsed": "dt_nascimento",
    }
    c = maestro.rename_columns(df= c, DictColumns= novosNomes)
        
    tuplas = [("NA", "Não Identificado")]
    c = maestro.replace_values_list(df= c, column= "nome", arrayDeTuplas= tuplas, exect= True)

    c["nome"] = c.apply(lambda x: str(x["id"]) if(x["id"] == "Não Identificado") else str(x["id"]) + " - " + str(x["nome"]), axis= 1)
        
    # c = maestro.incrise_by_n_hours(df= c, column= "dt_nascimento", hours= 3)

    def elk_upload(c: pd.DataFrame, index_name: str):
        client = dataRequest.ELASTICSEARCH_CONNECTION
        c = maestro.keep_columns(df= c, arrayColumns= [
            "id",
            "sexo",
            "dt_nascimento",
            "idade_hoje",
            "nome"
         ])
        actions = maestro.generate_actions(c, index_name)
        maestro.bulk_upload_with_retry(client, actions, context="pacientes", thread_count=1)
    print("Iniciando uploads!")
    table = "isa_pacientes"
    job = threading.Thread(target= elk_upload, args=(c.copy(), index_name))
    job_2 = threading.Thread(target=dataRequest.set_data_on_sql, args=(c, table), kwargs={"if_exists": "append", "isLocal": False})
    job_3 = threading.Thread(target=dataRequest.set_data_on_sql, args=(c, table), kwargs={"if_exists": "append", "isLocal": True})
    
    jobs = [
        job, 
        job_2, 
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

    index_name = maestro.getELKIndexValue("pacientes")
    if maestro.get_must_update_all_patients() == '1':
        create_query = """
            DROP TABLE IF EXISTS isa_pacientes;
            CREATE UNLOGGED TABLE isa_pacientes (
                id INTEGER,
                nome TEXT,
                dt_nascimento TIMESTAMP,
                sexo TEXT,
                idade_hoje FLOAT4,
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
                settings={"index": {"max_result_window": 100000}}
            )
            maestro.wait_for_index_health(client, index_name)
    else:
        # Drop local table
        dataRequest.execute("DELETE FROM isa_pacientes WHERE id in (select distinct record_id from patients_to_update)", isLocal= True)
        
        #Busca IDS para deleção
        df = dataRequest.get_data(queryText= f"SELECT distinct record_id::text FROM patients_to_update", chunck= None)
        pcts_ids = df['record_id'].tolist()

        # Drop Banco aws
        ids = "(" + ",".join(pcts_ids) + ")"
        dataRequest.execute(f"DELETE FROM isa_pacientes WHERE id in {ids}", isLocal= False)

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
                        "id": lote
                    }
                },
                conflicts= "proceed",
                refresh= True,
                slices= "auto"
            )
            total += resp['deleted']
            print(f"Deletados {resp['deleted']} pacientes do lote de {len(lote)} pacientes. Total deletados até agora: {total}")
        print(f"Deletados {total} pacientes no total para {len(pcts_ids)} pacientes.")

    append_query = """ 
        WITH s AS (
            SELECT DISTINCT         
                I.registro, 
                I.sexo, 
                I.dt_nascimento_parsed,
                EXTRACT(YEAR FROM AGE(date_trunc('day', ld.dia), I.dt_nascimento_parsed)) AS idade_hoje,
                pr."patient_name" as nome
            FROM "imparare2_pacientes_prepared" as I
            INNER JOIN (
                select
                    prontuario,
                    max(dia) as dia
                FROM imparare2_dataset_label_full
                GROUP BY prontuario
            ) ld
                ON ld.prontuario = I.registro
            LEFT JOIN "patients_records" as pr
            ON I.registro = pr."record_id"
        )
        SELECT DISTINCT
            s.*,
            c.company_code, 
            c.hospital_id as company_id
        FROM s
        LEFT JOIN imparare_patient_company_treatment c ON s.registro = c.record_id
        WHERE c.company_code IS NOT NULL
    """

    df_iterator = dataRequest.get_data(queryText= append_query)

    with Pool(4) as pool:
        for _ in pool.imap_unordered(worker, zip(df_iterator, itertools.repeat(index_name))):
            pass
        

if __name__ == "__main__":
    main()