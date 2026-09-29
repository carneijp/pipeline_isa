from ImpararePackage import dataRequest
from ImpararePackage import maestro

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS isa_suspeita_v2_prepared;
            CREATE UNLOGGED TABLE isa_suspeita_v2_prepared (
                id TEXT,
                paciente_id INTEGER,
                cd_atendimento INTEGER,
                dthr_internacao TIMESTAMP,
                dthr_alta TIMESTAMP,
                dt_infeccao DATE,
                prob_perc FLOAT4,
                max_prob FLOAT4,
                criterio TEXT
            );
            """
        dataRequest.execute(create_query)

    append_query = """
        SELECT 
            md5("paciente_id"::text || "cd_atendimento"::text || dt_infeccao::text) as id, 
            "paciente_id", 
            "cd_atendimento", 
            "dthr_internacao", 
            "dthr_alta", 
            "dt_infeccao", 
            "prob_perc", 
            "max_prob", 
            "notificado"
        FROM "imparare2_isa_suspeita_v2"
    """

    df = dataRequest.get_data(queryText= append_query)
    pos = 0
    for c in df:

        novosNomes = {
            "cd_atendimento": "cd_atendimento",
            "notificado": "criterio"
        }
        c = maestro.rename_columns(df= c, DictColumns= novosNomes)

        c = maestro.remove_columns(df= c, column= "dthr_internacao")

        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "isa_suspeita_v2_prepared", if_exists= "append")
        pos += 1

if __name__ == "__main__":
    main()