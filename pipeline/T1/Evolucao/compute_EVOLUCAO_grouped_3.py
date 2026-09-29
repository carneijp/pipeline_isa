from ImpararePackage import dataRequest

def main():
    """Pega todos os pacientes que tiveram evolução médica e calcula o numero de evoluções que eles tiveram e também agrupa as evoluções descobre qual foi a primeira unidade do paciente no dia a sua ultima unidade hospitalar e em quantas unidades distintas ele passou"""

    dataRequest.execute("""
        SET synchronous_commit = off;
        
        CREATE INDEX IF NOT EXISTS imparare2_evolucao_anon_data_trunc_idx_1  ON imparare2_evolucao_anon_data_trunc(registro, data_dia);

        DROP TABLE IF EXISTS imparare2_evolucao_grouped;

        CREATE UNLOGGED TABLE imparare2_evolucao_grouped AS
            SELECT
                registro::int4 AS registro,
                data_dia::date AS data_dia,
                string_agg(date(dthr_evolucao) || ': ' || new_sentence, ' | ' ORDER BY dthr_evolucao) AS evolucao_aggr,
                coalesce((array_agg(unidade ORDER BY dthr_evolucao) FILTER (WHERE unidade IS NOT NULL AND unidade <> ''))[1], 'Não informado') AS unidade_fst,
                coalesce((array_agg(unidade ORDER BY dthr_evolucao DESC) FILTER (WHERE unidade IS NOT NULL AND unidade <> ''))[1], 'Não informado') AS unidade_lst,
                count(DISTINCT unidade) FILTER (WHERE unidade IS NOT NULL AND unidade <> '')::smallint AS movimento_unidade_count,
                count(*)::smallint AS evol_count_sum
            FROM imparare2_evolucao_anon_data_trunc
            GROUP BY registro, data_dia;
    """)

if __name__ == "__main__":
    main()