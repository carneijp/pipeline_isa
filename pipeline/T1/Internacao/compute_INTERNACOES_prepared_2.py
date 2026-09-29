from ImpararePackage import maestro
from ImpararePackage import dataRequest
from datetime import datetime
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c:pd.DataFrame):
    try:
        destinos = ["los"]
        referencias = [["dthr_atendimento", "dthr_alta"]]
        c = maestro.difference_time_between_columns_days(df= c, arrayColunasDestino= destinos, arrayColunasReferencia= referencias)
        
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_internacoes_prepared", if_exists= "append")
    except Exception as e:
            print(f"Erro no processamento do bloco: {str(e)}")

def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_internacoes_prepared;
            CREATE UNLOGGED TABLE imparare2_internacoes_prepared (
                registro INTEGER,
                cd_atendimento INTEGER,
                dthr_atendimento TIMESTAMP,
                nmconvenio TEXT,
                unidade TEXT,
                especialidade TEXT,
                tipo_clinica TEXT,
                tipo_intern TEXT,
                dthr_alta TIMESTAMP,
                alta TEXT,
                los INTEGER
            );
        """
        dataRequest.execute(create_query)


    append_query = """
        SELECT 
            registro, 
            cd_atendimento, 
            dt_atendimento as dthr_atendimento, 
            nmconvenio, 
            "CODUNI||''||DESUNI" as unidade, 
            "CODESP||''||DESESP" as especialidade, 
            tipo_clinica, 
            tipo_intern, 
            dt_alta as dthr_alta, 
            alta
        FROM imparare2_internacoes_v2_stacked_by_cd_atendimento
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()