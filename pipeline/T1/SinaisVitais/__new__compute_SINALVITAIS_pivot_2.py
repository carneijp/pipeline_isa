from ImpararePackage import dataRequest, maestro
from multiprocessing import Pool, cpu_count
import pandas as pd


def worker(c: pd.DataFrame):
       
    perfil_translator = {
        "ENFERMEIRO(A)" : "ENFERMEIRO_A_",
        "TECNICO(A) EM ENFERMAGEM" : "TECNICO_A_EM_ENFERMAGEM",
    }
    c["perfil"] = c["perfil"].map(perfil_translator).fillna("OUTROS")

    desejos = ["ENFERMEIRO_A_", "TECNICO_A_EM_ENFERMAGEM", "OUTROS"]
    perfil_categorico = c["perfil"].astype(pd.CategoricalDtype(categories=desejos))
    dummies = pd.get_dummies(perfil_categorico, prefix="perfil").astype(int)
    c = pd.concat([c, dummies], axis=1)

    vital_sinal_translator = {
        # novos e duvidosos
        "PEEP" : "PEEP",
        "GLICEMIA CAPILAR" : "HGT",
        "HGT": "HGT",
        "ECG (GLASGOW)" : "GLASGOW",
        "GLASGOW" : "GLASGOW",

        # Ja existentes e duvidos
        "FIO2 %" : "FIO2",
        "FIO2" : "FIO2",
        "OXIGÊNIO (L/MIN)" : "O2",
        "O2" : "O2",

        # Ja existentes
        "FC" : "FC",
        "PEWS FC ACORDADO" : "FC",
        "PEWS FC DORMINDO" : "FC",

        "OXIMETRIA" : "OXIMETRIA",
        "ST" : "OXIMETRIA",
        "SAT.O2 %" : "OXIMETRIA",
        "SAT (M2BR)" : "OXIMETRIA",

        "TPM (M2BR)" : "TEMP",
        "TEMP" : "TEMP",

        "FRQR (M2BR)" : "FR",
        "FR" : "FR",

        "PAS" : "PAS",
        "PAS (M2BR)" : "PAS",

        "PAM" : "PAM",
        "P.A.M" : "PAM",
        "#P.A.M" : "PAM",
        
        "P.A. DIASTOLICA" : "PAD",
    }
    c["tipo_registro"] = c["tipo_registro"].map(vital_sinal_translator).fillna("drop")

    # Removendo outliers
    c = c[(c['tipo_registro'] != 'TEMP') | ((c['tipo_registro'] == 'TEMP') & (c['valor_medida'] > 24.0) & (c['valor_medida'] < 45.0))]
    c = c[(c['tipo_registro'] != 'FC') | ((c['tipo_registro'] == 'FC') & (c['valor_medida'] > 24) & (c['valor_medida'] < 350))]
    c = c[(c['tipo_registro'] != 'FR') | ((c['tipo_registro'] == 'FR') & (c['valor_medida'] > 4) & (c['valor_medida'] < 80))]
    c = c[(c['tipo_registro'] != 'OXIMETRIA') | ((c['tipo_registro'] == 'OXIMETRIA') & (c['valor_medida'] > 80) & (c['valor_medida'] < 100))]

    desejos = ["FC", "FR", "HGT", "PAS", "PAD", "TEMP", "OXIMETRIA", "O2", "FIO2", "PEEP"] 
    c = maestro.pivot_column_vectorized(df= c, columnLabels="tipo_registro", columnValues="valor_medida", arrayDeDesejos=desejos)

    # round values to determine them as INT or FLOAT
    colunas = ["FC", "FR", "HGT", 'PAS', "PAD", "OXIMETRIA", 
        "perfil_ENFERMEIRO_A_", "perfil_TECNICO_A_EM_ENFERMAGEM", "perfil_OUTROS"]
    c = maestro.to_int(df= c, arrayColumns= colunas, errors = 'ignore')
    
    colunas = ["registro", "dia", 
        "FC", "FR", "HGT", "PAS", "PAD", "TEMP", "OXIMETRIA", "O2", "FIO2", "PEEP",
        "perfil_ENFERMEIRO_A_", "perfil_TECNICO_A_EM_ENFERMAGEM", "perfil_OUTROS"]
    c = maestro.keep_columns(df= c, arrayColumns= colunas)
    
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_sinalvitais_pivot", if_exists= "append")

def main():
    replace =  True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_sinalvitais_pivot;
            CREATE UNLOGGED TABLE imparare2_sinalvitais_pivot (
                registro INTEGER,
                dia DATE,
                "FC" SMALLINT,
                "FR" SMALLINT,
                "HGT" FLOAT,
                "PAD" SMALLINT,
                "PAS" SMALLINT,
                "TEMP" FLOAT,
                "OXIMETRIA" SMALLINT,
                "O2" FLOAT,
                "FIO2" FLOAT,
                "PEEP" FLOAT,
                "perfil_ENFERMEIRO_A_" SMALLINT,
                "perfil_TECNICO_A_EM_ENFERMAGEM" SMALLINT,
                "perfil_OUTROS" SMALLINT
            );
        """
        dataRequest.execute(create_query)
    
    append_query = f"""
        SELECT
            record_id AS registro,
            acronym AS tipo_registro,
            collection_date::date AS dia,
            value::FLOAT AS valor_medida,
            measurement_unity AS uni_medida,
            provider_profile AS perfil
        FROM vital_signs
        where record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes=4) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()
