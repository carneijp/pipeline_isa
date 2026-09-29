from ImpararePackage import dataRequest
from ImpararePackage import maestro
import pandas as pd
from multiprocessing import Pool, cpu_count

def worker(c:pd.DataFrame):
    
    # Limpeza de marcadores tipo ( a ), ( b )
    c["new_sentence"] = c["sentence_original"].str.replace(r"\(\s*\w\s*\)", "", regex=True)
    
    # Normalização Maestro
    c = maestro.trim(df=c, column="new_sentence")

    tuplas = [
        (r"\r|\n", ". "),
        (r"\s+", " "),
    ]
    c = maestro.replace_values_list(df=c, arrayDeTuplas=tuplas, column="new_sentence", regex=True)
    c = maestro.normalize(df=c, column="new_sentence")

    # --- SALVAMENTO ---
    dataRequest.set_data_on_sql(df=c, nomeTabelaDestino="imparare2_evolucao_anon_data_trunc", if_exists="append")

def main():
    replace =True

    if replace:
        dataRequest.execute("""DROP TABLE if exists imparare2_evolucao_anon_data_trunc;""")
        create_query = """
                CREATE UNLOGGED TABLE imparare2_evolucao_anon_data_trunc (
                    registro INTEGER NULL,
                    perfil TEXT NULL,
                    unidade TEXT NULL,
                    sentence_original TEXT NULL,
                    new_sentence TEXT NULL,
                    tipo_atendimento TEXT NULL,
                    dthr_evolucao TIMESTAMP NULL,
                    data_dia DATE NULL
                );
            """
        dataRequest.execute(create_query)

    append_query = """
        SELECT 
            patient_id as registro, 
            perfil, 
            dthr_evolucao, 
            unidade,
            tipo_atendimento, 
            texto_evolucao as sentence_original,
            dthr_evolucao::date as data_dia 
        FROM imparare2_evolucao_prepared
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()