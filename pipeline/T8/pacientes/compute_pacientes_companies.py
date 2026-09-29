from ImpararePackage import dataRequest, maestro
import pandas as pd
from multiprocessing import Pool

def worker(c: pd.DataFrame):
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "isa_pacientes_companies", if_exists= "append", isLocal= False)
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "isa_pacientes_companies", if_exists= "append", isLocal= True)

def main():
    if maestro.get_must_update_all_patients() == "1":
        create_query = """
            DROP TABLE IF EXISTS isa_pacientes_companies;
            CREATE UNLOGGED TABLE isa_pacientes_companies (
                paciente_id int4,
                company_id uuid
            );
        """
        dataRequest.execute(create_query, isLocal= False)
        dataRequest.execute(create_query, isLocal= True)
    else:
        # Drop local table
        dataRequest.execute("DELETE FROM isa_pacientes_companies WHERE paciente_id in (select distinct record_id from patients_to_update)", isLocal= True)
        
        #Busca IDS para deleção
        df = dataRequest.get_data(queryText= f"SELECT distinct record_id::text FROM patients_to_update", chunck= None)
        pcts_ids = df['record_id'].tolist()

        ids = "(" + ",".join(pcts_ids) + ")"
        dataRequest.execute(f"DELETE FROM isa_pacientes_companies WHERE paciente_id in {ids}", isLocal= False)

    append_query = """ 
        SELECT DISTINCT
            record_id as paciente_id,
            hospital_id as company_id
        FROM imparare_patient_company_treatment;
    """

    df_iterator = dataRequest.get_data(queryText= append_query)

    with Pool(4) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()