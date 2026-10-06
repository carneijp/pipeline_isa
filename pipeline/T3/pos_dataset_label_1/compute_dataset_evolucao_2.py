from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""
        SET synchronous_commit = off;

        DROP TABLE IF EXISTS imparare2_dataset_evolucao;

        CREATE UNLOGGED TABLE imparare2_dataset_evolucao AS
            SELECT
				l.registro::int4 AS prontuario,
				l.dia,
				p.evo_passado,
				h.evolucao_aggr AS evo_hoje,
				h.unidade_fst,
				h.unidade_lst,
				coalesce(h.evol_count_sum, 0)::smallint AS evo_count_dia,
				f.evo_futuro,
                l.id_enterprise
            FROM imparare2_dataset_label l
            LEFT JOIN LATERAL (
                SELECT string_agg(e.evolucao_aggr, ' | ' ORDER BY e.data_dia) AS evo_passado
                FROM imparare2_evolucao_grouped e
                WHERE e.registro = l.registro
	                AND e.data_dia >= l.dia - INTERVAL '3 day'
	                AND e.data_dia <  l.dia
	                AND e.id_enterprise = l.id_enterprise
            ) p ON true
            LEFT JOIN LATERAL (
                SELECT string_agg(e.evolucao_aggr, ' | ' ORDER BY e.data_dia) AS evo_futuro
                FROM imparare2_evolucao_grouped e
                WHERE e.registro = l.registro
	                AND e.data_dia >  l.dia
	                AND e.data_dia <= l.dia + INTERVAL '3 day'
	                AND e.id_enterprise = l.id_enterprise
            ) f ON true
            LEFT JOIN imparare2_evolucao_grouped h
                ON h.registro = l.registro 
				AND h.data_dia = l.dia
				AND h.id_enterprise = l.id_enterprise;
    """)


if __name__ == "__main__":
    main()