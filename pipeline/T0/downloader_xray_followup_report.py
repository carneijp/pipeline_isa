from ImpararePackage import dataRequest
import pandas as pd

def main():
    print("Inicinado downloader_xray_followup_report")
    colunas_download = {
        "id": "uuid",
        "created_at": "date",
        "record_id": "integer",
        "xray_request_id": "integer",
        "xray_report_id": "integer",
        "xray_exam_description": "text",
        "xray_request_hour": "time",
        "xray_delivery_hour": "time",
        "xray_request_date": "date",
        "xray_delivery_date": "date",
        "attendance_type": "text"
    }
    query_dowloader = f"""
        SELECT
            {', '.join([f'{k}::{v}' for k, v in colunas_download.items()])}
        FROM xray_followup_report 
        WHERE xray_request_id IS NOT NULL
            AND xray_report_id IS NOT NULL
            AND xray_exam_description IS NOT null
            and adulthood = 'Pediatrico'
    """

    replace = True
    try:
        query_last_dowloaded_date = """
            SELECT 
                created_at 
            FROM xray_followup_report
            ORDER BY created_at DESC
            LIMIT 1
        """
        df = dataRequest.get_data(queryText= query_last_dowloaded_date, chunck= None)

        last_date = df.iloc[0]["created_at"]
        if last_date is not None and not pd.isna(last_date):
            query_dowloader += f" AND date(created_at) > '{last_date}'"
            print(f"Buscando todos os dados desde: {last_date}")    
            replace = False
    except:
        print(f"Erro na busca da ultima data, baixando tudo novamente")

    # Forçando buscar tudo novamente
    if replace:
        replace_query = f"""
            DROP TABLE IF EXISTS xray_followup_report;
            CREATE UNLOGGED TABLE xray_followup_report (
                {', '.join([f'{k} {v}' for k, v in colunas_download.items()])}
            );
        """
        dataRequest.execute(replace_query)

    create_index_wellhead = """CREATE INDEX IF NOT EXISTS idx_xray_followup_report_created_at_record_id ON xray_followup_report (company_code, (created_at::date), record_id);"""
    dataRequest.execute(create_index_wellhead, isWellheadEngine= True)
    create_index_local = """CREATE INDEX IF NOT EXISTS idx_xray_followup_report_created_at_record_id ON xray_followup_report (created_at, record_id);"""
    dataRequest.execute(create_index_local)

    df = dataRequest.get_data(queryText= query_dowloader, chunck= 10000, isWellheadEngine=True)
    count = 0
    for c in df:
        count += len(c)
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "xray_followup_report", if_exists= "append")

    print(f"Baixado no total: {count} linhas em xray_followup_report - downloader_xray_followup_report")
    
if __name__ == "__main__":
    main()

