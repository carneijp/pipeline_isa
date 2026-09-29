from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_cirurgias_grouped_day_joined"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_cirurgias_grouped_day_joined" AS
            SELECT DISTINCT 
                "cirurgias_nome_grouped_day"."patient_id" AS "REGISTRO",
                "cirurgias_nome_grouped_day"."data" AS "DATA",
                "cirurgias_nome_grouped_day"."tempo_cirurgia_dia" AS "tempo_cirurgia_dia",
                "cirurgias_nome_grouped_day"."count_procedimentos_dia" AS "count_procedimentos_dia",
                "rgos_grouped_day"."laudos_dia" AS "laudos_dia"
            FROM "imparare2_t1_cirurgias_3_4" "cirurgias_nome_grouped_day"
            INNER JOIN "imparare2_t1_cirurgias_4_6" "rgos_grouped_day"
                ON ("cirurgias_nome_grouped_day"."patient_id" = "rgos_grouped_day"."patient_id")
                AND (extract ('day' from "cirurgias_nome_grouped_day"."data") = extract ('day' from "rgos_grouped_day"."data") and extract ('month' from "cirurgias_nome_grouped_day"."data") = extract ('month' from "rgos_grouped_day"."data") and extract ('year' from "cirurgias_nome_grouped_day"."data") = extract ('year' from "rgos_grouped_day"."data"))    
        """)

    # dataRequest.execute("DROP TABLE IF EXISTS sample_imparare2_t1_cirurgias_3_4;")
    # dataRequest.execute("CREATE UNLOGGED TABLE sample_imparare2_t1_cirurgias_3_4 as ( SELECT * FROM imparare2_t1_cirurgias_3_4 LIMIT 5000);")
    # dataRequest.execute("DROP TABLE IF EXISTS imparare2_t1_cirurgias_3_4;")

    # dataRequest.execute("DROP TABLE IF EXISTS sample_imparare2_t1_cirurgias_4_6;")
    # dataRequest.execute("CREATE UNLOGGED TABLE sample_imparare2_t1_cirurgias_4_6 as ( SELECT * FROM imparare2_t1_cirurgias_4_6 LIMIT 5000);")
    # dataRequest.execute("DROP TABLE IF EXISTS imparare2_t1_cirurgias_4_6;")

if __name__ == "__main__":
    main()