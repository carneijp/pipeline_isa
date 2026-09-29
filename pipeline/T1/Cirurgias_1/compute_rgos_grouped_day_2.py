from ImpararePackage import dataRequest
from ImpararePackage import maestro

def main():

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_t1_cirurgias_4_6"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_t1_cirurgias_4_6" AS
            SELECT RGO."patient_id"
                , RGO."dt_criacao" as "data"
                , string_agg(RGO."texto_cirurgia",' | ' order by RGO."dthr_criacao") AS "laudos_dia"
            FROM "imparare2_t1_cirurgias_4_5" RGO
                WHERE RGO."tipo_atendimento" = 'I'
            GROUP BY RGO."patient_id", RGO."dt_criacao";
        """)

    dataRequest.execute("DROP TABLE IF EXISTS imparare2_t1_cirurgias_4_5;")

if __name__ == "__main__":
    main()