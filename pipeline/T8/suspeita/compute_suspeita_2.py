from ImpararePackage import dataRequest, maestro

def main():
    if maestro.get_must_update_all_patients() == "1":
        create_query = """
            DROP TABLE IF EXISTS isa_suspeita;
            CREATE UNLOGGED TABLE isa_suspeita (
                id TEXT, 
                paciente_id INTEGER, 
                cd_atendimento INTEGER, 
                dthr_alta TIMESTAMP, 
                dt_infeccao TIMESTAMP,
                prob_perc FLOAT4, 
                max_prob FLOAT4, 
                criterio TEXT, 
                dthr_internacao TIMESTAMP, 
                company_code TEXT,
                company_id TEXT
            );
            """
        dataRequest.execute(create_query, isLocal= True)
        dataRequest.execute(create_query, isLocal= False)
    else:
        # Drop local table
        dataRequest.execute("DELETE FROM isa_suspeita WHERE paciente_id in (select distinct record_id from patients_to_update)", isLocal= True)
        
        #Busca IDS para deleção
        df = dataRequest.get_data(queryText= f"SELECT distinct record_id::text FROM patients_to_update", chunck= None)
        pcts_ids = df['record_id'].tolist()

        ids = "(" + ",".join(pcts_ids) + ")"
        dataRequest.execute(f"DELETE FROM isa_suspeita WHERE paciente_id in {ids}", isLocal= False)


    append_query = """
        SELECT DISTINCT
            s.id, 
            s.paciente_id, 
            s.cd_atendimento, 
            s.dthr_alta, 
            s.dt_infeccao,
            s.prob_perc, 
            s.max_prob, 
            s.criterio, 
            s.dthr_internacao,
            c.company_code,
            c.hospital_id as company_id
        FROM "isa_suspeita_v2_prepared" as s 
        LEFT JOIN imparare2_company_code c 
            ON s.paciente_id = c.record_id
            AND s.dt_infeccao between c.attendance_date 
            AND coalesce(c.hospital_discharge_date, (
                SELECT min(c2.attendance_date)
                FROM imparare2_company_code c2
                WHERE c2.record_id = c.record_id AND c2.attendance_id > c.attendance_id
                GROUP BY c2.record_id 
            ), now())
            AND c.company_code IS NOT null        
    """

    pos = 0
    df = dataRequest.get_data(queryText= append_query)
    for c in df:
        # Salvando no local
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "isa_suspeita", isLocal= True, if_exists= "append")
        # Salvando no remoto
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "isa_suspeita", isLocal= False, if_exists= "append")
        pos += 1

if __name__ == "__main__":
    main()