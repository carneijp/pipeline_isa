from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""
        SET synchronous_commit = off;
        
        DROP TABLE IF EXISTS imparare2_dataset_sangue_categ_temporal;

        CREATE UNLOGGED TABLE imparare2_dataset_sangue_categ_temporal as
            SELECT
                pct_dia.registro,
                pct_dia.dia,
                pct_dia.id_enterprise::SMALLINT AS id_enterprise,
                hoje.data_requisicao_exame,
                hoje.leuco_min, hoje.leuco_max, hoje.leuco_avg,
                hoje.rdw_min,   hoje.rdw_max,   hoje.rdw_avg,
                hoje.neuto_min, hoje.neuto_max, hoje.neuto_avg,
                hoje.pcr_min,   hoje.pcr_max,   hoje.pcr_avg,
                futuro.leuco_alterada              AS leuco_alterado_futuro,
                futuro.leucocitose                 AS leucocitose_futuro,
                futuro.leucopenia                  AS leucopenia_futuro,
                futuro.rdw_alterada                AS rdw_alterado_futuro,
                futuro.neutrof_alterado            AS neutro_alterado_futuro,
                futuro.pcr_alterada                AS pcr_alterada_futuro,
                futuro.clostridium_positivo        AS clostridium_positivo_futuro,
                futuro.mrsa_positivo               AS mrsa_positivo_futuro,
                futuro.virus_resp_positivo         AS virus_resp_positivo_futuro,
                futuro.liquor_glicose              AS glicose_liquor_alterada_futuro,
                futuro.liquor_proteina             AS proteina_liquor_alterada_futuro,
                passado.leuco_alterada             AS leuco_alterado_passado,
                passado.leucocitose                AS leucocitose_passado,
                passado.leucopenia                 AS leucopenia_passado,
                passado.rdw_alterada               AS rdw_alterado_passado,
                passado.neutrof_alterado           AS neutro_alterado_passado,
                passado.pcr_alterada               AS pcr_alterada_passado,
                passado.clostridium_positivo       AS clostridium_positivo_passado,
                passado.mrsa_positivo              AS mrsa_positivo_passado,
                passado.virus_resp_positivo        AS virus_resp_positivo_passado,
                passado.liquor_glicose             AS glicose_liquor_alterada_passado,
                passado.liquor_proteina            AS proteina_liquor_alterada_passado,
                hoje."LEUCO_ALTERADA",
                hoje."LEUCOCITOSE",
                hoje."LEUCOPENIA",
                hoje."RDW_ALTERADA",
                hoje."NEUTROF_ALTERADO",
                hoje."PCR_ALTERADA",
                hoje."CLOSTRIDIUM_POSITIVO",
                hoje."MRSA_POSITIVO",
                hoje."VIRUS_RESPIRATORIO_POSITIVO",
                hoje."LIQUOR_ALTERA_GLICOSE",
                hoje."LIQUOR_ALTERA_PROTEINA"
            FROM imparare2_dataset_label pct_dia
            LEFT JOIN imparare2_dataset_sangue_categ hoje
                ON hoje.prontuario = pct_dia.registro
                	AND hoje.data_requisicao_exame = pct_dia.dia
                	AND hoje.id_enterprise = pct_dia.id_enterprise
            LEFT JOIN LATERAL (
                SELECT
                    MAX(s."LEUCO_ALTERADA")               AS leuco_alterada,
                    MAX(s."LEUCOCITOSE")                  AS leucocitose,
                    MAX(s."LEUCOPENIA")                   AS leucopenia,
                    MAX(s."RDW_ALTERADA")                 AS rdw_alterada,
                    MAX(s."NEUTROF_ALTERADO")             AS neutrof_alterado,
                    MAX(s."PCR_ALTERADA")                 AS pcr_alterada,
                    MAX(s."CLOSTRIDIUM_POSITIVO")         AS clostridium_positivo,
                    MAX(s."MRSA_POSITIVO")                AS mrsa_positivo,
                    MAX(s."VIRUS_RESPIRATORIO_POSITIVO")  AS virus_resp_positivo,
                    MAX(s."LIQUOR_ALTERA_GLICOSE")        AS liquor_glicose,
                    MAX(s."LIQUOR_ALTERA_PROTEINA")       AS liquor_proteina
                FROM imparare2_dataset_sangue_categ s
                WHERE s.prontuario = pct_dia.registro
                	AND s.data_requisicao_exame BETWEEN pct_dia.dia + 1 AND pct_dia.dia + 3
                	AND s.id_enterprise = pct_dia.id_enterprise
            ) futuro ON TRUE
            LEFT JOIN LATERAL (
                SELECT
                    MAX(s."LEUCO_ALTERADA")               AS leuco_alterada,
                    MAX(s."LEUCOCITOSE")                  AS leucocitose,
                    MAX(s."LEUCOPENIA")                   AS leucopenia,
                    MAX(s."RDW_ALTERADA")                 AS rdw_alterada,
                    MAX(s."NEUTROF_ALTERADO")             AS neutrof_alterado,
                    MAX(s."PCR_ALTERADA")                 AS pcr_alterada,
                    MAX(s."CLOSTRIDIUM_POSITIVO")         AS clostridium_positivo,
                    MAX(s."MRSA_POSITIVO")                AS mrsa_positivo,
                    MAX(s."VIRUS_RESPIRATORIO_POSITIVO")  AS virus_resp_positivo,
                    MAX(s."LIQUOR_ALTERA_GLICOSE")        AS liquor_glicose,
                    MAX(s."LIQUOR_ALTERA_PROTEINA")       AS liquor_proteina
                FROM imparare2_dataset_sangue_categ s
                WHERE s.prontuario = pct_dia.registro
                	AND s.data_requisicao_exame BETWEEN pct_dia.dia - 3 AND pct_dia.dia
                	AND s.id_enterprise = pct_dia.id_enterprise
        ) passado ON TRUE;
    """)

if __name__ == "__main__":
    main()