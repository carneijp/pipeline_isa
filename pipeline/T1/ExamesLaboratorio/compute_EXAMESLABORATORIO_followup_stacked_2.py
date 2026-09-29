from ImpararePackage import dataRequest, maestro

def main():
    dataRequest.execute(f"""
        SET synchronous_commit = off;
        DROP TABLE IF EXISTS imparare2_exameslaboratorio_followup_stacked;
        CREATE UNLOGGED TABLE imparare2_exameslaboratorio_followup_stacked AS
        select DISTINCT * from (
            SELECT DISTINCT
                record_id AS registro,
                exam_lab_name AS exame,
                exam_lab_id AS cd_exa_lab,
                laboratory_request_date AS dthr_pedido,
                laboratory_request_delivery_date AS dthr_entrega,
                exam_result_field_name AS item_exame,
                exam_result_description AS ds_resultado,
                NULL::text as ordem_amostra,
                NULL::timestamp as signature_date,
                'I' as tipo_atendimento
            FROM exams_reports
            WHERE (record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
                AND exam_result_description IS NOT NULL
            UNION
            SELECT  
                registro, 
                exame,
                cd_exa_lab,
                dthr_pedido,
                dthr_entrega, 
                item_exame, 
                ds_resultado,            
                ordem_amostra::text,
                signature_date,
                tipo_atendimento
            FROM imparare2_wellhead_hml_blood_culture_prepared p
            UNION
            SELECT 
                record_id AS registro,
                exam_lab_name AS exame,
                exam_lab_id AS cd_exa_lab,
                laboratory_request_date AS dthr_pedido,
                laboratory_request_delivery_date AS dthr_entrega,
                exam_result_field_name AS item_exame,
                exam_result_description AS ds_resultado,
                NULL::text as ordem_amostra,
                NULL::timestamp as signature_date,
                attendance_type AS tipo_atendimento
            FROM exam_followup_reports
            WHERE (record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
        ) a;
    """)

if __name__ == "__main__":
    main()