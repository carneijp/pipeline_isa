from ImpararePackage import dataRequest
from ImpararePackage import maestro
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from multiprocessing import Pool, cpu_count


# TODO: Manter visao aqui para possiveis erros de janelas, periodo entre atendimento e alta que devem ter janelas criadas.
def worker(c:pd.DataFrame):
    df_filtered = c[c['dt_alta'].isna()]
    linesToDrop = []

    for index in df_filtered.index:
        df_paciente = c[c['registro'] == c.iloc[index]['registro']]
        possiveis_datas = df_paciente[df_paciente['dt_atendimento'] > c.iloc[index]['dt_atendimento']]
        if len(possiveis_datas) > 0:
            possiveis_datas.sort_values('dt_atendimento', ascending= True, inplace= True)
            day = possiveis_datas.iloc[0]['dt_atendimento']
            day = (day - relativedelta(days= 1))
            c.loc[index, 'dt_alta'] = day
        else:
            df_por_dia = df_paciente[df_paciente['dt_atendimento'].dt.day == c.iloc[index]['dt_atendimento'].day] 
            df_por_mes = df_por_dia[df_por_dia['dt_atendimento'].dt.month == c.iloc[index]['dt_atendimento'].month]
            df_por_ano = df_por_mes[df_por_mes['dt_atendimento'].dt.year == c.iloc[index]['dt_atendimento'].year]
            if len(df_por_ano) > 1:
                linesToDrop.append(index)
            else:
                today = datetime.now()
                today = (today - relativedelta(days= 1))
                day = datetime(year= today.year, month= today.month, day= today.day, hour= 23, minute= 59, second= 59)
                c.loc[index, 'dt_alta'] = day

    c.drop(index= linesToDrop, inplace= True)

    #c = maestro.parse_date(c, arrayColumns= ["dt_atendimento_parsed", "dt_alta_parsed"], yearfirst=True)

    dataRequest.set_data_on_sql(c, nomeTabelaDestino= "imparare2_internacoes_v2_stacked_by_cd_atendimento", if_exists= "append")
            
def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_internacoes_v2_stacked_by_cd_atendimento;
            CREATE UNLOGGED TABLE imparare2_internacoes_v2_stacked_by_cd_atendimento (
                registro INTEGER,
                cd_atendimento INTEGER,
                dt_atendimento TIMESTAMP,
                dt_alta TIMESTAMP,
                nmconvenio TEXT,
                "CODUNI||''||DESUNI" TEXT,
                "CODESP||''||DESESP" TEXT,
                tipo_clinica TEXT,
                tipo_intern TEXT,
                alta TEXT
            );
        """
        dataRequest.execute(create_query)

    append_query = f"""
        SELECT 
            record_id AS registro,
            attendance_id AS cd_atendimento,
            "dt_atendimento" AS "dt_atendimento",
            MAX("NMCONVENIO_dku_lst") AS "nmconvenio",
            MAX("CODUNI||''||DESUNI_dku_lst") AS "CODUNI||''||DESUNI",
            MAX("CODESP||''||DESESP_dku_lst") AS "CODESP||''||DESESP",
            MAX("TPCLINICA_dku_lst") AS tipo_clinica,
            MAX("TIPOINT_dku_lst") AS tipo_intern,
            COALESCE(MAX("dt_alta_dku_lst"), (NOW() - interval '1 day')::timestamp) AS "dt_alta",
            MAX("ALTA_dku_lst") AS alta
        FROM (
            SELECT DISTINCT 
                record_id, 
                attendance_id, 
                dt_atendimento, 
                dt_alta,
                LAST_VALUE("health_insurance_name") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "NMCONVENIO_dku_lst",
                LAST_VALUE("unity_code_and_description") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "CODUNI||''||DESUNI_dku_lst",
                LAST_VALUE("clinic_type") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "CODESP||''||DESESP_dku_lst",
                LAST_VALUE("clinic_type") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "TPCLINICA_dku_lst",
                LAST_VALUE("hospitalization_type") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "TIPOINT_dku_lst",
                LAST_VALUE("dt_alta") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "dt_alta_dku_lst",
                LAST_VALUE("hospital_discharge_description") OVER (PARTITION BY "record_id", "attendance_id", "dt_atendimento" ORDER BY "created_at" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "ALTA_dku_lst"
            FROM (SELECT *,
				       (attendance_date::date + attendance_hour::time) AS "dt_atendimento",
				       (hospital_discharge_date::date + hospital_discharge_hour::time) AS "dt_alta"
				FROM "hospitalization" a
				WHERE "company_code" IS NOT NULL
				  AND (record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
            ) "dku__subquery" 
        )
        GROUP BY "record_id", "attendance_id", "dt_atendimento";
        """
    
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()