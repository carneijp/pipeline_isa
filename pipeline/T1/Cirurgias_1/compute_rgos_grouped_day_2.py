from ImpararePackage import dataRequest
from ImpararePackage import maestro

def main():

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_t1_cirurgias_4_6"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE imparare2_t1_cirurgias_4_6 AS
            SELECT RGO.patient_id
                , RGO.dt_criacao as data
                , string_agg(RGO.texto_cirurgia,' | ' order by RGO.dthr_criacao) AS laudos_dia,
                RGO.id_enterprise
            FROM imparare2_t1_cirurgias_4_5 RGO
            -- Question: é mesmo necessário filtrar somente os atendimentos do tipo I (internação)? Pois, se sim, então o campo "tipo_atendimento" não é necessário na tabela final.
            WHERE RGO.tipo_atendimento = 'I'
            GROUP BY RGO.patient_id, RGO.id_enterprise, RGO.dt_criacao;
        """)

    dataRequest.execute("DROP TABLE IF EXISTS imparare2_t1_cirurgias_4_5;")

if __name__ == "__main__":
    main()