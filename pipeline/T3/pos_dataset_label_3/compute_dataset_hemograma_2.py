from ImpararePackage import dataRequest

def main():
        # TODO: ACREDITO QUE ESSA QUERY ESTA ERRADA, ELE OLHA PARA A DATA DA ENTREGA DO EXAME, NAO PARA A DA COLETA
        # A COLETA SERIA A DATA DO PEDIDO, TALVEZ SEJA O CORRETO, POIS PACIENTE ESTAVA MAL DURANTE A COLETA E NAO NA ENTREGA
        # PACIENTE JA PODE TER MELHORADO NA ENTREGA.
        dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_exameslaboratorio_infecto_idx_1 ON "imparare2_exameslaboratorio_infecto"(registro, dthr_pedido);')

        dataRequest.execute('DROP TABLE IF EXISTS "imparare2_dataset_hemograma"')
        dataRequest.execute("""
                SET synchronous_commit = off;
                CREATE UNLOGGED TABLE "imparare2_dataset_hemograma" AS
                SELECT 
                        pct_dia.registro as prontuario, 
                        pct_dia.dia as dia,
                        -- HEMOCULTURA
                        (SELECT 
                                STRING_AGG(exa."BACTERIOLOGICO"::text, ' | ')
                         FROM imparare2_exameslaboratorio_infecto e 
                         WHERE e."BACTERIOLOGICO" IS NOT NULL 
                                AND  e.tipo_exame_infecto ILIKE '%HEMOCULTURA%POSITIVA%'
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                         GROUP BY pct_dia.registro,  pct_dia.dia
                        ) AS agg_hemocultura_futuro,
                        STRING_AGG(exa."BACTERIOLOGICO"::text, ' | ') FILTER (WHERE exa."BACTERIOLOGICO" IS NOT NULL AND exa.tipo_exame_infecto ILIKE '%HEMOCULTURA%POSITIVA%') AS agg_hemocultura_hoje,
                        (SELECT 
                                STRING_AGG(exa."BACTERIOLOGICO"::text, ' | ')
                         FROM imparare2_exameslaboratorio_infecto e
                         WHERE e."BACTERIOLOGICO" IS NOT NULL 
                                AND  e.tipo_exame_infecto ILIKE '%HEMOCULTURA%POSITIVA%'
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                         GROUP BY pct_dia.registro,  pct_dia.dia
                        ) AS agg_hemocultura_passado, 
                        -- UROCULTURA
                        (SELECT 
                                STRING_AGG(exa."BACTERIOLOGICO"::text, ' | ')
                         FROM imparare2_exameslaboratorio_infecto e 
                         WHERE e."BACTERIOLOGICO" IS NOT NULL AND 
                                e.tipo_exame_infecto ILIKE '%UROCULTURA%POSITIVA%'
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                         GROUP BY pct_dia.registro,  pct_dia.dia
                        ) AS agg_urocultura_futuro,
                        STRING_AGG(exa."BACTERIOLOGICO"::text, ' | ') FILTER (WHERE exa."BACTERIOLOGICO" IS NOT NULL AND exa.tipo_exame_infecto ILIKE '%UROCULTURA%POSITIVA%') AS agg_urocultura_hoje,
                        (SELECT 
                                STRING_AGG(exa."BACTERIOLOGICO"::text, ' | ')
                         FROM imparare2_exameslaboratorio_infecto e
                         WHERE e."BACTERIOLOGICO" IS NOT NULL AND 
                                e.tipo_exame_infecto ILIKE '%UROCULTURA%POSITIVA%'
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                         GROUP BY pct_dia.registro,  pct_dia.dia
                        ) AS agg_urocultura_passado,                
                        -- CULTURAS (todas)
                        (SELECT 
                                COUNT(DISTINCT e.exame_id)
                         FROM imparare2_exameslaboratorio_infecto e 
                         WHERE e.ds_resultado = 'POSITIVO'
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                        ) AS qtd_cultura_positiva_futuro,
                        (SELECT 
                                COUNT(DISTINCT e.exame_id) 
                         FROM imparare2_exameslaboratorio_infecto e
                         WHERE e.ds_resultado = 'POSITIVO'
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                        ) AS qtd_cultura_positiva_passado,
                        (SELECT 
                                COUNT(DISTINCT e.exame_id) 
                         FROM imparare2_exameslaboratorio_infecto e
                         WHERE e.ds_resultado = 'NEGATIVO' 
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                        ) AS qtd_cultura_sem_crescimento_futuro,
                        (SELECT 
                                COUNT(DISTINCT e.exame_id) 
                         FROM imparare2_exameslaboratorio_infecto e
                         WHERE e.ds_resultado = 'NEGATIVO' 
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                        ) AS qtd_cultura_sem_crescimento_passado,
                        (SELECT
                            CASE WHEN(COUNT(e.ds_resultado)) > 0 THEN 1 ELSE 0 END AS cultura_pos_categ
                            FROM imparare2_exameslaboratorio_infecto e
                         WHERE e.ds_resultado = 'POSITIVO' 
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia - INTERVAL '3 day' and pct_dia.dia
                        ) AS cultura_pos_categ_passado,
                        (SELECT
                            CASE WHEN(COUNT(e.ds_resultado)) > 0 THEN 1 ELSE 0 END AS cultura_pos_categ
                            FROM imparare2_exameslaboratorio_infecto e
                         WHERE e.ds_resultado = 'POSITIVO' 
                                AND pct_dia.registro = e.registro
                                AND e.dthr_pedido BETWEEN pct_dia.dia + INTERVAL '1 day' and pct_dia.dia + INTERVAL '3 day'
                        ) AS cultura_pos_categ_futuro
                FROM imparare2_dataset_label pct_dia
                LEFT JOIN imparare2_exameslaboratorio_infecto exa
                        ON pct_dia.registro = exa.registro
                        AND pct_dia.dia = exa.dthr_pedido
                GROUP BY pct_dia.registro, pct_dia.dia
        """)

if __name__ == "__main__":
    main()