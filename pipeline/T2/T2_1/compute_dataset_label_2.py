from ImpararePackage import maestro
from ImpararePackage import dataRequest
from multiprocessing import Pool, cpu_count
import pandas as pd
import numpy

def worker(c = pd.DataFrame):
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_dataset_label", if_exists=  "append")

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_dataset_label;
            CREATE UNLOGGED TABLE imparare2_dataset_label (
                registro INTEGER,
                dia DATE,
                sexo TEXT,
                idade_anos FLOAT,
                idade_dias FLOAT,
                unidade_internacao TEXT,
                especialidade_internacao TEXT,
                tipo_internacao TEXT,
                clinica_internacao TEXT,
                dthr_internacao date,
                dthr_alta date, 
                alta TEXT,
                los_dias SMALLINT,
                count SMALLINT
            );
        """
        dataRequest.execute(create_query)

    append_query = """
        SELECT 
            d.registro, 
            d.dia,
            MAX(d.sexo) sexo,
            MAX(idade_anos) idade_anos,
            MAX(idade_dias) idade_dias,
            MIN(unidade) unidade_internacao,
            MIN(especialidade) especialidade_internacao,
            MIN(tipo_intern) tipo_internacao,
            MIN(tipo_clinica) clinica_internacao,
            MIN(dthr_atendimento) dthr_internacao,
            MAX(dthr_alta) dthr_alta,
            COALESCE(d.dia-min(dthr_atendimento)::date, 0) as los_dias,
            count(*) 
        FROM imparare2_paciente_dia_internacao_with_label_nova as d
        GROUP BY d.registro, d.dia
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)

    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()