from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c:pd.DataFrame):
   
    c = maestro.trim(df= c, arrayColumns= ["texto_evolucao"])
    
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_evolucao_prepared", if_exists= "append")

def main():
    append_query = f"""
        SELECT 
            record_id AS patient_id, 
            pre_med_id AS cd_pre_med, 
            provider_profile AS perfil, 
            evolution_date AS dthr_evolucao,
            unity_code_and_description AS unidade, 
            STRING_AGG(distinct evolution_description, '. ')  AS texto_evolucao,
            attendance_type AS tipo_atendimento
        FROM evolutions_followup
        WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
        GROUP BY record_id, pre_med_id, provider_profile, evolution_date, unity_code_and_description, attendance_type
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass
if __name__ == "__main__":
    main()