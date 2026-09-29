from ImpararePackage import dataRequest


def main():
    dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_prescricoesantibiotico_by_prontuario_idx_1 ON "imparare2_prescricoesantibiotico_by_prontuario"(prontuario, dthr_prescricao);')

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_dataset_prescricao_ab"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_dataset_prescricao_ab" AS
            SELECT 
                evo.registro as prontuario,
                evo."dia",
                COALESCE(SUM(antb."ATB_COMUNITARIO_count"), 0) AS "ATB_COMUNITARIO_count", 
                COALESCE(SUM(antb."ATB_TOPICO_count"), 0) AS "ATB_TOPICO_count", 
                COALESCE(SUM(antb."ATB_INTERMEDIARIO_count"), 0) AS "ATB_INTERMEDIARIO_count", 
                COALESCE(SUM(antb."ATB_HOSPITALAR_count"), 0) AS "ATB_HOSPITALAR_count",
                COALESCE(SUM(antb."ATB_MMR_count"), 0) AS "ATB_MMR_count", 
                COALESCE(SUM(antb."ATB_ANTIFUNGICO_count"), 0) AS "ATB_ANTIFUNGICO_count", 
                COALESCE(SUM(antb."ATB_OUTROS_count"), 0) AS "ATB_OUTROS_count",
                COALESCE(SUM(antb."ATB_PROFILATICO_count"), 0) AS "ATB_PROFILATICO_count",
                COALESCE(MAX(antb."atb_categ"), 0) AS "atb_categ",
                COALESCE(MAX(antb."via_categ"), 0) AS "via_categ",
                -- COALESCE(SUM(antb."via_TOPICO_count"), 0)                          AS "via_TOPICO_count",
                -- SUM(antb."via_OUTRO_count")                           AS "via_OUTRO_count",
                -- SUM(antb."via_PARENTERAL_count")                      AS "via_PARENTERAL_count",
                -- SUM(antb."via_ENTERAL_count")                         AS "via_ENTERAL_count",
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM(antb."ATB_COMUNITARIO_count" + 
                                antb."ATB_TOPICO_count" + 
                                antb."ATB_INTERMEDIARIO_count" + 
                                antb."ATB_HOSPITALAR_count" + 
                                antb."ATB_MMR_count" + 
                                antb."ATB_ANTIFUNGICO_count" + 
                                antb."ATB_OUTROS_count"), 0)
                        FROM "imparare2_prescricoesantibiotico_by_prontuario" antb
                        WHERE antb.prontuario = evo.registro
                        AND antb."dthr_prescricao"
                            BETWEEN evo."dia" - INTERVAL '3 day'
                            AND evo."dia" - INTERVAL '1 day'
                    ) > 0 THEN 1
                    ELSE 0
                END AS "atb_em_uso_passado",
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM(antb."ATB_COMUNITARIO_count" + 
                                antb."ATB_TOPICO_count" + 
                                antb."ATB_INTERMEDIARIO_count" + 
                                antb."ATB_HOSPITALAR_count" + 
                                antb."ATB_MMR_count" + 
                                antb."ATB_ANTIFUNGICO_count" + 
                                antb."ATB_OUTROS_count"), 0)
                        FROM "imparare2_prescricoesantibiotico_by_prontuario" antb
                        WHERE antb.prontuario = evo.registro
                        AND antb."dthr_prescricao" = evo."dia"
                    ) > 0 THEN 1
                    ELSE 0
                END AS "atb_em_uso_hoje",
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM(antb."ATB_COMUNITARIO_count" + 
                                antb."ATB_TOPICO_count" + 
                                antb."ATB_INTERMEDIARIO_count" + 
                                antb."ATB_HOSPITALAR_count" + 
                                antb."ATB_MMR_count" + 
                                antb."ATB_ANTIFUNGICO_count" + 
                                antb."ATB_OUTROS_count"), 0)
                        FROM "imparare2_prescricoesantibiotico_by_prontuario" antb
                        WHERE antb.prontuario = evo.registro
                        AND antb."dthr_prescricao"
                            BETWEEN evo."dia" + INTERVAL '1 day'
                            AND evo."dia" + INTERVAL '3 day'
                    ) > 0 THEN 1
                    ELSE 0
                END AS "atb_em_uso_futuro",
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM(antb."ATB_COMUNITARIO_count" + 
                                antb."ATB_TOPICO_count" + 
                                antb."ATB_INTERMEDIARIO_count" + 
                                antb."ATB_HOSPITALAR_count" + 
                                antb."ATB_MMR_count" + 
                                antb."ATB_ANTIFUNGICO_count" + 
                                antb."ATB_OUTROS_count"), 0)
                        FROM "imparare2_prescricoesantibiotico_by_prontuario" antb
                        WHERE antb.prontuario = evo.registro
                        ) > 0 THEN 1
                    ELSE 0
                END AS "atb_em_uso"
            FROM "imparare2_dataset_label" evo -- me questiono sobre o join ser feito com as evos, como avaliar se estamos perdendo atbs?
            LEFT JOIN "imparare2_prescricoesantibiotico_by_prontuario" antb
                ON antb.prontuario = evo.registro
                AND antb."dthr_prescricao"
                    BETWEEN evo."dia" - INTERVAL '3 day'
                        AND evo."dia" + INTERVAL '3 day'
            GROUP BY evo.registro, evo.dia;
    """)

if __name__ == "__main__":
    main()