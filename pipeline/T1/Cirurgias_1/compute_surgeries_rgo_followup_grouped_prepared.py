from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool
import pandas as pd

def worker(c:pd.DataFrame):
    novosNomes = {
        "record_id": "patient_id", 
        "editor_registry_value": "texto_cirurgia", 
        "attendance_type": "tipo_atendimento", 
        "provider_profile": "perfil", 
        "procedure_type": "tipo_procedimento", 
        "provider_name": "nome_medico", 
        "provider_id": "prestador", 
        "creation_date": "dthr_criacao", 
        "close_date": "dthr_fim"
    }
    c = maestro.rename_columns(df= c, DictColumns= novosNomes)

    colunas = ["editor_registry_id"]
    c = maestro.remove_columns(df= c, arrayColumns= colunas)

    c = maestro.remove_nan(df= c, column= "texto_cirurgia")

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_t1_cirurgias_2_4", if_exists= "append")

def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_t1_cirurgias_2_4;
            CREATE UNLOGGED TABLE imparare2_t1_cirurgias_2_4 (
                patient_id INTEGER,
                tipo_atendimento TEXT,
                attendance_id INTEGER,
                perfil TEXT,
                prestador TEXT,
                dthr_criacao TIMESTAMP,
                dt_criacao DATE,
                tipo_procedimento TEXT,
                dthr_fim TIMESTAMP,
                texto_cirurgia TEXT,
                nome_medico TEXT
            );
        """             
        dataRequest.execute(create_query)   

    append_query = f"""
        WITH cirurgias_2_1 AS (
            SELECT
                created_at::timestamp, 
                record_id::integer, 
                attendance_id::integer, 
                attendance_type::text, 
                provider_profile::text, 
                provider_name::text, 
                editor_registry_id::integer, 
                provider_id::integer, 
                creation_date::timestamp as creation_date, 
                editor_registry_value::text, 
                procedure_type::text,
                close_date::timestamp as close_date
            FROM surgeries_rgo_followup
            WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
        ), cirurgias_2_2 AS (
            SELECT DISTINCT ON(record_id, attendance_id, 
                            attendance_type, provider_profile, 
                            provider_name, editor_registry_id, provider_id, 
                            creation_date, close_date, procedure_type)
                    record_id,
                    attendance_id,
                    attendance_type,
                    provider_profile,
                    provider_name,
                    editor_registry_id,
                    provider_id,
                    creation_date,
                    close_date,
                    procedure_type,
                    created_at,
                    editor_registry_value
                FROM cirurgias_2_1
                WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
                ORDER BY record_id, 
                        attendance_id, 
                        attendance_type, 
                        provider_profile, 
                        provider_name, 
                        editor_registry_id, 
                        provider_id, 
                        creation_date, 
                        close_date, 
                        procedure_type DESC
        )
            SELECT DISTINCT 
                record_id,
                attendance_id,
                attendance_type,
                provider_profile,
                editor_registry_id,
                provider_id,
                creation_date,
                creation_date::date as dt_criacao,
                procedure_type,
                close_date,
                editor_registry_value,
                STRING_AGG(provider_name, ', ' order by created_at) AS provider_name
            FROM cirurgias_2_2
            WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
            GROUP BY record_id, 
                    attendance_id, 
                    attendance_type, 
                    provider_profile, 
                    editor_registry_id, 
                    provider_id, 
                    creation_date, 
                    creation_date::date ,
                    procedure_type, 
                    close_date, 
                    editor_registry_value;
    """
    
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)

    with Pool(processes=4) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()