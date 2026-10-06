from ImpararePackage import dataRequest

def main():
    query = """
        DROP TABLE IF EXISTS imparare2_new_isa_infeccao;
        
        SET synchronous_commit = off;

        CREATE UNLOGGED TABLE imparare2_new_isa_infeccao AS
            SELECT DISTINCT
                prontuario as paciente_id, 
                dia::date as dt_infeccao, 
                id_enterprise,
                month_start,
                month_end,
                month_quadrant, 
                proba_1
            FROM imparare2_new_isa_set_scored_casos_infeccao_rescaled;
    """

    dataRequest.execute(queryText= query)

if __name__ == "__main__":
    main()