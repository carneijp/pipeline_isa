from ImpararePackage import dataRequest

def main():
    print("Executando compute_patients_to_update.py")
    dataRequest.execute("""
        CREATE TABLE IF NOT EXISTS pipeline_execution_log(
            id SERIAL PRIMARY KEY,
            execution_date DATE NOT NULL DEFAULT CURRENT_DATE
        );
        DROP TABLE IF EXISTS patients_to_update;
        CREATE TABLE patients_to_update AS (
            SELECT 
                DISTINCT record_id 
            FROM (
                SELECT 
                    DISTINCT record_id 
                FROM evolutions 
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM evolutions_followup
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM exam_followup_reports
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM exams_reports
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM hospitalization
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM patients_records
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM prescriptions
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM prescriptions_followup
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM surgeries_rgo
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM surgeries_rgo_followup
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM surgeries_rgo_names
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM surgeries_rgo_names_followup
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM vital_signs
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM vital_signs_followup
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM xray_followup_report
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
                UNION ALL
                SELECT 
                    DISTINCT record_id 
                FROM xrays_reports
                WHERE created_at > coalesce(
                    (SELECT execution_date FROM pipeline_execution_log pel ORDER BY id DESC LIMIT 1),
                    DATE('2022-01-01')
                ) - interval '1 day'
            ) a
        );

        CREATE INDEX idx_patients_to_update on patients_to_update(record_id);
    """)

if __name__ == "__main__":
    main()