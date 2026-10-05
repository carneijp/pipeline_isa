from ImpararePackage import dataRequest

def main():

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_prescricoesantibiotico_by_prontuario"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_prescricoesantibiotico_by_prontuario" AS
        SELECT 
            registro AS prontuario,
            dthr_prescricao AS dthr_prescricao,
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
        FROM imparare2_prescricoesantibiotico_prepared_teste
        GROUP BY registro, dthr_prescricao;
    """)

if __name__ == "__main__":
    main()