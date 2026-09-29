from ImpararePackage import dataRequest
from ImpararePackage import maestro
import pandas as pd

def main():
    print("Inicinado downloader_xrays_documents")
    replace = True
    
    colunas_download = {
        "xrayReportId": "uuid",
        "xrayFollowupReportId": "uuid",
        "content": "text"
    }
    last_date_xray_reports = None
    sub_query_xrays_reports = f"""
        SELECT 
            id::uuid
        FROM xrays_reports
        WHERE xray_request_id IS NOT NULL
            AND xray_report_id IS NOT NULL
            AND xray_exam_description IS NOT NULL
            AND adulthood = 'Pediatrico'
            AND company_code in {maestro.get_hospitals_allowed_process_string_condition()}
            AND record_id IS NOT NULL
            AND xray_request_date IS NOT NULL
            AND xray_delivery_date IS NOT NULL
    """
    try:
        query_busca_ultima_data_xray_reports = """
            select 
                xr.updated_at  
            from xrays_reports xr 
            inner join xrays_documents xd 
                on xr.id = xd."xrayReportId"
            order by 1 desc
            limit 1
        """
        df = dataRequest.get_data(queryText= query_busca_ultima_data_xray_reports, chunck= None)
        last_date_xray_reports = df.iloc[0]["updated_at"]
        if last_date_xray_reports is not None and not pd.isna(last_date_xray_reports):
            last_date_xray_reports = pd.to_datetime(last_date_xray_reports)
            replace = False
    except:
        replace = True
        print("Falha em localizar a data do ultimo laudo de imagem do xray_reports")

    last_date_xray_followup_report = None
    sub_query_xrays_followup_report = """
        SELECT
            id::uuid
        FROM xray_followup_report 
        WHERE xray_request_id IS NOT NULL
            AND xray_report_id IS NOT NULL
            AND xray_exam_description IS NOT null
            AND adulthood = 'Pediatrico'
    """
    try:
        query_last_dowloaded_date = """
            select
                xfr.updated_at 
            from xray_followup_report xfr 
            inner join xrays_documents xd 
                on xfr.id = xd."xrayFollowupReportId" 
            order by 1 desc
            limit 1
        """
        df = dataRequest.get_data(queryText= query_last_dowloaded_date, chunck= None)

        last_date_xray_followup_report = df.iloc[0]["updated_at"]
        if last_date_xray_followup_report is not None and not pd.isna(last_date_xray_followup_report):
            last_date_xray_followup_report = pd.to_datetime(last_date_xray_followup_report)
            replace = False
    except:
        replace = True
        print("Falha em localizar a data do ultimo laudo de imagem do xray_followup_report")

    # Forcando buscar tudo novamente
    replace = True
    if replace:
        replace_query = f"""
            DROP TABLE IF EXISTS xrays_documents;
            CREATE UNLOGGED TABLE xrays_documents (
                {', '.join([f'"{k}" {v}' for k, v in colunas_download.items()])}
            );
        """
        dataRequest.execute(replace_query)
    else:
        if last_date_xray_reports is not None:
            sub_query_xrays_reports += f" AND updated_at > '{last_date_xray_reports}'"
        if last_date_xray_followup_report is not None:
            sub_query_xrays_followup_report += f" AND updated_at > '{last_date_xray_followup_report}'"

        print(f"Buscando todos os dados novos desde: {last_date_xray_reports}")

    query_dowloader = f"""
        select 
            {', '.join([f'"{k}"::{v}' for k, v in colunas_download.items()])} 
        from xrays_documents xd 
        where xd."xrayReportId" in (
            {sub_query_xrays_reports}
        ) or xd."xrayFollowupReportId" in (
            {sub_query_xrays_followup_report}
        )
    """
    df = dataRequest.get_data(queryText= query_dowloader, chunck= 10000, isWellheadEngine=True)
    count = 0
    for c in df:
        count += len(c)
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "xrays_documents", if_exists= "append")

    print(f"Baixado no total: {count} linhas em xrays_documents - downloader_xrays_documents")
    
if __name__ == "__main__":
    main()

