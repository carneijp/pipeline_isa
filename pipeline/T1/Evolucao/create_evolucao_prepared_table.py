from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""
        SET synchronous_commit = off;
        DROP TABLE IF EXISTS imparare2_evolucao_prepared;
        CREATE UNLOGGED TABLE imparare2_evolucao_prepared (
            patient_id int4,
            cd_pre_med int4,
            perfil text,
            dthr_evolucao timestamp,
            unidade text,
            texto_evolucao text,
            tipo_atendimento text
        );
    """)

if __name__ == "__main__":
    main()