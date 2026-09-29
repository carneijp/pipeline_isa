from ImpararePackage import dataRequest

def main():
    #dataRequest.execute('CREATE INDEX IF NOT EXISTS imparare2_new_isa_set_scored_casos_infeccao_rescaled_1_idx ON imparare2_new_isa_set_scored_casos_infeccao_rescaled(prontuario, dia_parsed, month_quadrant, month_start, month_end);')
    dataRequest.execute('DROP TABLE IF EXISTS imparare2_isa_suspeita_v3;')

    query = """
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE imparare2_isa_suspeita_v3 AS
           WITH midstep AS (
           SELECT DISTINCT ON (prontuario, month_quadrant, month_start, month_end)
                prontuario,
                month_start,
                month_end,
                month_quadrant,
                dia_parsed   AS first_date,
                proba_1      AS max_prob,
                rescaled_proba_1
            FROM imparare2_new_isa_set_scored_casos_infeccao_rescaled
            ORDER BY
                prontuario,
                month_quadrant,
                month_start,
                month_end,
                proba_1 DESC
           ),
           midstep_max AS (
            SELECT DISTINCT ON (prontuario, month_start, month_end)
                prontuario,
                month_start,
                month_end,
                month_quadrant,
                first_date,
                max_prob,
                rescaled_proba_1
            FROM midstep                
            ORDER BY
                prontuario,
                month_start,
                month_end,
                max_prob DESC
        ),
        suspeitas AS (
        SELECT DISTINCT
            s.prontuario            AS paciente_id,
            i.cd_atendimento,
            i.dthr_atendimento_parsed AS dthr_internacao,
            i.dthr_alta_parsed        AS dthr_alta,
            s.first_date::date        AS dt_infeccao,
            s.max_prob                AS prob_perc,
            s.max_prob,
            s.first_date::date,
            s.month_start, 
            s.month_end,
            ''                        AS avaliacao_status,
            ''                        AS avaliacao_data,
            ''                        AS avaliacao_responsavel,
            ''                        AS avaliacao_comentario,
            ''                        AS notificado
        FROM (
            SELECT prontuario, month_start, month_end, month_quadrant,
                first_date, max_prob, rescaled_proba_1
            FROM midstep_max
            UNION
            SELECT ms.prontuario, ms.month_start, ms.month_end, ms.month_quadrant,
                ms.first_date, ms.max_prob, ms.rescaled_proba_1
            FROM midstep ms
            INNER JOIN midstep_max mx
                ON  ms.prontuario   = mx.prontuario
                AND ms.month_start  = mx.month_start
                AND ms.month_end    = mx.month_end
                AND (   ms.month_quadrant = mx.month_quadrant + 2
                    OR ms.month_quadrant = mx.month_quadrant - 2)
        ) s
        JOIN imparare2_internacoes_prepared i
        ON  s.prontuario = i.registro
        AND s.first_date::timestamp
            BETWEEN DATE_TRUNC('day', i.dthr_atendimento_parsed)::timestamp
                AND DATE_TRUNC('day', COALESCE(i.dthr_alta_parsed, now()))::timestamp
        ORDER BY s.prontuario, s.month_start, s.month_end, s.first_date
        )
        SELECT 
            paciente_id,
            cd_atendimento,
            dthr_internacao,
            dthr_alta,
            dt_infeccao,
            prob_perc,
            max_prob,
            first_date,
            avaliacao_status,
            avaliacao_data,
            avaliacao_responsavel,
            avaliacao_comentario,
            notificado
        FROM suspeitas
    """

    dataRequest.execute(queryText= query)

if __name__ == "__main__":
    main()