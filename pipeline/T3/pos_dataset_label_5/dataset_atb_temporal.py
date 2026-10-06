from ImpararePackage import dataRequest


def main():
    dataRequest.execute("""
        SET synchronous_commit = off;
        DROP TABLE IF EXISTS imparare2_dataset_prescricao_ab;
        CREATE UNLOGGED TABLE imparare2_dataset_prescricao_ab AS
            SELECT 
                evo.registro as prontuario,
                evo.dia,
                evo.id_enterprise::SMALLINT as id_enterprise,
                COALESCE(SUM("ATB_COMUNITARIO_count"), 0)::SMALLINT AS "ATB_COMUNITARIO_count", 
                COALESCE(SUM("ATB_TOPICO_count"), 0)::SMALLINT AS "ATB_TOPICO_count", 
                COALESCE(SUM("ATB_INTERMEDIARIO_count"), 0)::SMALLINT AS "ATB_INTERMEDIARIO_count", 
                COALESCE(SUM("ATB_HOSPITALAR_count"), 0)::SMALLINT AS "ATB_HOSPITALAR_count",
                COALESCE(SUM("ATB_MMR_count"), 0)::SMALLINT AS "ATB_MMR_count", 
                COALESCE(SUM("ATB_ANTIFUNGICO_count"), 0)::SMALLINT AS "ATB_ANTIFUNGICO_count", 
                COALESCE(SUM("ATB_OUTROS_count"), 0)::SMALLINT AS "ATB_OUTROS_count",
                COALESCE(SUM("ATB_PROFILATICO_count"), 0)::SMALLINT AS "ATB_PROFILATICO_count",
                COALESCE(MAX(atb_categ), 0)::SMALLINT AS atb_categ,
                COALESCE(MAX(via_categ), 0)::SMALLINT AS via_categ,
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM("ATB_COMUNITARIO_count" + 
                                "ATB_TOPICO_count" + 
                                "ATB_INTERMEDIARIO_count" + 
                                "ATB_HOSPITALAR_count" + 
                                "ATB_MMR_count" + 
                                "ATB_ANTIFUNGICO_count" + 
                                "ATB_OUTROS_count"), 0)
                        FROM imparare2_prescricoesantibiotico_by_prontuario antb
                        WHERE antb.prontuario = evo.registro
                            AND evo.id_enterprise = antb.id_enterprise
                            AND antb.dthr_prescricao BETWEEN evo.dia - INTERVAL '3 day' AND evo.dia - INTERVAL '1 day'
                    ) > 0 THEN TRUE
                    ELSE FALSE
                END AS atb_em_uso_passado,
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM("ATB_COMUNITARIO_count" + 
                                "ATB_TOPICO_count" + 
                                "ATB_INTERMEDIARIO_count" + 
                                "ATB_HOSPITALAR_count" + 
                                "ATB_MMR_count" + 
                                "ATB_ANTIFUNGICO_count" + 
                                "ATB_OUTROS_count"), 0)
                        FROM imparare2_prescricoesantibiotico_by_prontuario antb
                        WHERE antb.prontuario = evo.registro
                            AND evo.id_enterprise = antb.id_enterprise
                            AND antb.dthr_prescricao = evo.dia
                    ) > 0 THEN TRUE
                    ELSE FALSE
                END AS atb_em_uso_hoje,
                CASE 
                    WHEN (
                        SELECT COALESCE (
                            SUM("ATB_COMUNITARIO_count" + 
                                "ATB_TOPICO_count" + 
                                "ATB_INTERMEDIARIO_count" + 
                                "ATB_HOSPITALAR_count" + 
                                "ATB_MMR_count" + 
                                "ATB_ANTIFUNGICO_count" + 
                                "ATB_OUTROS_count"), 0)
                        FROM imparare2_prescricoesantibiotico_by_prontuario antb
                        WHERE antb.prontuario = evo.registro
                            AND evo.id_enterprise = antb.id_enterprise
                            AND antb.dthr_prescricao BETWEEN evo.dia + INTERVAL '1 day' AND evo.dia + INTERVAL '3 day'
                    ) > 0 THEN TRUE
                    ELSE FALSE
                END AS atb_em_uso_futuro
            FROM imparare2_dataset_label evo -- me questiono sobre o join ser feito com as evos, como avaliar se estamos perdendo atbs?
            LEFT JOIN imparare2_prescricoesantibiotico_by_prontuario antb
                ON antb.prontuario = evo.registro
                    AND evo.id_enterprise = antb.id_enterprise
                    AND antb.dthr_prescricao BETWEEN evo.dia - INTERVAL '3 day' AND evo.dia + INTERVAL '3 day'
            GROUP BY evo.registro, evo.dia, evo.id_enterprise;
    """)

if __name__ == "__main__":
    main()