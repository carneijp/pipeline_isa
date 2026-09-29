from ImpararePackage import dataRequest

def main():
    print("Iniciando companyCodeMigration")
    query_create_table_if_not_exists = """
        CREATE UNLOGGED TABLE IF NOT EXISTS isa_companies (
            id uuid NOT NULL,
            name text NOT NULL,
            code text NOT NULL,
            sso_client_name text NOT NULL,
            CONSTRAINT "PK_4711c1cc17e9492ba4b6a5f280a" PRIMARY KEY (id),
            CONSTRAINT "UQ_1e8356fedbbe62bcd46fa94a291" UNIQUE (sso_client_name),
            CONSTRAINT "UQ_216a287f5e0ca4ded72e74a294f" UNIQUE (name),
            CONSTRAINT "UQ_d52e9703f3783524297917ec90c" UNIQUE (code)
        );
    """

    dataRequest.execute(queryText= query_create_table_if_not_exists, isLocal= False)

    query_select_companies = """
        SELECT * FROM isa_companies;
    """

    df = dataRequest.get_data(queryText= query_select_companies, isLocal= False, chunck= None)

    if len(df) > 0:
        dataRequest.set_data_on_sql(df= df, nomeTabelaDestino= "isa_companies", isLocal= True)
    else:
        dataRequest.execute(queryText= query_create_table_if_not_exists, isLocal= True)

        query_insert = """
            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL MATER DEI S/A STO AGOSTINHO', '1', 'materdei_sto_agostinho');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL MATER DEI S/A CONTORNO', '6', 'materdei_contorno');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL MATER DEI S/A BETIM-CONTAGEM', '7', 'materdei_betim_contagem');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL MATER DEI S/A SALVADOR/BAHIA', '8', 'materdei_salvador_bahia');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'EMEC EMPREENDIMENTOS', '22', 'emec');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL E MATERNIDADE SANTA CLARA', '23', 'maternidade_santa_clara');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'PREMIUM', '21', 'premium');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL SANTA GENOVEVA LTDA',	'18',	'santa_genoveva');

            INSERT INTO isa_companies (id, name, code, sso_client_name)
            VALUES(gen_random_uuid(), 'HOSPITAL NOVA LIMA',	'12',	'nova_lima');
        """

        
        dataRequest.execute(queryText= query_insert, isLocal= False)

        df = dataRequest.get_data(queryText= query_select_companies, isLocal= False, chunck= None)
        dataRequest.set_data_on_sql(df= df, nomeTabelaDestino= "isa_companies", if_exists= "replace", isLocal= True)
        print("Finalizando download/criação de isa_comapanies -companyCodeMigration")

if __name__ == "__main__":
    main()
    