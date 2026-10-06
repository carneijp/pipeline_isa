from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""
        SET synchronous_commit = off;
        DROP TABLE IF EXISTS imparare2_prescricoesantibiotico_by_prontuario;

        CREATE UNLOGGED TABLE imparare2_prescricoesantibiotico_by_prontuario AS
            SELECT 
                registro AS prontuario,
                date(dthr_prescricao) AS dthr_prescricao,
                id_enterprise::SMALLINT AS id_enterprise,
                SUM("atb_COMUNITARIO") AS "ATB_COMUNITARIO_count",
                SUM("atb_TOPICO") AS "ATB_TOPICO_count",
                SUM("atb_INTERMEDIARIO") AS "ATB_INTERMEDIARIO_count",
                SUM("atb_HOSPITALAR") AS "ATB_HOSPITALAR_count",
                SUM("atb_MMR") AS "ATB_MMR_count",
                SUM("atb_ANTIFUNGICO") AS "ATB_ANTIFUNGICO_count",
                SUM("atb_OUTROS") AS "ATB_OUTROS_count",
                SUM("atb_PROFILATICO") AS "ATB_PROFILATICO_count",
                MAX(atb_importancia) AS atb_categ,
                MAX(via_importancia) AS via_categ
            FROM imparare2_prescricoesantibiotico_prepared
            GROUP BY registro, date(dthr_prescricao), id_enterprise;

        CREATE INDEX IF NOT EXISTS imparare2_prescricoesantibiotico_by_prontuario_idx_1 ON imparare2_prescricoesantibiotico_by_prontuario(id_enterprise, prontuario, dthr_prescricao);
    """)

if __name__ == "__main__":
    main()