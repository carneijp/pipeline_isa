from ImpararePackage import dataRequest
from ImpararePackage import maestro
from multiprocessing import Pool, cpu_count
import pandas as pd

def worker(c = pd.DataFrame):
   
    colunas = ["texto_futuro", "texto_hoje", "texto_passado"]
    c[colunas] = c[colunas].fillna("")

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
                texto_futuro text NULL,
                texto_hoje text NULL,
                texto_passado text NULL
            );
            
            CREATE INDEX IF NOT EXISTS idx_evo_reg_dia  ON "imparare2_dataset_evolucao"   (prontuario, dia);
            CREATE INDEX IF NOT EXISTS idx_rx_reg_dia   ON "imparare2_dataset_raiox"      (prontuario, dia);
            CREATE INDEX IF NOT EXISTS idx_cir_reg_dia  ON "imparare2_dataset_cirurgias"  (prontuario, dia);
            CREATE INDEX IF NOT EXISTS idx_hem_reg_dia  ON "imparare2_dataset_hemograma"  (prontuario, dia);
        """
        dataRequest.execute(create_query)

    append_query = """
        SELECT
            evo.prontuario AS prontuario,
            evo.dia AS dia,
            CONCAT_WS(' | ',
                ' <<<< EVOLUCAO >>>>> ', evo.evo_futuro, 
                ' <<<< IMAGEM >>>>> ', rx.laudos_futuro, 
                ' <<<< CIRURGIA  >>> ', cir.laudos_cirurgicos_futuro, 
                ' <<<< HEMOCULTURA >>> ', hem.agg_hemocultura_futuro, 
                ' <<<< UROCULTURA >>> ', hem.agg_urocultura_futuro
            ) AS texto_futuro,
            CONCAT_WS(' | ',
                ' <<<< EVOLUCAO >>>>> ', evo.evo_hoje, 
                ' <<<< IMAGEM >>>>> ', rx.laudos_hoje, 
                ' <<<< CIRURGIA  >>> ', cir.laudos_cirurgicos_hoje, 
                ' <<<< HEMOCULTURA >>> ', hem.agg_hemocultura_hoje, 
                ' <<<< UROCULTURA >>> ', hem.agg_urocultura_hoje
            ) AS texto_hoje,
            CONCAT_WS(' | ',
                ' <<<< EVOLUCAO >>>>> ', evo.evo_passado, 
                ' <<<< IMAGEM >>>>> ', rx.laudos_passado, 
                ' <<<< CIRURGIA  >>> ', cir.laudos_cirurgicos_passado, 
                ' <<<< HEMOCULTURA >>> ', hem.agg_hemocultura_passado, 
                ' <<<< UROCULTURA >>> ', hem.agg_urocultura_passado
            ) AS texto_passado
        FROM imparare2_dataset_evolucao evo
        FULL OUTER JOIN imparare2_dataset_raiox rx
            ON evo.prontuario = rx.prontuario AND evo.dia = rx.dia
        FULL OUTER JOIN imparare2_dataset_cirurgias cir
            ON evo.prontuario = cir.prontuario AND evo.dia = cir.dia
        FULL OUTER JOIN imparare2_dataset_hemograma hem
            ON evo.prontuario = hem.prontuario AND evo.dia = hem.dia;
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)

    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()