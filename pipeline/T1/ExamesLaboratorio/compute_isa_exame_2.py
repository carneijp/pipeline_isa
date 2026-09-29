from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_isa_exame"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_isa_exame" AS
            SELECT
                dthr_pedido::varchar||dthr_entrega::varchar||registro::varchar||cd_exa_lab::varchar||
                exame||item_exame||COALESCE(ds_resultado::varchar, '1')||COALESCE(tipo_atendimento::varchar, '1')||
                COALESCE(ordem_amostra::varchar, '') || COALESCE(signature_date::varchar, '') as id, 
                registro as patient_id,
                cd_exa_lab as exame_id, 
                exame as exame, 
                item_exame as item_exame, 
                dthr_pedido as dthr_pedido, 
                dthr_entrega as dthr_entrega,
                ds_resultado as resultado,
                tipo_atendimento as tipo_atendimento,
                ordem_amostra as ordem_amostra,
                signature_date as data_assinatura,
                null as ordem,
                null as criterio
            from "imparare2_exameslaboratorio_followup_stacked";
    """)

if __name__ == "__main__":
    main()