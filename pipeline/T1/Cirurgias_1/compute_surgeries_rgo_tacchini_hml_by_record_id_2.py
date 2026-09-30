from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool
import pandas as pd

def worker(c:pd.DataFrame):
    
    novosNomes = {
            "record_id": "patient_id",
            "surgery_description": "texto_cirurgia",
            "attendance_type": "tipo_atendimento",
            "attendance_id": "id_atendimento",
            #"provider_profile": "perfil",
            #"procedure_type": "tipo_procedimento",
            "provider_name": "nome_medico",
            #"provider_id": "prestador",
    }
    c = maestro.rename_columns(df= c, DictColumns= novosNomes)

    colunas = ["count", "editor_registry_id","attendance_id"]
    c = maestro.remove_columns(df= c, arrayColumns= colunas)

    c = maestro.remove_nan(df= c, column= "texto_cirurgia")

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_t1_cirurgias_4_4", if_exists= "append")

def main():
    replace= True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_t1_cirurgias_4_4;
            CREATE UNLOGGED TABLE imparare2_t1_cirurgias_4_4 (
                patient_id INTEGER,
                texto_cirurgia TEXT,
                tipo_atendimento TEXT,
                id_atendimento INTEGER,
                -- perfil TEXT,
                -- tipo_procedimento TEXT,
                nome_medico TEXT,
                -- prestador TEXT,
                dthr_criacao TIMESTAMP,
                dt_criacao DATE,
                dthr_fim TIMESTAMP,
                id_enterprise INTEGER
            );
        """             
        dataRequest.execute(create_query)

    append_query = f"""
        WITH cirurgias_4_1 AS (
            SELECT 
                created_at, 
                record_id, 
                attendance_id, 
                attendance_type, 
                -- provider_profile, 
                provider_name, 
                -- editor_registry_id, 
                -- provider_id, 
                DATE_TRUNC('minute', creation_date)::timestamp as creation_date, 
                -- editor_registry_value, 
                -- procedure_type, 
                DATE_TRUNC('minute', close_date)::timestamp as close_date,
                surgery_description,
                h.id_enterprise
            FROM surgeries_rgo
            JOIN hospitals h ON surgeries_rgo.id_hospital = h.id_hospital
            --WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
        ), cirurgias_4_2 AS (
            SELECT DISTINCT ON(record_id, id_enterprise, attendance_id, attendance_type, provider_name, creation_date, close_date)
                record_id,
                attendance_id,
                attendance_type,
                provider_name,
                creation_date,
                close_date,
                created_at,
                surgery_description,
                id_enterprise
            FROM cirurgias_4_1
            -- WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
            ORDER BY record_id, id_enterprise,attendance_id, attendance_type, provider_name, creation_date, close_date, created_at DESC
        )
        SELECT 
            record_id,
            attendance_id,
            attendance_type,
            -- provider_profile,
            -- editor_registry_id,
            -- provider_id,
            creation_date as dthr_criacao,
            creation_date:: date as dt_criacao,
            -- procedure_type,
            close_date as dthr_fim,
            -- editor_registry_value,
            STRING_AGG(provider_name, ', ' order by created_at) AS provider_name,
            surgery_description,
            id_enterprise,
            COUNT(*) AS count
        FROM cirurgias_4_2
        -- WHERE record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
        GROUP BY record_id, id_enterprise, attendance_id, attendance_type, creation_date, close_date, surgery_description;
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes=4) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()