from ImpararePackage import dataRequest

def main():
        # TODO: ACREDITO QUE ESSA QUERY ESTA ERRADA, ELE OLHA PARA A DATA DA ENTREGA DO EXAME, NAO PARA A DA COLETA
        # A COLETA SERIA A DATA DO PEDIDO, TALVEZ SEJA O CORRETO, POIS PACIENTE ESTAVA MAL DURANTE A COLETA E NAO NA ENTREGA
        # PACIENTE JA PODE TER MELHORADO NA ENTREGA.
        dataRequest.execute("""
                SET synchronous_commit = off;
                
                DROP TABLE IF EXISTS imparare2_dataset_hemograma;

                CREATE UNLOGGED TABLE imparare2_dataset_hemograma AS
                SELECT 
                        pct_dia.registro as prontuario, 
                        pct_dia.dia as dia,
                        pct_dia.id_enterprise::smallint as id_enterprise,
                        -- HEMOCULTURA
                        (SELECT 
                                STRING_AGG(e.resultado_bacteriologico::text, ' | ')
                         FROM imparare2_wellhead_hml_blood_culture_prepared e 
                         WHERE e.resultado_bacteriologico IS NOT NULL 
							 AND e.exame ILIKE '%HEMOCULTURA%'
							 AND pct_dia.registro = e.registro
							 AND pct_dia.id_enterprise = e.id_enterprise
							 AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                         GROUP BY pct_dia.registro, pct_dia.dia, pct_dia.id_enterprise
                        ) AS agg_hemocultura_futuro,
                        STRING_AGG(exa.resultado_bacteriologico::text, ' | ') FILTER (WHERE exa.resultado_bacteriologico IS NOT NULL AND exa.exame ILIKE '%HEMOCULTURA%') AS agg_hemocultura_hoje,
                        (SELECT 
                                STRING_AGG(e.resultado_bacteriologico::text, ' | ')
                         FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacteriologico IS NOT NULL 
                            AND e.exame ILIKE '%HEMOCULTURA%'
                            AND pct_dia.registro = e.registro
                            AND pct_dia.id_enterprise = e.id_enterprise
                            AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                         GROUP BY pct_dia.registro, pct_dia.dia, pct_dia.id_enterprise
                        ) AS agg_hemocultura_passado, 
                        -- UROCULTURA
                        (SELECT 
                                STRING_AGG(e.resultado_bacteriologico::text, ' | ')
                         FROM imparare2_wellhead_hml_blood_culture_prepared e 
                         WHERE e.resultado_bacteriologico IS NOT NULL 
                     		AND e.exame ILIKE '%UROCULTURA%'
                            AND pct_dia.registro = e.registro
                            AND pct_dia.id_enterprise = e.id_enterprise
                            AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                         GROUP BY pct_dia.registro, pct_dia.dia, pct_dia.id_enterprise
                        ) AS agg_urocultura_futuro,
                        STRING_AGG(exa.resultado_bacteriologico::text, ' | ') FILTER (WHERE exa.resultado_bacteriologico IS NOT NULL AND exa.exame ILIKE '%UROCULTURA%') AS agg_urocultura_hoje,
                        (SELECT 
                                STRING_AGG(e.resultado_bacteriologico::text, ' | ')
                         FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacteriologico IS NOT NULL 
                     		AND e.exame ILIKE '%UROCULTURA%'
                            AND pct_dia.registro = e.registro
                            AND pct_dia.id_enterprise = e.id_enterprise
                            AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                         GROUP BY pct_dia.registro, pct_dia.dia, pct_dia.id_enterprise
                        ) AS agg_urocultura_passado,                
                        -- CULTURAS (todas)
                        (SELECT 
                                COUNT(DISTINCT e.cd_exa_lab)
                         FROM imparare2_wellhead_hml_blood_culture_prepared e 
                         WHERE e.resultado_bacterioscopico = 'POSITIVO'
                            AND pct_dia.registro = e.registro
                            AND pct_dia.id_enterprise = e.id_enterprise
                            AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                        )::SMALLINT AS qtd_cultura_positiva_futuro,
                        count(distinct exa.cd_exa_lab) filter (WHERE exa.resultado_bacterioscopico = 'POSITIVO')::SMALLINT AS qtd_cultura_positiva_hoje,
                        (SELECT 
                                COUNT(DISTINCT e.cd_exa_lab) 
                         FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacterioscopico = 'POSITIVO'
	                         AND pct_dia.registro = e.registro
	                         AND pct_dia.id_enterprise = e.id_enterprise
	                         AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                        )::SMALLINT AS qtd_cultura_positiva_passado,
                        (SELECT 
                                COUNT(DISTINCT e.cd_exa_lab) 
                         FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacterioscopico = 'NEGATIVO' 
                                AND pct_dia.registro = e.registro
                                AND pct_dia.id_enterprise = e.id_enterprise
                                AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                        )::SMALLINT AS qtd_cultura_sem_crescimento_futuro,
                        count(distinct exa.cd_exa_lab) filter (WHERE exa.resultado_bacterioscopico = 'NEGATIVO')::SMALLINT AS qtd_cultura_sem_crescimento_hoje,
                        (SELECT 
                                COUNT(DISTINCT e.cd_exa_lab) 
                         FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacterioscopico = 'NEGATIVO' 
                                AND pct_dia.registro = e.registro
                                AND pct_dia.id_enterprise = e.id_enterprise
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' AND pct_dia.dia
                        )::SMALLINT AS qtd_cultura_sem_crescimento_passado,
                        (SELECT
                            CASE WHEN(COUNT(DISTINCT e.cd_exa_lab)) > 0 THEN TRUE ELSE FALSE END AS cultura_pos_categ
                            FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacterioscopico = 'POSITIVO' 
                                AND pct_dia.registro = e.registro
                                AND pct_dia.id_enterprise = e.id_enterprise
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                        ) AS cultura_pos_categ_passado,
                        CASE WHEN (COUNT(DISTINCT exa.cd_exa_lab) FILTER (WHERE exa.resultado_bacterioscopico = 'POSITIVO')) > 0 THEN TRUE ELSE FALSE END AS cultura_pos_categ_hoje,
                        (SELECT
                            CASE WHEN(COUNT(DISTINCT e.cd_exa_lab)) > 0 THEN TRUE ELSE FALSE END AS cultura_pos_categ
                            FROM imparare2_wellhead_hml_blood_culture_prepared e
                         WHERE e.resultado_bacterioscopico = 'POSITIVO' 
                            AND pct_dia.registro = e.registro
                            AND pct_dia.id_enterprise = e.id_enterprise
                            AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' AND pct_dia.dia + INTERVAL '3 day'
                        ) AS cultura_pos_categ_futuro
                FROM imparare2_dataset_label pct_dia
                LEFT JOIN imparare2_wellhead_hml_blood_culture_prepared exa
                    ON pct_dia.id_enterprise = exa.id_enterprise 
                    	AND pct_dia.registro = exa.registro
                        AND pct_dia.dia = date(exa.dthr_pedido)
                GROUP BY pct_dia.registro, pct_dia.dia, pct_dia.id_enterprise;
        """)

if __name__ == "__main__":
    main()