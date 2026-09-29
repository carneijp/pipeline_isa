from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c: pd.DataFrame):
    #c = maestro.extract_time(df= c, column= "data_pedido")
    #c = maestro.extract_time(df= c, column= "data_entrega")

    #destinos = ["data_pedido", "data_entrega"]
    #referencias = [["data_pedido_year", "data_pedido_month", "data_pedido_day"], 
     #           ["data_entrega_year", "data_entrega_month", "data_entrega_day"]]
    #separadores = ["-", "-"]
    #c = maestro.concatenate_columns(df= c, arrayDeReferencias= referencias, arrayDestinos= destinos, arraySeparadores= separadores)

    #destinos = ["data_pedido", "data_entrega"]
    #referencias = [["data_pedido", "hora_pedido"], ["data_entrega", "hora_entrega"]]
    #separadores = [" ", " "]
    #c = maestro.concatenate_columns(df= c, arrayDestinos= destinos, arrayDeReferencias= referencias, arraySeparadores= separadores, asTypeSTR= True)

    #c = maestro.parse_date(df= c, arrayColumns=["data_pedido", "data_entrega"], yearfirst=True)

    #colunas = [
     #   "xray_report_id",
     #   "data_entrega",
     #   'hora_entrega',
     #   "data_pedido",
     #   "hora_pedido",
     #   "data_pedido_year", "data_pedido_month", "data_pedido_day", 
     #  "data_entrega_year", "data_entrega_month", "data_entrega_day"
    #]
    #c = maestro.remove_columns(df= c, arrayColumns= colunas)

    c = maestro.to_int(df= c, column= "registro")
    c = maestro.to_int(df= c, column= "cd_ped_rx")

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_wellhead_hml_xray_followup_prepared", if_exists= "append")

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_wellhead_hml_xray_followup_prepared;
            CREATE UNLOGGED TABLE imparare2_wellhead_hml_xray_followup_prepared (
                registro INTEGER,
                xray_request_id INTEGER,
                cd_ped_rx INTEGER,
                ds_exa_rx TEXT,
                data_pedido TIMESTAMP,
                data_entrega TIMESTAMP,
                ds_laudo TEXT,
                attendance_type TEXT
            );
        """
        dataRequest.execute(create_query)
    append_query = f"""
        SELECT DISTINCT 
            xr.record_id AS registro,
            xr.xray_request_id AS xray_request_id,
            xr.xray_report_id AS cd_ped_rx,
            xr.xray_exam_description AS ds_exa_rx,
            xr.xray_request_date::date + xr.xray_request_hour::time AS data_pedido,
            xr.xray_delivery_date::date + xr.xray_delivery_hour::time AS data_entrega,
            xrays_documents.content AS ds_laudo,
            xr.attendance_type
        FROM xray_followup_report xr
        LEFT JOIN xrays_documents xrays_documents
            ON xr.id = xrays_documents."xrayFollowupReportId"
        WHERE xr.xray_request_id IS NOT null
            AND xr.xray_report_id IS NOT NULL
            AND UPPER(xr.xray_exam_description) ILIKE ANY(array['%ABDOME%', '%OSCOP%', '%TC%', '%RM%', '%TORAX%', '%PUNCAO%', '%RIN%', '%CATET%', '%DRENAGE%', '%OPERAT%', '%PERITO%']) 
            AND UPPER(xr.xray_exam_description) not ILIKE ALL(array['%ANGIO%', '%FLUXO%', '%FUNCION%'])
            AND (xr.record_id IN (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
        """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass
    

if __name__ == "__main__":
    main()
