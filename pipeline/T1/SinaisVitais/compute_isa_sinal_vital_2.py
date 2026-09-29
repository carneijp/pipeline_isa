from ImpararePackage import dataRequest, maestro

def main():
    dataRequest.execute(f"""
        SET synchronous_commit = off;

        DROP TABLE IF EXISTS imparare2_isa_sinal_vital;

        CREATE UNLOGGED TABLE imparare2_isa_sinal_vital AS (
            SELECT DISTINCT 
                (record_id::varchar || collection_date::varchar || acronym::varchar || measurement_unity::varchar || provider_profile::varchar || attendance_type::varchar) as id, 
                record_id AS registro,
                acronym AS tipo_registro,
                collection_date AS dthr_coleta,
                value AS valor_medida,
                measurement_unity AS uni_medida,
                provider_profile AS perfil,
                attendance_type AS tipo_atendimento,
                null as ordem,
                null as criterio
            FROM vital_signs
            where value IS NOT NULL
                AND acronym IS NOT NULL
                AND (record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
            UNION ALL
            SELECT DISTINCT 
                (record_id::varchar || collection_date::varchar || acronym::varchar || measurement_unity::varchar || provider_profile::varchar || attendance_type::varchar) as id, 
                record_id AS registro,
                acronym AS tipo_registro,
                collection_date AS dthr_coleta,
                value AS valor_medida,
                measurement_unity AS uni_medida,
                provider_profile AS perfil,
                attendance_type AS tipo_atendimento,
                null as ordem,
                null as criterio
            FROM vital_signs_followup
            where value IS NOT NULL
                AND acronym IS NOT NULL
                AND (record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
        );
    """)
    

if __name__ == "__main__":
    main()