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
        
        create index IF NOT EXISTS new_isa_infeccao_idx ON imparare2_new_isa_infeccao(id_enterprise, paciente_id, CAST(dt_infeccao AS DATE));
    """

    dataRequest.execute(queryText= query)

if __name__ == "__main__":
    main()