from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_isa_pacientes"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_isa_pacientes" AS
        SELECT "REGISTRO", "SEXO", "DT_NASCIMENTO_parsed"--, "Idade Hoje"
        FROM "imparare2_pacientes_prepared"
    """)

if __name__ == "__main__":
    main()