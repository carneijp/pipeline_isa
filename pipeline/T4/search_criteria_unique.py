from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=Warning)

def worker(args: tuple[pd.DataFrame, int]):
    df = args
    allColumns = [f"texto{suffi}" for suffi in maestro.CRITERIOS_TEMPORAL_SUFFIX]
    for suffi in maestro.CRITERIOS_TEMPORAL_SUFFIX:
        c = df.copy()
        column = f"texto{suffi}"

        c[column] = c[column].apply(lambda x: maestro.split_sentences(str(x) if not isinstance(x, str) else x)).astype(str)

        c = maestro.creat_row_criterios_with_suffix_assign(c, maestro.CRITERIOS_FEATURE_EXTRACTION_MODELO, [suffi], mustCaptureNeg= False, mustCapturePos= False)
        
        c = maestro.operando_vetorizado_re_sanatized_with_suffix(c, maestro.CRITERIOS_FEATURE_EXTRACTION_MODELO, suffix= [suffi], mustCaptureNeg= False, mustCapturePos= False)
        
        c = c.drop(columns= allColumns)
        dataRequest.set_data_on_sql(df=c, nomeTabelaDestino= f"imparare2_search_criteria_dense{suffi}", if_exists= "append")

def main(): 
    replace = True

    if replace: 
        for s in maestro.CRITERIOS_TEMPORAL_SUFFIX:
            columns = ""
            for cri in maestro.CRITERIOS_FEATURE_EXTRACTION_MODELO:
                columns += f"{cri}{s} FLOAT4,\n"
                # columns += f"{cri}{s}_sent_pos text null,\n"
                columns += f"{cri}{s}_sent_pos_count SMALLINT,\n"

            columns = columns.strip(',\n')
            query_create_table = f"""
                DROP TABLE IF EXISTS imparare2_search_criteria_dense{s};
                CREATE UNLOGGED TABLE public.imparare2_search_criteria_dense{s} (
                    prontuario int8 NULL, 
                    dia timestamp NULL,
                    {columns}
                );
                CREATE INDEX imparare2_search_criteria_dense{s}_idx_1 ON public.imparare2_search_criteria_dense{s} USING btree(prontuario, dia);
            """
            dataRequest.execute(query_create_table)

    query = """
        SELECT 
            prontuario, 
            dia, 
            texto_futuro,
            texto_hoje,
            texto_passado
        FROM imparare2_coorte_notes_and_codes_text_prepared
    """

    df_iterator = dataRequest.get_data(queryText= query, chunck= 2000)

    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()