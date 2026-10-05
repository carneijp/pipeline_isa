from ImpararePackage import dataRequest
from multiprocessing import Pool, cpu_count
from worker_compute_evol_sent_pos_joined_prepared_3 import main as worker

def main():
    replace = True

    if replace:
        dataRequest.execute("DROP TABLE IF EXISTS imparare2_evol_sent_pos_joined_prepared;")
        create_query = """
            CREATE UNLOGGED TABLE imparare2_evol_sent_pos_joined_prepared (
                registro int8 NULL,
                dthr_evolucao DATE NULL,
                dthr_evolucao_hr timestamp NULL,
                texto_evolucao text NULL,
                termos_achados text NULL,
                perfil_termos text NULL,
                id_enterprise int4 NULL
            );
        """
        dataRequest.execute(create_query)

    append_query = """
        SELECT
            registro,
            perfil,
            dthr_evolucao::date as dthr_evolucao,
            dthr_evolucao as dthr_evolucao_hr,
            sentence_original as texto_evolucao,
            new_sentence,
            id_enterprise
        FROM imparare2_evolucao_anon_data_trunc
        ORDER BY registro, id_enterprise, new_sentence, dthr_evolucao
    """
    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)

    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()
