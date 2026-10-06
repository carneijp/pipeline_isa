from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c = pd.DataFrame):
   
    colunas = ["texto_futuro", "texto_hoje", "texto_passado"]
    c = maestro.normalize(df= c, arrayColumns= colunas)

    c = maestro.trim(df= c, arrayColumns= colunas)

    tuplas = [(r"\n", ". "), (r"\|", "."), (r"\s\.\s", "."), (r"\s\s", ". ")]
    c = maestro.replace_values_list(df= c, arrayColumns= colunas, arrayDeTuplas= tuplas) 
    tuplas = [(r'(\.\s*){2,}', '. ')]
    c = maestro.replace_values_list(df= c, arrayColumns= colunas, arrayDeTuplas= tuplas, regex= True)

    dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_coorte_notes_and_codes_text_prepared", if_exists= "append")

def main():
    replace = True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS imparare2_coorte_notes_and_codes_text_prepared;
            CREATE UNLOGGED TABLE imparare2_coorte_notes_and_codes_text_prepared (
                prontuario int8 NULL,
                dia timestamp NULL,
                id_enterprise smallint NULL,
                texto_futuro text NULL,
                texto_hoje text NULL,
                texto_passado text NULL
            );
        """
        dataRequest.execute(create_query)

    append_query = """
        SELECT
            evo.prontuario AS prontuario,
            evo.dia AS dia,
            evo.id_enterprise::SMALLINT AS id_enterprise,
            COALESCE(CONCAT_WS(' | ',
                ' <<<< EVOLUCAO >>>>> ', evo.evo_futuro, 
                ' <<<< IMAGEM >>>>> ', rx.laudos_futuro, 
                ' <<<< CIRURGIA  >>> ', cir.laudos_cirurgicos_futuro, 
                ' <<<< HEMOCULTURA >>> ', hem.agg_hemocultura_futuro, 
                ' <<<< UROCULTURA >>> ', hem.agg_urocultura_futuro
            ), '') AS texto_futuro,
            COALESCE(CONCAT_WS(' | ',
                ' <<<< EVOLUCAO >>>>> ', evo.evo_hoje, 
                ' <<<< IMAGEM >>>>> ', rx.laudos_hoje, 
                ' <<<< CIRURGIA  >>> ', cir.laudos_cirurgicos_hoje, 
                ' <<<< HEMOCULTURA >>> ', hem.agg_hemocultura_hoje, 
                ' <<<< UROCULTURA >>> ', hem.agg_urocultura_hoje
            ), '') AS texto_hoje,
            COALESCE(CONCAT_WS(' | ',
                ' <<<< EVOLUCAO >>>>> ', evo.evo_passado, 
                ' <<<< IMAGEM >>>>> ', rx.laudos_passado, 
                ' <<<< CIRURGIA  >>> ', cir.laudos_cirurgicos_passado, 
                ' <<<< HEMOCULTURA >>> ', hem.agg_hemocultura_passado, 
                ' <<<< UROCULTURA >>> ', hem.agg_urocultura_passado
            ), '') AS texto_passado
        FROM imparare2_dataset_evolucao evo
        FULL OUTER JOIN imparare2_dataset_raiox rx
            ON evo.prontuario = rx.prontuario 
                AND evo.dia = rx.dia
                AND evo.id_enterprise = rx.id_enterprise
        FULL OUTER JOIN imparare2_dataset_cirurgias cir
            ON evo.prontuario = cir.prontuario AND evo.dia = cir.dia
                AND evo.id_enterprise = cir.id_enterprise
        FULL OUTER JOIN imparare2_dataset_hemograma hem
            ON evo.prontuario = hem.prontuario AND evo.dia = hem.dia
                AND evo.id_enterprise = hem.id_enterprise;
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)

    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()