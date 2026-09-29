from ImpararePackage import dataRequest

def main():
    dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_raiox_computed_idx_1 ON "imparare2_raiox_computed"(registro, data);')

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_dataset_raiox"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_dataset_raiox" AS
        SELECT  
            pct_dia.registro as prontuario, 
            pct_dia.dia  as dia,
            (SELECT 
                string_agg(rx.laudos_dia,' | ' order by rx.data) 
             FROM "imparare2_raiox_computed" AS rx 
             WHERE pct_dia.registro = rx.registro 
                AND rx.data BETWEEN pct_dia.dia + INTERVAL '1 day'
                AND pct_dia.dia + INTERVAL '3 day'
             GROUP BY pct_dia.registro,  pct_dia.dia
            ) laudos_futuro,
            (SELECT 
                string_agg(rx.laudos_dia, rx.data||' | ' order by rx.data) 
             FROM "imparare2_raiox_computed" AS rx 
             WHERE pct_dia.registro = rx.registro 
                AND rx.data = pct_dia.dia
            ) as laudos_hoje,
            (SELECT 
                string_agg(rx.laudos_dia,' | ' order by rx.data) 
             FROM "imparare2_raiox_computed" AS rx 
             WHERE pct_dia.registro = rx.registro 
                AND rx.data BETWEEN pct_dia.dia - INTERVAL '3 day'
                AND pct_dia.dia - INTERVAL '1 day'
             GROUP BY pct_dia.registro,  pct_dia.dia
            ) AS laudos_passado,
            COALESCE(
                (SELECT 
                    sum(rx.count_laudos_dia::numeric)
                FROM "imparare2_raiox_computed" AS rx 
                WHERE pct_dia.registro = rx.registro 
                    AND pct_dia.dia = rx.data
            ), 0) as laudo_exame_count
        FROM imparare2_dataset_label pct_dia
        LEFT JOIN imparare2_raiox_computed rx_computed
            ON pct_dia.registro = rx_computed.registro
            AND pct_dia.dia = rx_computed.data
    """)


if __name__ == "__main__":
    main()