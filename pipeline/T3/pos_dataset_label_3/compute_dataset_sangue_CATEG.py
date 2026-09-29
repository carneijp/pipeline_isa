from multiprocessing import Pool, cpu_count
from ImpararePackage import dataRequest
import pandas as pd

def worker(c: pd.DataFrame):
    colunas_exames = [
        'leuco_max', 'leuco_min', 'neuto_max', 'rdw_max', 'pcr_max', 
        'clostridium_pos', 'mrsa_pos', 'virus_resp_pos', 
        'glicose_liquor_min', 'proteina_liquor_max'
    ]
    for col in colunas_exames:
        if col in c.columns:
            c[col] = pd.to_numeric(c[col], errors='coerce')
    
    criterios = [
        'LEUCO_ALTERADA', 'LEUCOCITOSE', 'LEUCOPENIA',
        'RDW_ALTERADA', 
        'NEUTROF_ALTERADO',
        'PCR_ALTERADA', 
        'CLOSTRIDIUM_POSITIVO',
        'MRSA_POSITIVO',
        'VIRUS_RESPIRATORIO_POSITIVO',
        'LIQUOR_ALTERA_GLICOSE',
        'LIQUOR_ALTERA_PROTEINA'
    ]
    c[criterios] = 0
            
    def criterio(row):
        idade_meses = row['idade_meses']
        idade_dias = row['idade_dias']
        
        if idade_dias <= 1:
            row['LEUCO_ALTERADA'] = 1 if (row['leuco_max'] >= 30000) | (row['leuco_min'] <= 5000) else 0 
            row['LEUCOCITOSE'] = 1 if (row['leuco_max'] >= 30000) else 0 
            row['LEUCOPENIA'] = 1 if (row['leuco_min'] <= 5000) else 0
            row['NEUTROF_ALTERADO'] = 1 if (row['neuto_max'] > 10000) else 0
            row['RDW_ALTERADA'] = 1 if (row['rdw_max'] > 20) else 0
            row['PCR_ALTERADA'] = 1 if (row['pcr_max'] > 10) else 0
            row['CLOSTRIDIUM_POSITIVO'] = 1 if (row['clostridium_pos'] > 0) else 0
            row['MRSA_POSITIVO'] = 1 if (row['mrsa_pos'] > 0) else 0
            row['VIRUS_RESPIRATORIO_POSITIVO'] = 1 if (row['virus_resp_pos'] > 0) else 0
            row['LIQUOR_ALTERA_GLICOSE'] = 1 if (row['glicose_liquor_min'] < 40) | (row['glicose_liquor_min'] < 70) else 0 
            row['LIQUOR_ALTERA_PROTEINA'] = 1 if (row['proteina_liquor_max'] < 12) | (row['proteina_liquor_max'] < 60) else 0 

        if idade_dias >= 2 and idade_dias < 4:
            row['LEUCO_ALTERADA'] = 1 if (row['leuco_max'] >= 21000) | (row['leuco_min'] <= 5000) else 0 
            row['LEUCOCITOSE'] = 1 if (row['leuco_max'] >= 21000) else 0 
            row['LEUCOPENIA'] = 1 if (row['leuco_min'] <= 5000) else 0
            row['NEUTROF_ALTERADO'] = 1 if (row['neuto_max'] > 9000) else 0
            row['RDW_ALTERADA'] = 1 if (row['rdw_max'] > 20) else 0
            row['PCR_ALTERADA'] = 1 if (row['pcr_max'] > 10) else 0
            row['CLOSTRIDIUM_POSITIVO'] = 1 if (row['clostridium_pos'] > 0) else 0
            row['MRSA_POSITIVO'] = 1 if (row['mrsa_pos'] > 0) else 0
            row['VIRUS_RESPIRATORIO_POSITIVO'] = 1 if (row['virus_resp_pos'] > 0) else 0
            row['LIQUOR_ALTERA_GLICOSE'] = 1 if (row['glicose_liquor_min'] < 40) | (row['glicose_liquor_min'] < 70) else 0 
            row['LIQUOR_ALTERA_PROTEINA'] = 1 if (row['proteina_liquor_max'] < 12) | (row['proteina_liquor_max'] < 60) else 0 

        if idade_dias >= 4 and idade_dias < 30:
            row['LEUCO_ALTERADA'] = 1 if (row['leuco_max'] >= 21000) | (row['leuco_min'] <= 5000) else 0 
            row['LEUCOCITOSE'] = 1 if (row['leuco_max'] >= 21000) else 0 
            row['LEUCOPENIA'] = 1 if (row['leuco_min'] <= 5000) else 0 
            row['NEUTROF_ALTERADO'] = 1 if (row['neuto_max'] > 6000) else 0
            row['RDW_ALTERADA'] = 1 if (row['rdw_max'] > 20) else 0
            row['PCR_ALTERADA'] = 1 if (row['pcr_max'] > 10) else 0
            row['CLOSTRIDIUM_POSITIVO'] = 1 if (row['clostridium_pos'] > 0) else 0
            row['MRSA_POSITIVO'] = 1 if (row['mrsa_pos'] > 0) else 0
            row['VIRUS_RESPIRATORIO_POSITIVO'] = 1 if (row['virus_resp_pos'] > 0) else 0
            row['LIQUOR_ALTERA_GLICOSE'] = 1 if (row['glicose_liquor_min'] < 40) | (row['glicose_liquor_min'] < 70) else 0 
            row['LIQUOR_ALTERA_PROTEINA'] = 1 if (row['proteina_liquor_max'] < 12) | (row['proteina_liquor_max'] < 60) else 0 

        if idade_meses >= 1:
            row['LEUCO_ALTERADA'] = 1 if (row['leuco_max'] >= 15000) | (row['leuco_min'] <= 5000) else 0 
            row['LEUCOCITOSE'] = 1 if (row['leuco_max'] >= 15000) else 0 
            row['LEUCOPENIA'] = 1 if (row['leuco_min'] <= 5000) else 0 
            row['NEUTROF_ALTERADO'] = 1 if (row['neuto_max'] > 6000) else 0
            row['RDW_ALTERADA'] = 1 if (row['rdw_max'] > 20) else 0
            row['PCR_ALTERADA'] = 1 if (row['pcr_max'] > 10) else 0
            row['CLOSTRIDIUM_POSITIVO'] = 1 if (row['clostridium_pos'] > 0) else 0
            row['MRSA_POSITIVO'] = 1 if (row['mrsa_pos'] > 0) else 0
            row['VIRUS_RESPIRATORIO_POSITIVO'] = 1 if (row['virus_resp_pos'] > 0) else 0
            row['LIQUOR_ALTERA_GLICOSE'] = 1 if (row['glicose_liquor_min'] < 40) | (row['glicose_liquor_min'] < 70) else 0 
            row['LIQUOR_ALTERA_PROTEINA'] = 1 if (row['proteina_liquor_max'] < 12) | (row['proteina_liquor_max'] < 60) else 0 
            
        return row
    
    c = c.apply(criterio, axis= 1)

    colunas_DROP = [
        'clostridium_pos', 
        'mrsa_pos', 
        'virus_resp_pos', 
        'glicose_liquor_min', 
        'proteina_liquor_max'
    ]

    c.drop(columns=colunas_DROP, inplace= True)

    dicionario = {
        "registro": "prontuario"
    }
    c = c.rename(columns= dicionario)

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_dataset_sangue_categ", if_exists= "append")

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_dataset_sangue_categ;

            CREATE UNLOGGED TABLE imparare2_dataset_sangue_categ (
                prontuario INTEGER,
                data_requisicao_exame DATE,
                leuco_min FLOAT,
                leuco_max FLOAT,
                leuco_avg FLOAT,
                rdw_min FLOAT,
                rdw_max FLOAT,
                rdw_avg FLOAT,
                neuto_min FLOAT,
                neuto_max FLOAT,
                neuto_avg FLOAT,
                pcr_min FLOAT,
                pcr_max FLOAT,
                pcr_avg FLOAT,
                idade_dias INTEGER,
                idade_meses FLOAT,
                "LEUCO_ALTERADA" INTEGER, 
                "LEUCOCITOSE" INTEGER, 
                "LEUCOPENIA" INTEGER, 
                "RDW_ALTERADA" INTEGER, 
                "NEUTROF_ALTERADO" INTEGER,
                "PCR_ALTERADA" INTEGER,
                "CLOSTRIDIUM_POSITIVO" INTEGER,
                "MRSA_POSITIVO" INTEGER,
                "VIRUS_RESPIRATORIO_POSITIVO" INTEGER,
                "LIQUOR_ALTERA_GLICOSE" INTEGER,
                "LIQUOR_ALTERA_PROTEINA" INTEGER
            );
        """
        dataRequest.execute(create_query)

    append_query = """
        select 
            *
        from (
            select 
                de.*,
                (de.data_requisicao_exame - pr.birthdate) as idade_dias,
                ((de.data_requisicao_exame - pr.birthdate) / 30.44)::smallint as idade_meses
            from imparare2_dataset_sangue de
            INNER join (
                select distinct record_id, birthdate from patients_records
            ) pr
                on de.registro = pr.record_id
        ) a
        where a.idade_dias >= 0
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes = cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()