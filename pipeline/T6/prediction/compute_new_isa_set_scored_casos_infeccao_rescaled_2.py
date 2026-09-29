from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_new_isa_set_scored_casos_infeccao_rescaled";')
    
    query = """
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE imparare2_new_isa_set_scored_casos_infeccao_rescaled AS
        WITH max_value AS(
            SELECT 
                MAX(proba_1)::decimal as max_proba
            FROM imparare2_new_isa_set_scored_casos_infeccao
        ), dados_calc AS (
            SELECT
                prontuario,
                dia,
                proba_1,
                prediction,
                CEILING(proba_1::decimal * 1000.0/(SELECT max_proba FROM max_value))/1000.0 as rescaled_proba_1,
                date_trunc('month', dia::date)::date as month_start,
                (date_trunc('month', dia::date)::date + INTERVAL '1 month')::date as month_end,
                CASE
                    WHEN EXTRACT(day FROM dia::date) BETWEEN 1 AND 7 THEN 1
                    WHEN EXTRACT(day FROM dia::date) BETWEEN 8 AND 14 THEN 2
                    WHEN EXTRACT(day FROM dia::date) BETWEEN 15 AND 21 THEN 3
                    ELSE 4
                END AS month_quadrant
            FROM imparare2_new_isa_set_scored_casos_infeccao
        )
        SELECT DISTINCT 
            prontuario, 
            dia, 
            proba_1, 
            prediction, 
            rescaled_proba_1, 
            month_start, 
            month_end, 
            month_quadrant
        FROM dados_calc
        ORDER BY prontuario, dia;
    """

    dataRequest.execute(queryText= query)
    dataRequest.execute('CREATE INDEX IF NOT EXISTS idx_casos_infeccao_rescaled ON imparare2_new_isa_set_scored_casos_infeccao_rescaled (prontuario, dia);')

if __name__ == "__main__":
    main()