from ImpararePackage import dataRequest
import pandas as pd
from multiprocessing import Pool, cpu_count

def worker_uploader(c: pd.DataFrame) -> int:
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "padrao_ouro", if_exists= "append")
    return len(c)

def main():
    print("Iniciando downloader_padrao_ouro")
    colunas_download = {
        "paciente_id": "integer", 
        "aval_dt_infec":"timestamp",
        "tipo_infeccao": "text",
        "outra_infec": "text",
        "avaliacao_responsavel": "text",
        "company_id": "uuid"
    }
    query_dowloader = f"""
        select  
            {', '.join([f'{k}::{v}' for k, v in colunas_download.items()])} 
        FROM isa_avaliacao
    """

    replace_query = f"""
        DROP TABLE IF EXISTS padrao_ouro;
        CREATE UNLOGGED TABLE padrao_ouro (
            {', '.join([f'{k} {v}' for k, v in colunas_download.items()])}
        );
    """
    dataRequest.execute(replace_query)

    df = dataRequest.get_data(queryText= query_dowloader, chunck= 10000, isLocal= False)
    count = 0
    with Pool(4) as pool:
        for result in pool.imap_unordered(worker_uploader, df):
            count += result
    
    print(f"Baixado no total: {count} linhas em padrao_ouro - downloader_padrao_ouro")
    
if __name__ == "__main__":
    main()