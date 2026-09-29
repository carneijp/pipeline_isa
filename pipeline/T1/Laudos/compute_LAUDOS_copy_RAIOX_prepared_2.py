from ImpararePackage import maestro
from ImpararePackage import dataRequest
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c: pd.DataFrame):

    c = maestro.to_int(df= c, column= "registro")
    c = maestro.to_int(df= c, column= "cd_ped_rx")

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_laudos_copy_raiox_prepared", if_exists=  "append")

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_laudos_copy_raiox_prepared;
            CREATE UNLOGGED TABLE imparare2_laudos_copy_raiox_prepared (
                registro INTEGER,
                xray_request_id INTEGER,
                cd_ped_rx INTEGER,
                data_pedido TIMESTAMP,
                data_entrega TIMESTAMP,
                ds_exa_rx TEXT,
                ds_laudo TEXT,
                attendance_type TEXT
            );
        """
        dataRequest.execute(create_query)

    append_query = f"""
        SELECT
            xr.record_id AS registro,
            xr.xray_request_id AS xray_request_id,
            xr.xray_report_id AS cd_ped_rx,
            xr.xray_exam_description AS ds_exa_rx,
            (xr.xray_request_date::date + xr.xray_request_hour::time) AS data_pedido,
            (xr.xray_delivery_date::date + xr.xray_delivery_hour::time) AS data_entrega,
            xrays_documents.content AS ds_laudo, 
            xr.attendance_type
        FROM xrays_reports xr
        INNER JOIN xrays_documents xrays_documents
            ON xr.id = xrays_documents."xrayReportId"
        WHERE xr.xray_request_id IS NOT NULL
            AND xr.xray_report_id IS NOT NULL
            AND UPPER(xr.xray_exam_description) ILIKE ANY(array['%ABDOME%', '%OSCOP%', '%TC%', '%RM%', '%TORAX%', '%PUNCAO%', '%RIN%', '%CATET%', '%DRENAGE%', '%OPERAT%', '%PERITO%']) 
            AND UPPER(xr.xray_exam_description) not ILIKE ALL(array['%ANGIO%', '%FLUXO%', '%FUNCION%'])
            AND (xr.record_id IN (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
            AND xr.xray_request_date IS NOT NULL
            AND xr.xray_delivery_date IS NOT null
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()