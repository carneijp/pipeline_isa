from ImpararePackage import dataRequest

def main():
    dataRequest.execute("""create index if not exists imparare2_wellhead_hml_blood_culture_prepared_idx on imparare2_wellhead_hml_blood_culture_prepared("registro", "blood_culture_collection_date", "signature_date", "cd_exa_lab", "exame", "ds_resultado", "item_exame", "dthr_pedido", "dthr_entrega");""")
    dataRequest.execute("""create index if not exists imparare2_isa_exame_gmr_idx on imparare2_isa_exame_gmr("patient_id", "exame", "exame_id", "dthr_pedido", "dthr_entrega", "item_exame", "resultado");""")
    dataRequest.execute("DROP TABLE if exists imparare2_exameslaboratorio_infecto;")
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE imparare2_exameslaboratorio_infecto AS (
            with base as (
                SELECT
                    a.registro,
                    a.blood_culture_collection_date,
                    a.signature_date,
                    a.cd_exa_lab as exame_id,
                    a.exame,
                    a.dthr_pedido,
                    a.dthr_entrega,
                    MAX(a.ds_resultado) FILTER (WHERE a.item_exame = 'BACTERIOSCÓPICO')            AS "BACTERIOSCOPICO",
                    MAX(a.ds_resultado) FILTER (WHERE a.item_exame = 'MATERIAL')                    AS "MATERIAL",
                    MAX(a.ds_resultado) FILTER (WHERE a.item_exame = 'OBSERVAÇÃO DO MATERIAL')      AS "OBSERVAÇÃO DO MATERIAL",
                    MAX(a.ds_resultado) FILTER (WHERE a.item_exame = 'OBSERVAÇÃO DA COLÔNIA')       AS "OBSERVAÇÃO DA COLÔNIA",
                    STRING_AGG(a.ds_resultado, ', ' ORDER BY a.ds_resultado) FILTER (WHERE a.item_exame = 'BACTERIOLÓGICO') AS "BACTERIOLOGICO"
                FROM imparare2_wellhead_hml_blood_culture_prepared a
                GROUP BY
                    a.registro, a.blood_culture_collection_date, a.signature_date,
                    a.cd_exa_lab, a.exame, a.dthr_pedido, a.dthr_entrega	
            )
            SELECT
                e.patient_id  AS registro,
                e.exame,      
                e.exame_id,
                e.dthr_pedido::date AS dthr_pedido,
                e.dthr_entrega AS dthr_entrega,
                e.item_exame,
                (
                    CASE e.resultado
                        WHEN 'P' THEN 'POSITIVO'
                        WHEN 'N' THEN 'NEGATIVO'
                    END  
                ) AS ds_resultado,
                (
                    CASE e.resultado
                        WHEN 'P' THEN 'CULTURA_POSITIVA'
                        WHEN 'N' THEN 'CULTURA_NEGATIVA'
                    END             
                ) AS tipo_exame_infecto,
                'CULTURA'       AS material_exame_infecto,
                null as "BACTERIOLOGICO"
            FROM imparare2_isa_exame_gmr e
            WHERE e.item_exame = 'CULTURA'
            AND e.resultado IN ('P','N')
            union ALL
            SELECT 
                base.registro,
                base.exame,
                base.exame_id,
                base.dthr_pedido::date,
                base.dthr_entrega,
                'BACTERIOSCÓPICO' as item_exame,
                base."BACTERIOSCOPICO" as ds_resultado,
                (
                    CASE base."BACTERIOSCOPICO"
                        WHEN 'NEGATIVO' THEN
                            CASE
                                WHEN base.exame like '%HEMOCULTURA%' then 'HEMOCULTURA'
                                WHEN base.exame like '%FUNGO%' then 'CULTURA_FUNGOS'
                                WHEN base.exame like '%BACTERIOSCOPI%' then 'BACTERIOSCOPIA'
                                WHEN base.exame like '%CORPOCULTU%' then 'CORPOCULTURA'
                                WHEN base.exame like '%UROCULTU%' then 'UROCULTURA'
                                else 'CULTURA'
                            END || '_NEGATIVA'
                        WHEN 'POSITIVO' then
                            CASE
                                WHEN base.exame like '%HEMOCULTURA%' then 'HEMOCULTURA'
                                WHEN base.exame like '%FUNGO%' then 'CULTURA_FUNGOS'
                                WHEN base.exame like '%BACTERIOSCOPI%' then 'BACTERIOSCOPIA'
                                WHEN base.exame like '%CORPOCULTU%' then 'CORPOCULTURA'
                                WHEN base.exame like '%UROCULTU%' then 'UROCULTURA'
                                else 'CULTURA'
                            END || '_POSITIVA'
                    END
                ) AS tipo_exame_infecto,
                base."MATERIAL" AS material_exame_infecto,
                base."BACTERIOLOGICO" as "BACTERIOLOGICO"
            FROM base            
        );
    """)

if __name__ == "__main__":
    main()