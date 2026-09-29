from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool
import pandas as pd

def worker(c:pd.DataFrame):
   
    #dá pra concatenar isso na criação da tabela e fazer cating como string? - testar
    c["tmp_start"] = c["dthr_procedimento"].astype(str)
    c["tmp_end"] = c["dthr_fim_procedimento"].astype(str)
    
    referencias = [["tmp_start", "tmp_end"]]
    separadores = [""]
    destino = ["chave_procedimento"]
    c = maestro.concatenate_columns(df=c, arrayDeReferencias=referencias, arraySeparadores=separadores, arrayDestinos=destino)

    novosNomes = {
        "record_id": "patient_id",
        "surgery_description": "nome_procedimento",
        "provider_id": "prestador",
        "provider_name": "nome_medico",
        "attendance_type": "tipo_atendimento"
    }
    c = maestro.rename_columns(df=c, DictColumns=novosNomes)

    c = maestro.difference_time_between_columns(
        df=c, 
        colunaInicio="dthr_procedimento", 
        colunaFim="dthr_fim_procedimento", 
        colunaDestino="tempo_de_cirurgia"
    )

    colunas_remover = ["tmp_start", "tmp_end"]
    c = maestro.remove_columns(df=c, arrayColumns=colunas_remover)
    
    colunas_nan = ["dthr_fim_procedimento", "tempo_de_cirurgia"]
    c = maestro.remove_nan(df=c, arrayColumns=colunas_nan)
    
    tuplas = [(" ", "")]
    c = maestro.replace_values_list(df=c, column="chave_procedimento", arrayDeTuplas=tuplas)

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_t1_cirurgias_1_3", if_exists= "append")

def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_t1_cirurgias_1_3;
            CREATE UNLOGGED TABLE imparare2_t1_cirurgias_1_3 (
                patient_id INTEGER,
                attendance_id INTEGER,
                tipo_atendimento TEXT,  
                surgery_notice_id INTEGER, 
                nome_procedimento TEXT, 
                dthr_procedimento TIMESTAMP, 
                dt_procedimento DATE ,
                dthr_fim_procedimento TIMESTAMP, 
                prestador INTEGER, 
                nome_medico TEXT,
                chave_procedimento TEXT,
                tempo_de_cirurgia FLOAT
            );    
        """   
        dataRequest.execute(create_query)                    
    
    append_query = f"""
       SELECT
            record_id::integer, 
            attendance_id::integer, 
            attendance_type::text, 
            surgery_notice_id::integer, 
            surgery_description::text, 
            DATE_TRUNC('minute', "surgery_start_date")::timestamp as dthr_procedimento, 
            surgery_start_date::date as "dt_procedimento",
            DATE_TRUNC('minute', "surgery_end_date")::timestamp as dthr_fim_procedimento, 
            provider_id::integer, 
            provider_name::text
        FROM surgeries_rgo_names_followup
        where record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
        GROUP BY record_id, attendance_id, surgery_notice_id, surgery_description, DATE_TRUNC('minute', "surgery_start_date"), DATE_TRUNC('minute', "surgery_end_date"), provider_id, provider_name, attendance_type, surgery_start_date::date;
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)

    with Pool(processes= 4) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()