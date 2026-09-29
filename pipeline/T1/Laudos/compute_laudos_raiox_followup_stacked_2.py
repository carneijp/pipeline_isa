from ImpararePackage import dataRequest

def main():

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_laudos_raiox_followup_stacked"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_laudos_raiox_followup_stacked" AS
        SELECT DISTINCT 
            registro::integer AS registro,
            cd_ped_rx AS cd_ped_rx,
            ds_exa_rx AS ds_exa_rx,
            data_pedido AS data_pedido,
            data_entrega AS data_entrega,
            ds_laudo AS ds_laudo,
            'I' AS attendance_type
        FROM "imparare2_laudos_copy_raiox_prepared"
        UNION
        SELECT DISTINCT 
            registro,
            cd_ped_rx,
            ds_exa_rx,
            data_pedido,
            data_entrega,
            ds_laudo,
            attendance_type
        FROM "imparare2_wellhead_hml_xray_followup_prepared";
    """)

if __name__ == "__main__":
    main()