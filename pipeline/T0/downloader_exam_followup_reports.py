from ImpararePackage import dataRequest
from ImpararePackage import maestro
import pandas as pd
from multiprocessing import Pool, cpu_count

def worker_uploader(c: pd.DataFrame) -> int:
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "exam_followup_reports", if_exists= "append")
    return len(c)

def main():
    print ("Iniciando downloader_exam_followup_reports")
    colunas_download = {
        "record_id": "integer",
        "created_at": "date",
        "exam_lab_id": "integer",
        "exam_lab_name": "text",
        "laboratory_request_date": "timestamp",
        "laboratory_request_delivery_date": "timestamp",
        "exam_result_field_name": "text",
        "exam_result_description": "text",
        "attendance_type": "text"
    }
    query_dowloader = f"""
        SELECT DISTINCT
            {', '.join([f'{k}::{v}' for k, v in colunas_download.items()])}
        FROM exam_followup_reports
        WHERE adulthood = 'Pediatrico'
            AND company_code in {maestro.get_hospitals_allowed_process_string_condition()}
            AND record_id IS NOT NULL
    """

    replace = True
    try:
        query_last_dowloaded_date = """
            SELECT 
                created_at 
            FROM exam_followup_reports
            ORDER BY created_at DESC
            LIMIT 1
        """
        df = dataRequest.get_data(queryText= query_last_dowloaded_date, chunck= None)

        last_date = df.iloc[0]["created_at"]
        if last_date is not None and not pd.isna(last_date):
            query_dowloader += f" AND date(created_at) > '{last_date}'"
            print(f"Buscando todos os dados novos desde: {last_date}")
            replace = False
    except:
        print(f"Erro na busca da ultima data de liberação, baixando tudo novamente")

    if replace:
        replace_query = f"""
            DROP TABLE IF EXISTS exam_followup_reports;
            CREATE UNLOGGED TABLE exam_followup_reports (
                {', '.join([f'{k} {v}' for k, v in colunas_download.items()])}
            );
        """
        dataRequest.execute(replace_query)

    create_index_wellhead = """CREATE INDEX IF NOT EXISTS idx_exam_followup_reports_created_at_record_id ON exam_followup_reports (company_code, (created_at::date), record_id);"""
    dataRequest.execute(create_index_wellhead, isWellheadEngine= True)
    create_index_local = """CREATE INDEX IF NOT EXISTS idx_exam_followup_reports_created_at_record_id ON exam_followup_reports (created_at, record_id);"""
    dataRequest.execute(create_index_local)

    df = dataRequest.get_data(queryText= query_dowloader, chunck= 10000, isWellheadEngine=True)
    count = 0
    with Pool(4) as pool:
        for result in pool.imap_unordered(worker_uploader, df):
            count += result
    
    print(f"Baixado no total: {count} linhas em exam_followup_reports - downloader_exam_followup_reports")

if __name__ == "__main__":
    main()