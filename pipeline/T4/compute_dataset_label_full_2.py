from ImpararePackage import dataRequest
from ImpararePackage import maestro

def main():
    dataRequest.execute('CREATE INDEX IF NOT EXISTS idx_dataset_intermediario ON "imparare2_dataset_label_intermediario" (prontuario, dia);')
    

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_dataset_label_full"')
    columns = ""
    joins = ""
    for s in maestro.CRITERIOS_TEMPORAL_SUFFIX:
        dataRequest.execute(f'CREATE INDEX IF NOT EXISTS idx_search_criteria_dense{s} ON imparare2_search_criteria_dense{s} (prontuario, dia);')
        for cri in maestro.CRITERIOS_FEATURE_EXTRACTION_MODELO:
            columns += f"df_cri{s}.{cri}{s},\n"
            columns += f"df_cri{s}.{cri}{s}_sent_pos_count,\n"

        joins += f"""LEFT JOIN imparare2_search_criteria_dense{s} df_cri{s}
                ON df_i.prontuario = df_cri{s}.prontuario
                AND df_i.dia = df_cri{s}.dia\n"""

    columns = columns.strip(',\n')
    joins = joins.strip('\n')
    query = f"""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_dataset_label_full" AS
        SELECT DISTINCT 
            df_i.*,
            {columns}
        FROM "imparare2_dataset_label_intermediario" df_i
        {joins};
    """
    try:
        dataRequest.execute(query)
    except Exception as e:
        with open("error_log.txt", "a") as log_file:    
            log_file.write(f"Error executing query: {e}\n")
            log_file.write(f"Query: {query}\n")
        print(f"Error executing query: {e}")
        raise e
    # dataRequest.execute(query)

if __name__ == "__main__":
    main()