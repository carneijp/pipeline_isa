from ImpararePackage import maestro
from ImpararePackage import dataRequest
from ImpararePackage import regexPattern
import pandas as pd
import urllib.parse


# Rótulo (não é o regex de casamento -- esse vem de regexPattern.regex_search) exibido em
# termos_achados quando o critério bate na frase. Preservado tal como no worker anterior.
_VALUES_MAP = {
    "ronco":"sronc|ronc|estert",
    "tosse":"tosse|dispn|taquip",
    "cavita":"cavita",
    "opac":"opac",
    "infil":"infil",
    "fibrose_cistica":"fibr\\w* \\w*cistica",
    "sec_pur_pulmonar":"puru\\w* \\w*resp|secrec\\w* \\w*resp|mucopurul|escarr|hematopuru|via\\w* \\w*aer",
    "secr_traq":"secrec\\w* \\w*traq",
    "secr":"secrec",
    "puru":"purul",
    "dpoc":"dpoc|doen\\w* \\w*pulm\\w* \\w*obst\\w* \\w*cr",
    "hemoptise": "hemopt",
    "leucemia":"leuce",
    "esplenectomia": "esplenec",
    "febre":"febr",
    "consol":"consol",
    "linfoma":"linfoma",
    "o2":"o2|ox|o²",
    "acinetobacter":"acinetobac",
    "amarelada":"amarel",
    "aspiracao":"aspira",
    "broncograma_aereo":"broncog\\w* \\w*aere",
    "crepitante":"crepit",
    "enterobacter":"enterobac",
    "enterococcus":"enterococ",
    "hemophylus": "hemoph|haemoph",
    "hipertermia":"hiperter",
    "imunossuprimido":"imunossup",
    "infeccao":"infec",
    "klebsiella":"klebsiel|kpc",
    "legionella":"legionel",
    "leucocitose":"leucocitose",
    "leucopenia":"leucopen|neutropen",
    "moraxella":"moraxel",
    "pneumococcus":"pneumococ",
    "pseudomonas":"pseudomon",
    "sibilos": "sibilo",
    "intubacao":"intub",
    "staphylococcus_aureus":"staphylococcus aureus",
    "sepse_pulmonar":"sepse\\w* \\w*pulmon",
    "sepse_respiratoria":"sepse\\w* \\w*respir",
    "sepse_urinaria":"sepse\\w* \\w*urinari",
    "padrao_ventilatorio":"padrao\\w* \\w*ventil\\w* \\w*altera",
    "insuficiencia_ventilatoria": "insufi \\w* \\w*ventila|insufi\\w* \\w*respirat",
    "esforco_ventilatorio":"esforc \\w* \\w*ventila|esforc\\w* \\w*respirat",
    "lavado_broncoalveolar":"lavad\\w* \\w*broncoalv",
    "derrame_pleural":"derram\\w* \\w*pleur",
    "escherichia_coli":"escheric\\w* \\w*coli",
    "choque_septico":"choq\\w* \\w*septic",
    "dor_pleuritica":"dor\\w* \\w*pleur",
    "dor_ventilatorio_dependente": "dor\\w* \\w*ventil\\w* \\w*depend",
    "ventilacao_mecanica":"ventil\\w* \\w*mecan",
    "iot":"iot|intub\\w* \\w*orotraq|intub\\w* \\w*endotraq",
    "pav":"pav|",
    "endoftalmite":"pneum\\w* \\w*assoc\\w* \\w*ventil\\w* \\w*mecan",
    "eritema":"erite",
    "hiperemia":"hiperemi",
    "mediastinite":"mediastini",
    "staphylococcus_coagulase_negativo":"staphylococcus coagulase neg",
    "supuracao":"supur",
    "rubor":"rubo",
    "mal_estar": "mal\\w* \\w*estar",
    "abscesso":"absces",
    "calor":"calor",
    "dreno":"dren",
    "edema":"edema",
    "endocardite":"endocardit",
    "antibiotico":"antibiot",
    "bacteriologico":"bacteriologia|bacteriologic|cultura",
    "deiscencia":"deisc",
    "resistente":"resisten",
    "taquicardia":"taquic",
    "cateter":"cateter",
    "cateter_arterial": "cateter\\w* \\w*arterial",
    "cateter_urinario":"cateter\\w* \\w*urinar",
    "cvc":"cvc|cateter\\w* \\w*venos\\w* \\w*centr",
    "cateter_venoso_periferico":"cateter\\w* \\w*venos\\w* \\w*perif",
    "clorose":"clorose",
    "instabilidade":"instab",
    "oliguria":"oligur",
    "hipotensao":"hipotens",
    "anuria":"anur",
    "bacteremia":"bactere",
    "bacteriuria":"bacteriu",
    "disuria": "disur|urodi",
    "leucocituria":"leucocitu",
    "nitrito":"nitrit|azotit",
    "svd":"svd|sond\\w* \\w*vesic\\w* \\w*demor",
    "tsa":"tsa|test\\w* \\w*sensib",
    "choque":"choq",
    "staphylococcus":"staphylococcus",
    "e_coli":"e coli",
    "colecao":"coleca",
    "tremor":"tremor|tremendo",
    "calafrio":"calafr",
    "pos_operatorio":"operato",
    "dor_suprapubica":"dor\\w* \\w*suprapu",
    "foco_urinario": "foco\\w* \\w*urinari",
    "colite_pseudomembranosa":"colit\\w* \\w*pseudome",
    "yersinia":"yersini",
    "vomito":"vomit",
    "shigella":"shigel",
    "salmonela":"salmonel",
    "nausea":"nause",
    "giardia":"giard",
    "dor_cabeca":"dor\\w* \\w*cabec|dor\\w* \\w*de\\w* \\w*cabec",
    "dor_abdominal":"dor\\w* \\w*abdom",
    "diarreia":"diarr",
    "clostridium":"clostridi|colite\\w* \\w*(pseudo)?membranos",
    "campylobacter": "campylob",
    "urgencia_urinaria":"urgenc\\w* \\w*urinari",
    "urgencia_miccional": "urgenc\\w* \\w*mic",
    "sondagem_alivio":"sondag\\w* \\w*alivio",
    "sondagem_vesical":"sondag\\w* \\w*vesic",
    "urocultura":"urocu",
    "piuria":"piuri",
    "albumina":"albumina",
    "press_parc_co2":"press\\w* \\w*gas\\w* \\w*carbonic|press\\w* \\w*co2|arter\\w* \\w*pco|paco2|pco2",
    "bicarbonato":"bicarbonat",
    "calcio": "calci",
    "creatinina":"creatini",
    "glicose":"glicos",
    "hemoglobina":"hemoglobina",
    "plaquetas":"plaqueta|plaquetop|trombocitop",
    "potassio":"potassio",
    "sodio":"sodio",
    "bilirrubina":"bilirrubin",
    "cardiomegalia":"cardiomeg",
    "lesao_pulmonar":"lesao\\w* \\w*pulmon",
    "pneumonia":"pneumon|pnm",
    "atelectasia":"atelect",
    "pneumotorax":"pneumotor",
    "fratura":"fratu",
    "freq_respiratoria":"freq\\w* \\w*respirat",
    "freq_cardiaca":"freq\\w* \\w*cardiac",
    "pressao_sanguinea":"pressao\\w* \\w*sanguin|sistoli|diastoli",
    "saturacao_sangue":"saturac\\w* \\w*sangu",
    "hemocultura":"hemocu",
    "temperatura":"temperat",
    "ph_sangue":"ph\\w* \\w*sangu\\w* \\w*alterad|ph\\w* \\w*sangu\\w* \\w*anormal|altera\\w* \\w*ph\\w* \\w*sangu",
    "propionibacterium":"cutib\\w* \\w*acne|propionib\\w* \\w*acne|cutibac|propionibac",
    "cryptococcus":"cryptococcus",
    "pneumocystis":"pneumocystis",
    "histoplasma":"histoplasm",
    "paracoccidioides":"paracoccidioides",
    "bacteroides":"bacteroides",
    "candida":"candid",
    "fusobacterium":"fusobacter",
    "peptostreptococcus":"peptostreptococcus",
    "sibilancia":"sibil",
    "hipotermia":"hipotermia",
    "apneia":"apneia",
    "bradicardia":"bradicardi",
    "streptococcus_viridans":"streptococcus viridans",
    "consciencia":"consci",
    "hcm":"hcm",
    "hgm":"hemoglob\\w* \\w*corpusc\\w* \\w*med",
    "corynebacterium":"corynebacterium",
    "bacillus":"bacillus",
    "aerococcus":"aerococcus",
    "coccidioides":"coccidioides",
    "veillonella":"veillonella",
    "covid":"covid",
    "peep":"peep",
    "fio2":"fio2|fio²",
    "spo2":"spo2|spo²",
    "pcr_covid":"pcr\\w* \\w*covid",
    "avc":"avc|ave|aciden\\w* \\w*vasc\\w* \\w*cereb|aciden\\w* \\w*vasc\\w* \\w*encef",
    "sne":"sne|sond\\w* \\w*naso\\w* \\w*enter",
    "desnutricao":"desnutri|emagrecim",
    "sedacao":"sedac|sedad",
    "vsg":"vsg|veloc\\w* \\w*sediment\\w* \\w*glob|veloc\\w* \\w*hemossedim",
    "fosfatase_alcalina":"fosfat\\w* \\w*alcal",
    "ldh":"ldh|lactat\\w* \\w*desidrog",
    "cetamina":"cetamin|ketamin",
    "propofol":"propofol",
    "clorpromazina":"clorpromazina",
    "fentanil":"fentanil",
    "pancuronio":"pancuronio",
    "noradrenalina":"noradrenalina",
    "diazepan":"diazepan",
    "lorazepan":"lorazepa",
    "flumazenil":"flumazenil",
    "clonidina":"clonidina",
    "npt":"npt",
    "cateter_monolumen":"cml|catet\\w* \\w*mono\\w* \\w*lumen",
    "cateter_duplolumen":"cdl|catet\\w* \\w*dupl\\w* \\w*lumen",
    "cateter_triplolumen":"ctl|catet\\w* \\w*tripl\\w* \\w*lumen",
    "portocath":"portocath|port\\w* \\w*cath",
    "cateter_hickmann":"catet\\w* \\w*hickman",
    "shilley":"shilley",
    "obesidade":"obeso|obesid",
    "diabetes":"diabet",
    "neutropenia":"neutropeni",
    "tabagismo":"tabagis"
}

# Cache por processo worker: os padrões são compilados uma única vez (não a cada chunk),
# já que o Pool reutiliza os mesmos processos entre chamadas de imap_unordered().
# Só entram aqui os critérios que também têm rótulo em _VALUES_MAP -- os demais nunca
# apareciam em termos_achados mesmo na versão anterior (tabela larga), então pular seu
# casamento aqui não muda o resultado.
_criterios_compilados_cache = None


def _criterios_compilados():
    global _criterios_compilados_cache
    if _criterios_compilados_cache is None:
        compilados = []
        for cri in maestro.CRITERIOS_INTERFACE:
            rotulo = _VALUES_MAP.get(cri)
            if rotulo is None:
                continue
            pattern_pos_raw, pattern_neg_raw = regexPattern.regex_search(cri)
            pattern_pos_re, pos_sanitized = maestro._compile_sanitized(pattern_pos_raw)
            pattern_neg_re, neg_sanitized = maestro._compile_sanitized(pattern_neg_raw)
            compilados.append((rotulo, pattern_pos_re, pos_sanitized, pattern_neg_re, neg_sanitized))
        _criterios_compilados_cache = compilados
    return _criterios_compilados_cache


def _matches_por_criterio(new_sentence: pd.Series, pattern_pos_re, pos_sanitized: bool, pattern_neg_re, neg_sanitized: bool) -> list[list[str]]:
    """Mesma extração pos-menos-neg de maestro.operando_vetorizado_re_sanatized, só que devolvida
    direto (sem virar coluna) para o chamador decidir o que fazer com o resultado por linha."""
    all_pos = new_sentence.str.findall(pattern_pos_re)

    if pos_sanitized:
        all_pos_filtered = all_pos.tolist()
    else:
        all_pos_filtered = []
        for lst in all_pos:
            if not lst:
                all_pos_filtered.append([])
                continue
            all_pos_filtered.append([
                maestro._first_non_none_from_tuple(item) if isinstance(item, tuple) else item
                for item in lst
            ])

    final_pos = []
    for pos_list in all_pos_filtered:
        if not pos_list:
            final_pos.append([])
            continue
        negs = set()
        for p in pos_list:
            s = p if isinstance(p, str) else ""
            found = pattern_neg_re.findall(s)
            if neg_sanitized:
                negs.update(found)
            else:
                negs.update(
                    maestro._first_non_none_from_tuple(m) if isinstance(m, tuple) else m
                    for m in found
                )
        final_pos.append([x for x in pos_list if x not in negs])

    return final_pos


def main(c: pd.DataFrame) -> None:
    # Preparo de texto (igual ao antigo compute_evol_sent_pos_2_unique.py)
    c["new_sentence"] = c["new_sentence"].str.encode("ascii", "ignore")
    c["new_sentence"] = c["new_sentence"].str.decode("utf-8")
    c["new_sentence"] = c["new_sentence"].apply(
        lambda x: maestro.split_sentences(str(x) if not isinstance(x, str) else x)
    ).astype(str)

    # Casamento por critério, acumulando direto em duas listas por linha em vez de
    # criar uma coluna por critério (~190 colunas, na maioria vazias, que antes eram
    # gravadas em imparare2_evol_joined_original só para serem relidas e colapsadas aqui).
    termos_achados_por_linha: list[list[str]] = [[] for _ in range(len(c))]
    frases_por_linha: list[list[str]] = [[] for _ in range(len(c))]

    for rotulo, pattern_pos_re, pos_sanitized, pattern_neg_re, neg_sanitized in _criterios_compilados():
        final_pos = _matches_por_criterio(c["new_sentence"], pattern_pos_re, pos_sanitized, pattern_neg_re, neg_sanitized)
        for i, hits in enumerate(final_pos):
            if hits:
                termos_achados_por_linha[i].append(rotulo)
                # o match inclui as aspas delimitadoras do repr de new_sentence (ex: "'texto'") --
                # removidas aqui pra sobrar só o trecho da frase, como no pipeline anterior
                frases_por_linha[i].extend(h.strip("'") for h in hits)

    c["termos_achados"] = (
        pd.Series(termos_achados_por_linha, index=c.index).astype(str).str.replace("[]", "", regex=False)
    )

    c["dthr_evolucao_hr"] = c["dthr_evolucao"]
    c["dthr_evolucao"] = pd.to_datetime(c["dthr_evolucao"], utc=False)

    try:
        c["texto_evolucao"] = c["texto_evolucao"].apply(lambda x: urllib.parse.quote(str(x)))
        c["texto_evolucao"] = c["texto_evolucao"].apply(lambda x: urllib.parse.unquote(str(x)))
    except Exception:
        print("bug")

    try:
        c["texto_evolucao"] = c["texto_evolucao"].apply(lambda x: str.encode(str(x)))
    except Exception:
        print("bug2")

    c["texto_evolucao"] = c["texto_evolucao"].replace("/&lt;/g", "<")
    c["texto_evolucao"] = c["texto_evolucao"].replace("/&gt;/g", ">")
    c["texto_evolucao"] = c["texto_evolucao"].replace('/&quot;/g', '"')
    c["texto_evolucao"] = c["texto_evolucao"].replace("/&#39;/g", "'")
    c["texto_evolucao"] = c["texto_evolucao"].replace("/&amp;/g", "&")
    c["texto_evolucao"] = c["texto_evolucao"].astype("str").str.strip()

    hour_part = (
        c["dthr_evolucao_hr"]
        .astype(str)
        .str.replace("+", " ", regex=False)
        .str.split()
        .str[1]
    )
    c["texto_evolucao"] = "[" + c["perfil"].astype(str) + "] " + hour_part + " \n" + c["texto_evolucao"].astype(str) + " \n"

    # perfil_termos: mostra a(s) frase(s) originais que geraram os achados (não o rótulo
    # do regex), para leitura humana -- construído direto de frases_por_linha, sem passar
    # pela string-surgery que existia na versão anterior.
    frases_join = ["/*".join(f) for f in frases_por_linha]
    c["perfil_termos"] = "[" + c["perfil"].astype(str) + "] " + hour_part + "/*" + pd.Series(frases_join, index=c.index)
    c["perfil_termos"] = c["perfil_termos"].fillna("")

    c = c[[
        "registro",
        "dthr_evolucao",
        "dthr_evolucao_hr",
        "texto_evolucao",
        "termos_achados",
        "perfil_termos",
    ]]

    c = maestro.split_columns_count_vectorized(
        df=c,
        arrayDeReferencia=["dthr_evolucao"],
        arraySeparadores=[" "],
        maxColumnsToSplit=2,
    )

    # Zera hora/min/seg mantendo só a data
    c["dthr_evolucao"] = c["dthr_evolucao"].dt.normalize()

    c = maestro.concatenate_columns(
        df=c,
        arrayDestinos=["dthr_evolucao"],
        arrayDeReferencias=[["dthr_evolucao_0", "dthr_evolucao_1"]],
        arraySeparadores=[" "],
    )

    c = maestro.remove_columns(df=c, arrayColumns=["dthr_evolucao_0", "dthr_evolucao_1"])

    c = maestro.replace_values_list(
        df=c,
        arrayColumns=["perfil_termos", "termos_achados", "texto_evolucao"],
        arrayDeTuplas=[("None", "")],
    )

    dataRequest.set_data_on_sql(
        df=c,
        nomeTabelaDestino="imparare2_evol_sent_pos_joined_prepared",
        if_exists="append",
    )
