from ImpararePackage import maestro
from ImpararePackage import dataRequest

def main():
    query = """
        drop table if exists imparare_patient_company_treatment;
        CREATE UNLOGGED TABLE imparare_patient_company_treatment as (
            select
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
                c.company_code,
                c.hospital_id
            from imparare2_company_code c
        );
    """
    dataRequest.execute(queryText= query)

    query = """
        create index idx_imparare_patient_company_treatment on imparare_patient_company_treatment (record_id, attendance_date, discharge_date, company_code);
    """
    dataRequest.execute(queryText= query)

if __name__ == "__main__":
    main()