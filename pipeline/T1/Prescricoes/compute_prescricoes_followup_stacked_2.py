from ImpararePackage import  dataRequest

def main():

    dataRequest.execute("""
        SET synchronous_commit = off;
        DROP TABLE IF EXISTS imparare2_prescricoes_followup_stacked;
        CREATE UNLOGGED TABLE imparare2_prescricoes_followup_stacked AS
            SELECT DISTINCT 
                registro,
                cd_pre_med,
                dthr_prescricao,
                atb  AS antibiotico,
                dose,
                unidade,
                frequencia,
                via,
                'I' AS tipo_atendimento
            FROM imparare2_prescricoesantibiotico_prepared_teste
            UNION
            SELECT DISTINCT 
                registro,
                cd_pre_med,
                dthr_prescricao,
                atb  AS antibiotico,
                dose,
                unidade,
                frequencia,
                via,
                attendance_type AS tipo_atendimento
            FROM imparare2_wellhead_hml_prescriptions_followup_prepared;
    """)

if __name__ == "__main__":
    main()