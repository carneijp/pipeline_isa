from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_dataset_sangue"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        create unlogged table imparare2_dataset_sangue as
            select 
                s.registro, 
                s.laboratory_request_date::date as data_requisicao_exame,
                min(s.leucocitos) as leuco_min,
                max(s.leucocitos) as leuco_max,
                avg(s.leucocitos) as leuco_avg,
                min(s.rdw) as rdw_min,
                max(s.rdw) as rdw_max,
                avg(s.rdw) as rdw_avg,
                min(s.neutrofilo) as neuto_min,
                max(s.neutrofilo) as neuto_max,
                avg(s.neutrofilo) as neuto_avg,
                min(s.pcr) as pcr_min,
                max(s.pcr) as pcr_max,
                avg(s.pcr) as pcr_avg,
                max(s.clostridium) as clostridium_pos,
                max(s.mrsa) as mrsa_pos,
                max(s.virus_resp) as virus_resp_pos,
                --min(s.proteina_liquor) as proteina_liquor_min,
                max(s.proteina_liquor) as proteina_liquor_max,
                --avg(s.proteina_liquor) as proteina_liquor_avg,
                min(s.glicose_liquor) as glicose_liquor_min
                --max(s.glicose_liquor) as glicose_liquor_max
                --avg(s.glicose_liquor) as glicose_liquor_avg
            from  hemograma_bioquimica_pivot s
            group by s.registro, s.laboratory_request_date;
    """)

if __name__ == "__main__":
    main()