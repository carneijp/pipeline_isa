from ImpararePackage import dataRequest
from ImpararePackage  import maestro
import pandas as pd
from multiprocessing import Pool, cpu_count

def worker_uploader(c: pd.DataFrame) -> int:
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "surgeries_rgo", if_exists= "append")
    return len(c)

def main():
    print("Inciando downloader Cirurgias 4")
    colunas_download = {
        "created_at": "date",
        "record_id": "integer", 
        "attendance_id": "integer", 
        "attendance_type": "text",
        "provider_profile": "text",
        "provider_name": "text",
        "editor_registry_id": "integer",
        "provider_id ": "integer",
        "creation_date": "timestamp",
        "editor_registry_value": "text",
        "procedure_type": "text",   
        "close_date": "timestamp"
    }
    query_dowloader = f"""
        select 
            {', '.join([f'{k}::{v}' for k, v in colunas_download.items()])} 
        FROM surgeries_rgo 
        WHERE adulthood = 'Pediatrico' 
            AND company_code in {maestro.get_hospitals_allowed_process_string_condition()}
    """
    replace = True
    try:
        query_last_dowloaded_date = """
            SELECT 
                created_at 
            FROM surgeries_rgo
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
        print(f"Erro na busca da ultima data, baixando tudo novamente")

    if replace:
        replace_query = f"""
            DROP TABLE IF EXISTS surgeries_rgo;
            CREATE UNLOGGED TABLE surgeries_rgo (
                {', '.join([f'{k} {v}' for k, v in colunas_download.items()])}
            );
        """
        dataRequest.execute(replace_query)

    create_index_wellhead = """CREATE INDEX IF NOT EXISTS idx_surgeries_rgo_created_at_record_id ON surgeries_rgo (company_code, (created_at::date), record_id);"""
    dataRequest.execute(create_index_wellhead, isWellheadEngine= True)
    create_index_local = """CREATE INDEX IF NOT EXISTS idx_surgeries_rgo_created_at_record_id ON surgeries_rgo (created_at, record_id);"""
    dataRequest.execute(create_index_local)

    df = dataRequest.get_data(queryText= query_dowloader, chunck= 10000, isWellheadEngine=True)
    count = 0
    with Pool(4) as pool:
        for result in pool.imap_unordered(worker_uploader, df):
            count += result
    
    print(f"Baixado no total: {count} linhas em surgeries_rgo - downloader Cirurgias 4")

if __name__ == "__main__":
    main()