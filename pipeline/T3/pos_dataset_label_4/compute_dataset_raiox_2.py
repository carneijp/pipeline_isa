from ImpararePackage import dataRequest

def main():
    dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_raiox_computed_idx_1 ON imparare2_raiox_computed(record_id, data);')

    dataRequest.execute("""
        SET synchronous_commit = off;
       
        DROP TABLE IF EXISTS imparare2_dataset_raiox;

        CREATE UNLOGGED TABLE imparare2_dataset_raiox AS
            SELECT  -- DISTINCT
                pct_dia.registro as prontuario, 
                pct_dia.dia  as dia,
                pct_dia.id_enterprise::SMALLINT as id_enterprise,
                (SELECT 
                    string_agg(rx.laudos_dia,' | ' order by rx.data) 
                FROM imparare2_raiox_computed AS rx 
                WHERE pct_dia.registro = rx.record_id 
                    AND rx.data BETWEEN pct_dia.dia + INTERVAL '1 day' AND pct_dia.dia + INTERVAL '3 day'
                    AND pct_dia.id_enterprise = rx.id_enterprise
                GROUP BY pct_dia.registro,  pct_dia.dia, pct_dia.id_enterprise
                ) laudos_futuro,
                (SELECT 
                    string_agg(rx.laudos_dia, rx.data||' | ' order by rx.data) 
                FROM imparare2_raiox_computed AS rx 
                WHERE pct_dia.registro = rx.record_id 
                    AND rx.data = pct_dia.dia
                    AND pct_dia.id_enterprise = rx.id_enterprise
                ) as laudos_hoje,
                (SELECT 
                    string_agg(rx.laudos_dia,' | ' order by rx.data) 
                FROM imparare2_raiox_computed AS rx 
                WHERE pct_dia.registro = rx.record_id 
                    AND rx.data BETWEEN pct_dia.dia - INTERVAL '3 day' AND pct_dia.dia - INTERVAL '1 day'
                    AND pct_dia.id_enterprise = rx.id_enterprise
                GROUP BY pct_dia.registro, pct_dia.dia, pct_dia.id_enterprise
                ) AS laudos_passado,
                COALESCE(
                    (SELECT 
                        sum(rx.count_laudos_dia::numeric)
                    FROM imparare2_raiox_computed AS rx 
                    WHERE pct_dia.registro = rx.record_id 
                        AND pct_dia.dia = rx.data
                        AND pct_dia.id_enterprise = rx.id_enterprise
                ), 0) as laudo_exame_count
            FROM imparare2_dataset_label pct_dia
            LEFT JOIN imparare2_raiox_computed rx_computed
                ON pct_dia.registro = rx_computed.record_id
                AND pct_dia.dia = rx_computed.data
                AND pct_dia.id_enterprise = rx_computed.id_enterprise;
            
        CREATE INDEX IF NOT EXISTS idx_rx_reg_dia ON imparare2_dataset_raiox (id_enterprise, prontuario, dia);
    """)


if __name__ == "__main__":
    main()