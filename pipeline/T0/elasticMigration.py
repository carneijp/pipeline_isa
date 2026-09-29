from ImpararePackage import dataRequest
import os

def main():
    print ("Inicinado elasticMigration download")
    query_create_if_not_exists = """
        CREATE UNLOGGED TABLE IF NOT EXISTS elk_indexes (
            id text NOT NULL,
            key text NOT NULL,
            value text NOT NULL,
            company_id uuid NULL,
            CONSTRAINT "UQ_9dfc66630a611662b49ecf9ef47" UNIQUE (id)
        );
    """
    
    dataRequest.execute(queryText= query_create_if_not_exists, isLocal= False)
    
    query_get_existing_data = """
        SELECT * FROM elk_indexes; 
    """
    
    df = dataRequest.get_data(queryText= query_get_existing_data, isLocal= False, chunck= None)
    
    if len(df) > 0:
        dataRequest.set_data_on_sql(df= df, nomeTabelaDestino= "elk_indexes", if_exists= "replace", isLocal= True)
    else:
        dataRequest.execute(queryText= query_create_if_not_exists, isLocal= True)

        database_client = os.getenv('CLIENT_NAME')
        
        if database_client is None:
            database_client = "materdei"

        query_insert = f"""
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'pacientes', 'pacientes-{database_client}', NULL);

            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'avaliacoes', 'avaliacoes-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'encontros', 'encontros-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'exames', 'exames-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'laudos', 'laudos-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'medicamentos', 'medicamentos-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'procedimentos', 'procedimentos-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'sinais-vitais', 'sinais-vitais-{database_client}', NULL);

            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'suspeitas', 'suspeitas-{database_client}', NULL);

            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'infeccoes', 'infeccoes_{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'unidades', 'unidades-{database_client}', NULL);
            
            INSERT INTO elk_indexes (id, key, value, company_id)
            VALUES(gen_random_uuid(), 'valores-referencias', 'valores-referencias-{database_client}', NULL);

        """

        dataRequest.execute(queryText= query_insert, isLocal= False)

        # Atualizando o banco local com os novos valores do banco remoto
        df = dataRequest.get_data(queryText= query_get_existing_data, isLocal= False, chunck= None)
        dataRequest.set_data_on_sql(df= df, nomeTabelaDestino= "elk_indexes", if_exists= "replace", isLocal= True)
        print("Terminando elk_indexes - elasticMigration")

if __name__ == "__main__":
    main()