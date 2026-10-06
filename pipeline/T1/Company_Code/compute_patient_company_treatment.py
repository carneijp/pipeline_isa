from ImpararePackage import maestro
from ImpararePackage import dataRequest

def main():
    query = """
        DROP TABLE IF EXISTS imparare_patient_company_treatment;

        CREATE UNLOGGED TABLE imparare_patient_company_treatment AS (
            SELECT DISTINCT ON (c.record_id, c.id_enterprise, c.attendance_id)
                c.record_id,
                c.attendance_id,
                c.attendance_date,
                coalesce(c.hospital_discharge_date, (
                    SELECT min(c2.attendance_date)
                    FROM imparare2_company_code c2
                    WHERE c2.record_id = c.record_id 
                        AND c2.attendance_id > c.attendance_id
                    GROUP BY c2.record_id 
                ), now())::date as discharge_date,
                c.id_hospital,
                c.id_enterprise
            FROM imparare2_company_code c
        );

        CREATE INDEX idx_imparare_patient_company_treatment ON imparare_patient_company_treatment (id_enterprise, record_id, id_hospital, attendance_date, discharge_date);
    """
    dataRequest.execute(queryText= query)

if __name__ == "__main__":
    main()