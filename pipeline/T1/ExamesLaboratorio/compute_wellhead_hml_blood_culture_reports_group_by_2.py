from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c:pd.DataFrame):
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_wellhead_hml_blood_culture_prepared", if_exists= "append")

def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_wellhead_hml_blood_culture_prepared;
            CREATE UNLOGGED TABLE imparare2_wellhead_hml_blood_culture_prepared (
                registro INTEGER,
                atendimento INTEGER,
                exame TEXT,
                sector_name TEXT,
                tipo_atendimento TEXT,
                cd_exa_lab INTEGER,
                dthr_pedido TIMESTAMP,
                dthr_entrega TIMESTAMP,
                blood_culture_collection_date TIMESTAMP,
                ordem_amostra INTEGER,
                item_exame TEXT,
                ds_resultado TEXT,
                signature_date TIMESTAMP
            );
        """   
        dataRequest.execute(create_query)
    
    append_query = f"""
        SELECT DISTINCT 
            record_id AS registro, 
            attendance_id AS atendimento, 
            exam_lab_name AS exame, 
            sector_name, 
            attendance_type as tipo_atendimento, 
            laboratory_request_id AS cd_exa_lab, 
            DATE_TRUNC('minute', blood_culture_request_date) as dthr_pedido, 
            DATE_TRUNC('minute', blood_culture_collection_date) as blood_culture_collection_date, 
            DATE_TRUNC('minute', blood_culture_delivery_date) as dthr_entrega, 
            exam_result_question_order_id AS ordem_amostra, 
            exam_result_field_name AS item_exame, 
            exam_result_description AS ds_resultado, 
            signature_date
        FROM blood_culture_reports
        WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()