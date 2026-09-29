from ImpararePackage import dataRequest, maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c = pd.DataFrame):
    
    c = maestro.to_str_format(df= c, column= "laudos_dia")

    tuplas = [("None", "")]
    c = maestro.replace_values_list(df= c, column= "laudos_dia", arrayDeTuplas= tuplas)

    c = maestro.normalize(df= c, column= "laudos_dia")

    c = maestro.trim(df= c, column= "laudos_dia")

    tuplas = [("rx de torax", "rx de torax ")]
    c = maestro.replace_values_list(df= c, column= "laudos_dia", arrayDeTuplas= tuplas)#, regex=True) 

    tuplas = [
        (r"\n", r". "), (r"\|", r". "), (r"\s\.\s", r". "), (r"\s\s", r". "), (r"\.+", r"."), (r" +", r" ")
    ]
    c = maestro.replace_values_list(df= c, column= "laudos_dia", arrayDeTuplas= tuplas, regex=True) 

    c = maestro.to_int(df= c, column= "REGISTRO")

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_raiox_computed", if_exists= "append")

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS "imparare2_raiox_computed";
            CREATE UNLOGGED TABLE "imparare2_raiox_computed" (
                registro INTEGER,
                data DATE,
                laudos_dia TEXT,
                count_laudos_dia INTEGER
            );                
        """
        dataRequest.execute(create_query)
    
    append_query = """
        SELECT 
            RX.registro, 
            date(RX.data_entrega) AS data,
            string_agg(RX."ds_laudo",' | ' order by RX."data_entrega") AS laudos_dia,
            count(*) AS count_laudos_dia
        FROM "imparare2_laudos_copy_raiox_prepared" AS RX
        GROUP BY RX.registro , date(RX.data_entrega )
    """
    
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass
    
if __name__ == "__main__":
    main()