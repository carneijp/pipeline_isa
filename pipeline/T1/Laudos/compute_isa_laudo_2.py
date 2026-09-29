from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_isa_laudo"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_isa_laudo" AS
        select 
            (data_pedido::varchar||data_entrega::varchar||registro::varchar||cd_ped_rx::varchar||ds_exa_rx::varchar||attendance_type::varchar) as id, 
            registro as registro,
            cd_ped_rx as codigo_laudo,
            ds_exa_rx as descricao_laudo,
            data_pedido as dthr_pedido,
            data_entrega as dthr_entrega_laudo, 
            ds_laudo as laudo_texto,
            attendance_type as tipo_atendimento, 
            null as ordem,
            null as criterio
        from "imparare2_laudos_raiox_followup_stacked";
    """)

if __name__ == "__main__":
    main()