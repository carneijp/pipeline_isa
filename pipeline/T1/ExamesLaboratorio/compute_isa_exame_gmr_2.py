from ImpararePackage import dataRequest

def main():
    dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_isa_exame_idx_1 ON "imparare2_isa_exame" ("patient_id", "dthr_pedido");')
    dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_isa_exame_idx_2 ON "imparare2_isa_exame" ("id");')
    
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_isa_exame_gmr"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_isa_exame_gmr" AS
            select isa_e.*, COALESCE(g.gmr, 0) as gmr
        from "imparare2_isa_exame" isa_e
        LEFT JOIN (
            SELECT DISTINCT e2.*, 1 as GMR--e1.id, 1 as GMR
                FROM "public"."imparare2_isa_exame" e2 
                    JOIN "public"."imparare2_isa_exame" e1 ON e2."patient_id" = e1."patient_id" AND e2."dthr_pedido" = e1."dthr_pedido"
                        where (UPPER(e2."exame") LIKE '%%CULTURA%%QUANT%%'
                            OR UPPER(e2."exame") LIKE '%%UROCULTURA%%'
                            OR UPPER(e2."exame") LIKE '%%HEMOCULTURA%%')
                        --    AND e2."item_exame" LIKE '%%CULTURA%%' 
                            AND (e2."resultado" ILIKE '%%klebsiella%%' 
                            OR e2."resultado" ILIKE '%%escherichia%%coli%%' 
                            OR e2."resultado" ILIKE '%%proteus%%'  
                            OR e2."resultado" ILIKE '%%enterobacter%%' 
                            OR e2."resultado" ILIKE '%%serratia%%' 
                            OR e2."resultado" ILIKE '%%morganella%%' 
                            OR e2."resultado" ILIKE '%%citrobacter%%' 
                            OR e2."resultado" ILIKE '%%providencia%%' 
                            OR e2."resultado" ILIKE '%%shigella%%' 
                            OR e2."resultado" ILIKE '%%edwardsiella%%' 
                            OR e2."resultado" ILIKE '%%salmonella%%' 
                            OR e2."resultado" ILIKE '%%hafnia%%' 
                            OR e2."resultado" ILIKE '%%yersinia%%' 
                            OR e2."resultado" ILIKE '%%acinetobacter%%' 
                            OR e2."resultado" ILIKE '%%pseudomonas%%')
                            AND (e1."item_exame" ILIKE '%%IMIPINEM%%'
                            OR e1."item_exame" ILIKE '%%IMIPENEM%%'
                            OR e1."item_exame" ILIKE '%%meropenem%%'
                            OR e1."item_exame" ILIKE '%%ertapenem%%')
                            AND (e1."resultado" = 'R' or e1."resultado" ILIKE '%%R MIC%%')
            UNION
            SELECT DISTINCT e2.*, 1 as GMR--e1.id, 1 as GMR
                FROM "public"."imparare2_isa_exame" e2 
                    JOIN "public"."imparare2_isa_exame" e1 ON e2."patient_id" = e1."patient_id" 
                                                                AND e2."dthr_pedido" = e1."dthr_pedido"
                        where (UPPER(e2."exame") LIKE '%%CULTURA%%QUANT%%'
                            OR UPPER(e2."exame") LIKE '%%UROCULTURA%%'
                            OR UPPER(e2."exame") LIKE '%%HEMOCULTURA%%')
                            -- AND e2."item_exame" LIKE 'CULTURA%%' 
                            AND e2."resultado" ILIKE '%%staphylococcus%%aureus%%'
                            AND e1."item_exame" ILIKE '%%oxacilina%%'
                            AND (e1."resultado" = 'R' or e1."resultado" ILIKE '%%R MIC%%')
            UNION
            SELECT DISTINCT e2.*, 1 as GMR--e1.id, 1 as GMR
                FROM "public"."imparare2_isa_exame" e2 
                    JOIN "public"."imparare2_isa_exame" e1 ON e2."patient_id" = e1."patient_id" 
                                                                AND e2."dthr_pedido" = e1."dthr_pedido"
                        where (UPPER(e2."exame") LIKE '%%CULTURA%%QUANT%%'
                            OR UPPER(e2."exame") LIKE '%%UROCULTURA%%'
                            OR UPPER(e2."exame") LIKE '%%HEMOCULTURA%%')
                            -- AND e2."item_exame" LIKE 'CULTURA%%' 
                            AND e2."resultado" ILIKE '%%enterococcus%%'
                            AND e1."item_exame" ILIKE '%%vancomicina%%'
                            AND (e1."resultado" = 'R' or e1."resultado" ILIKE '%%R MIC%%')
            UNION 
            SELECT DISTINCT e2.*, 1 as GMR
                FROM "public"."imparare2_isa_exame" e2 
                    WHERE (UPPER(e2."exame") LIKE '%%CULTURA%%QUANT%%'
                            OR UPPER(e2."exame") LIKE '%%UROCULTURA%%'
                            OR UPPER(e2."exame") LIKE '%%HEMOCULTURA%%')
                        -- AND e2."item_exame" LIKE '%%CULTURA%%' 
                        AND e2."resultado" ILIKE '%%clostridium%%difficile%%'
            UNION
            SELECT DISTINCT e2.*, 1 as GMR
                FROM "public"."imparare2_isa_exame" e2 
                    WHERE e2."exame" = '%%CULTURA%%VIGIL%%'
                        AND e2."resultado" ILIKE '%%POSIT%%'
        ) g 
        ON isa_e.id = g.id;
    """)

if __name__ == "__main__":
    main()