from ImpararePackage import dataRequest

def main():
    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_paciente_dia_internacao_with_label_nova"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_paciente_dia_internacao_with_label_nova" AS
        select 
                a.registro::int, 
                a.sexo::text, 
                a.dt_nascimento_parsed::date, 
                a.idade_anos::smallint,
                a.idade_dias::int, 
                a.dia::date,
                a.dthr_atendimento::date, 
                a.nmconvenio::text, 
                a.unidade::text, 
                a.especialidade::text, 
                a.tipo_clinica::text, 
                a.tipo_intern::text, 
                a.dthr_alta::date, 
                a.alta::text
        from (
            select 
                int.registro, 
                pac.sexo::text, 
                pac.dt_nascimento_parsed::date,
                EXTRACT(YEAR FROM AGE(date(dd), pac.dt_nascimento_parsed)) AS idade_anos,
                (date(dd) - pac.dt_nascimento_parsed::date) AS idade_dias,
                dd as dia,
                int.dthr_atendimento, 
                int.nmconvenio, 
                int.unidade, 
                int.especialidade, 
                int.tipo_clinica, 
                int.tipo_intern,
                COALESCE(dthr_alta, (SELECT MAX(e.dthr_evolucao) FROM imparare2_evolucao_prepared as e WHERE e.patient_id = pac.registro)) as dthr_alta, 
                COALESCE(alta, 'AINDA INTERNADO') as alta
            from generate_series('2020-01-01' , (date_trunc('day', (NOW() + interval '1 day'))::date), '1 day'::interval) dd, 
                imparare2_pacientes_prepared pac 
            inner join imparare2_internacoes_prepared int
                on pac.registro = int.registro
            where date(dd) BETWEEN date(dthr_atendimento) 
                and date(COALESCE(dthr_alta, (SELECT MAX(e.dthr_evolucao) FROM imparare2_evolucao_prepared as e WHERE e.patient_id = pac.registro)))
        ) a
    """)

if __name__ == "__main__":
    main()