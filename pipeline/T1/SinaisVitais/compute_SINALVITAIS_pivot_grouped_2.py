from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""
        SET synchronous_commit = off;

        CREATE INDEX IF NOT EXISTS imparare2_sinalvitais_pivot_idx_1 ON imparare2_sinalvitais_pivot(registro, dia);

        DROP TABLE IF EXISTS imparare2_dataset_enfermagem;

        CREATE UNLOGGED TABLE imparare2_dataset_enfermagem AS
        SELECT 
            registro AS registro,
            dia::date AS dia,
            MIN("FC") AS "FC_min",
            MAX("FC") AS "FC_max",
            MIN("FR") AS "FR_min",
            MAX("FR") AS "FR_max",
            MIN("HGT") AS "HGT_min",
            MAX("HGT") AS "HGT_max",
            MIN("OXIMETRIA") AS "OXIMETRIA_min",
            MAX("OXIMETRIA") AS "OXIMETRIA_max",
            MIN("PAD") AS "PAD_min",
            MAX("PAD") AS "PAD_max",
            MIN("PAS") AS "PAS_min",
            MAX("PAS") AS "PAS_max",
            MIN("TEMP") AS "TEMP_min",
            MAX("TEMP") AS "TEMP_max",
            MIN("O2") AS "O2_min",
            MAX("O2") AS "O2_max",
            MIN("FIO2") AS "FIO2_min",
            MAX("FIO2") AS "FIO2_max",
            MIN("PEEP") AS "PEEP_min",
            MAX("PEEP") AS "PEEP_max",
            COUNT(*) AS "SINAIS_VITAIS_count_total"
        FROM imparare2_sinalvitais_pivot
        GROUP BY registro, dia;
    """)
    
if __name__ == "__main__":
    main()