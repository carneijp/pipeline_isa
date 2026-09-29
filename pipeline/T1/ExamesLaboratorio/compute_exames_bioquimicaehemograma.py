from ImpararePackage import dataRequest, maestro
from multiprocessing import Pool, cpu_count
import pandas as pd
import re

def tratar_resultado_exame(valor):
    texto = str(valor).strip().upper()
    termos_negativos = ["NEGATIV", "NAO DETECT", "NÃO DETECT", "NOT DETEC", "NORNAL", "AUSENT", "NAO REAGENTE", "NÃO REAGENTE"]
    termos_positivos = ["POSITIV", "DETECT", "REAGENTE", "ALTERA", "PRESENT", "INCONC", "INDETERM"] #O QUE É P RESULTADO "ALTA" PARA PCR DE VRUS RESPIRATORIO?
    numeros_limpos = re.sub(r'[^0-9.,]', '', texto)

    if any(termo in texto for termo in termos_negativos):
        return 0
    elif any(termo in texto for termo in termos_positivos):
        return 1
    
    numeros_limpos = re.sub(r'[^0-9.,]', '', texto)
    if not numeros_limpos:
        return None
    try:
        if ',' in numeros_limpos and '.' in numeros_limpos:
            numeros_limpos = numeros_limpos.replace('.', '').replace(',', '.')
        elif ',' in numeros_limpos:
            numeros_limpos = numeros_limpos.replace(',', '.')
        return float(numeros_limpos)
    except ValueError:
        return None #força a só tratar os tipos de resultado elencados na função, vai dar nulo para qualquer outro resultado

def transpose(row):
    tipo = row['tipo']
    nome = row['exam_lab_name']
    valor = row['valor']
    if tipo == 'GLOBAL DE LEUCOCITOS':
        row['leucocitos'] = valor
    elif tipo == 'RDW':
        row['rdw'] = valor
    elif tipo == 'SEGMETADO NEUTROFILO':
        row['neutrofilo'] = valor
    elif tipo == 'RESULTADO' and row['exam_lab_name'] == 'PCR (PROTEINA C REATIVA)':
        row['pcr'] = valor
    elif 'CLOSTRIDIUM' in nome:
        row['clostridium'] = valor
    elif 'MRSA' in nome:
        row['mrsa'] = valor
    elif 'VI' in nome:
        row['virus_resp'] = valor
    elif 'PROT' in tipo and'LIQUOR' in nome:
        row['proteina_liquor'] = valor
    elif 'GLICOSE' in tipo and'LIQUOR' in nome:
        row['glicose_liquor'] = valor
    else:
        print(f"deu ruim: {nome} - {tipo} - {valor}")
    
    return row

def worker(c:pd.DataFrame):
    c['valor'] = c['valor'].apply(tratar_resultado_exame).astype(float)
    c[['leucocitos', 'rdw', 'neutrofilo', 'clostridium', 'mrsa', 'virus_resp', 'proteina_liquor', 'glicose_liquor', 'pcr']] = None

    c = c.apply(transpose, axis= 1)
    
    c[['leucocitos', 'rdw', 'neutrofilo', 'glicose_liquor', 'proteina_liquor', 'pcr']] = c[['leucocitos', 'rdw', 'neutrofilo', 'glicose_liquor', 'proteina_liquor', 'pcr']].astype(float)
    c.drop(columns=['tipo', 'valor', 'exam_lab_name'], inplace = True)

    dataRequest.set_data_on_sql(c, nomeTabelaDestino= 'hemograma_bioquimica_pivot', if_exists= 'append')


def main():
    replace =True

    if replace:
        create_query = """
            DROP TABLE IF EXISTS hemograma_bioquimica_pivot;
            CREATE UNLOGGED TABLE hemograma_bioquimica_pivot (
                registro INTEGER,
                laboratory_request_date TIMESTAMP,
                leucocitos FLOAT,
                rdw FLOAT,
                neutrofilo FLOAT,
                clostridium FLOAT,
                mrsa FLOAT,
                virus_resp FLOAT,
                pcr FLOAT,
                proteina_liquor FLOAT,
                glicose_liquor FLOAT
            );
        """
        dataRequest.execute(create_query)

    append_query = f"""
        select 
            record_id as registro, 
            laboratory_request_date,
            exam_lab_name,
            er.exam_result_description as valor,
            exam_result_field_name as tipo
        from exams_reports er
        where (record_id in (select distinct record_id from patients_to_update) or 1 = {maestro.get_must_update_all_patients()})
            AND (
                (exam_lab_name = 'HEMOGRAMA' and exam_result_field_name in ('GLOBAL DE LEUCOCITOS', 'RDW', 'SEGMETADO NEUTROFILO')) 
                or (er.exam_lab_name = 'PCR (PROTEINA C REATIVA)' and er.exam_result_field_name = 'RESULTADO')
                or er.exam_result_field_name ilike'%protfli%'
                or er.exam_result_field_name ilike'%glicose liquor%'
                or (er.exam_lab_name = 'ROTINA DE LIQUIDO CEFALORRAQUIDIANO (LIQUOR)' and (er.exam_result_field_name = 'PROTEINAS' or er.exam_result_field_name = 'GLICOSE'))
                or er.exam_lab_name ilike '%clostr%'
                or er.exam_lab_name ilike '%mrsa%'
                or (er.exam_lab_name ilike '%sinci%'and er.exam_result_field_name = 'RESULTADO')
                or (er.exam_lab_name ilike '%covid%' and er.exam_result_field_name ilike '%RESULTADO%')
                or er.exam_lab_name = 'PAINEL INF RESPIRATÓRIAS VIRAIS, MYCOPLASMA E BORDETELLA'
            );
    """

    df_iterator = dataRequest.get_data(queryText= append_query, chunck= 2000)
    with Pool(processes= cpu_count()) as pool:
        for _ in pool.imap_unordered(worker, df_iterator):
            pass

if __name__ == "__main__":
    main()