from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c: pd.DataFrame):
    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_wellhead_hml_prescriptions_followup_prepared", if_exists= "append")


def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_wellhead_hml_prescriptions_followup_prepared;
            CREATE UNLOGGED TABLE imparare2_wellhead_hml_prescriptions_followup_prepared (
                registro INTEGER,
                cd_pre_med INTEGER,
                dthr_prescricao TIMESTAMP,
                atb TEXT,
                dose TEXT,
                unidade TEXT,
                frequencia TEXT,
                via TEXT,
                attendance_type TEXT
            );
        """
        dataRequest.execute(create_query)

    append_query = f"""
        SELECT 
            record_id as registro, 
            pre_med_id as cd_pre_med, 
            prescription_date as dthr_prescricao, 
            antibiotic as atb, 
            dosage as dose, 
            antibiotic_unity as unidade, 
            frequency as frequencia, 
            via as via, 
            "attendanceType" AS attendance_type
        FROM prescriptions_followup
        WHERE record_id IN (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()}
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck=2000)
    with Pool(processes = cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()