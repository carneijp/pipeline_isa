from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""
        SET synchronous_commit = off;
        
        CREATE INDEX IF NOT EXISTS imparare2_evolucao_grouped_idx_1 ON imparare2_evolucao_grouped(registro, data_dia);

        DROP TABLE IF EXISTS imparare2_dataset_evolucao;

        CREATE UNLOGGED TABLE imparare2_dataset_evolucao AS
            SELECT
                l.registro::int4 AS prontuario,
                l.dia,
                p.evo_passado,
                h.evolucao_aggr AS evo_hoje,
                h.unidade_fst,
                h.unidade_lst,
                coalesce(h.evol_count_sum, 0)::int4 AS evo_count_dia,
                f.evo_futuro
            FROM imparare2_dataset_label l
            LEFT JOIN LATERAL (
                SELECT string_agg(e.evolucao_aggr, ' | ' ORDER BY e.data_dia) AS evo_passado
                FROM imparare2_evolucao_grouped e
                WHERE e.registro = l.registro
                AND e.data_dia >= l.dia - INTERVAL '3 day'
                AND e.data_dia <  l.dia
            ) p ON true
            LEFT JOIN LATERAL (
                SELECT string_agg(e.evolucao_aggr, ' | ' ORDER BY e.data_dia) AS evo_futuro
                FROM imparare2_evolucao_grouped e
                WHERE e.registro = l.registro
                AND e.data_dia >  l.dia
                AND e.data_dia <= l.dia + INTERVAL '3 day'
            ) f ON true
            LEFT JOIN imparare2_evolucao_grouped h
                ON h.registro = l.registro AND h.data_dia = l.dia;
    """)


if __name__ == "__main__":
    main()