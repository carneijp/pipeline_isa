from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def create_columns(df: pd.DataFrame) -> pd.DataFrame:
    # df['termos_achados_distinct'] = df['termos_achados_agg'].apply(lambda x: x.split())
    df["termos_achados_distinct"] = df["termos_achados_agg"].str.rsplit()# transformou em uma lista
    df["termos_achados_distinct"] = df["termos_achados_distinct"].apply(lambda x: list(set(x))) # transformou em set e depois em lista de novo, removendo as duplicatas
    df["termos_achados_distinct"] = df["termos_achados_distinct"].astype("str") # transformou em string
    return df

def worker(c:pd.DataFrame):
    # Faz parecer que a operação feita aqui é só para pegar os distintos 
    # É mais razoavel fazer nos steps anteriores, adicionado mais um step para só mudar os distintos...
    c['termos_achados_agg'] = c['termos_achados_agg'].fillna('')

    c["termos_achados_agg"] = c["termos_achados_agg"].astype('str')
    
    tuplas: list[tuple[str, str]] = [("[", ""), ("]", ""), (" ", ""), ("'", ""), (",", " ")]
    c = maestro.replace_values_list(df= c, column= "termos_achados_agg", arrayDeTuplas= tuplas)

    c = create_columns(c)

    colunas = ["count", "termos_achados_agg"]
    c = maestro.remove_columns(df= c, arrayColumns= colunas)

    novosNomes = {
        "texto_termos_agg": "termos_texto",
        "termos_achados_distinct": "termos_achados"
    }
    c = maestro.rename_columns(df= c, DictColumns= novosNomes)
    
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_evol_sent_pos_grouped_dthr_prepared", if_exists= "append")

def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_evol_sent_pos_grouped_dthr_prepared;
            CREATE UNLOGGED TABLE imparare2_evol_sent_pos_grouped_dthr_prepared (
                registro INTEGER  NULL,
                dthr_evolucao DATE NULL,
                termos_texto TEXT NULL,
                texto_evolucao_agg TEXT NULL,
                termos_achados TEXT NULL,
                id_enterprise SMALLINT NULL
            );
        """
        dataRequest.execute(create_query)

    append_query = """
        SELECT DISTINCT 
            registro::integer AS registro,
            dthr_evolucao AS dthr_evolucao,
            string_agg(perfil_termos,  '/*---/*' order by dthr_evolucao_hr):: text AS texto_termos_agg, 
            string_agg(termos_achados,  ','):: text AS termos_achados_agg,
            string_agg(texto_evolucao,  '\n---\n' order by dthr_evolucao_hr):: text AS texto_evolucao_agg,
            id_enterprise::smallint AS id_enterprise
        FROM (
            SELECT 
                DISTINCT 
                registro, 
                dthr_evolucao, 
                dthr_evolucao_hr, 
                texto_evolucao, 
                termos_achados, 
                perfil_termos,
                id_enterprise
            FROM imparare2_evol_sent_pos_joined_prepared
        ) dku__subquery
        GROUP BY registro, id_enterprise, dthr_evolucao
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()