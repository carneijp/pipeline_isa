def regex_search(c):

    pattern_pos_pneumatose = r"(\'[^\']*\spneumato[^\']*\')"
    pattern_neg_pneumatose = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')"
    )
    if c == "pneumatose":
        return pattern_pos_pneumatose, pattern_neg_pneumatose

    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença
    pattern_pos_ronco = r"(\'[^\']*\sronc[^\']*\')|" r"(\'[^\']*estert[^\']*\')"
    pattern_neg_ronco = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\sronc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\sronc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\sronc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\sronc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*estert[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*estert[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*estert[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*estert[^\']*\')"
    )

    if c == "ronco":
        return pattern_pos_ronco, pattern_neg_ronco

    pattern_pos_tosse = (
        r"(\'[^\']*tosse[^\']*\')|"
        r"(\'[^\']*dispn[^\']*\')|"
        r"(\'[^\']*taquip[^\']*\')"
    )

    pattern_neg_tosse = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tosse[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tosse[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*toss[^\']*\')|"
        r"(\'[^\']*ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*toss[^\']*\')|"
        r"(\'[^\']*toss[^\']*ausen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dispn[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dispn[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dispn[^\']*\')|"
        r"(\'[^\']*ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dispn[^\']*\')|"
        r"(\'[^\']*dispn[^\']*ausen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquip[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquip[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquip[^\']*\')|"
        r"(\'[^\']*ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquip[^\']*\')|"
        r"(\'[^\']*taquip[^\']*ausen[^\']*\')"
    )

    if c == "tosse":
        return pattern_pos_tosse, pattern_neg_tosse

    pattern_pos_cavita = r"(\'[^\']*cavita[^\']*\')"
    pattern_neg_cavita = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cavita[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cavita[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cavita[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cavita[^\']*\')"
    )

    if c == "cavita":
        return pattern_pos_cavita, pattern_neg_cavita

    pattern_pos_opac = r"(\'[^\']*opac[^\']*\')"
    pattern_neg_opac = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*opac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*opac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*opac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*opac[^\']*\')"
    )

    if c == "opac":
        return pattern_pos_opac, pattern_neg_opac

    pattern_pos_infil = r"(\'[^\']*infil[^\']*\')"
    pattern_neg_infil = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infil[^\']*\')"
    )

    if c == "infil":
        return pattern_pos_infil, pattern_neg_infil

    pattern_pos_fibrose_cistica = "('[^']*fibr[^']{1,50}cistica[^']*')"
    pattern_neg_fibrose_cistica = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)fibr[^\']{1,50}cistica[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fibr((?!\'|com\s).){1,50}cistica[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fibr[^\']{1,50}cistica[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fibr((?!\'|com\s).){1,50}cistica[^\']*\')"
    )

    if c == "fibrose_cistica":
        return pattern_pos_fibrose_cistica, pattern_neg_fibrose_cistica

    pattern_pos_sec_pur_pulmonar = (
        r"(\'[^\']*puru[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*secrec[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*mucopurul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])escarr[^\']*\')|"
        r"(\'[^\']*hematopuru[^\']*\')|"
        r"(\'[^\']*via[^\']{1,50}aer[^\']*\')"
    )
    pattern_neg_sec_pur_pulmonar = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*puru[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mucopurul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])escarr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hematopuru[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*via[^\']{1,50}aer[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*puru[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mucopurul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])escarr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hematopuru[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*via((?!\'|com\s).){1,50}aer[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*puru[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec[^\']{1,50}resp[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])escarr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hematopuru[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*via[^\']{1,50}aer[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mucopurul[^\']*\')"
    )

    if c == "sec_pur_pulmonar":
        return pattern_pos_sec_pur_pulmonar, pattern_neg_sec_pur_pulmonar

    pattern_pos_secr_traq = r"(\'[^\']*secrec[^\']{1,50}traq[^\']*\')"
    pattern_neg_secr_traq = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec((?!\'|com\s).){1,50}traq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec((?!\'|com\s).){1,50}traq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec((?!\'|com\s).){1,50}traq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec((?!\'|com\s).){1,50}traq[^\']*\')"
    )

    if c == "secr_traq":
        return pattern_pos_secr_traq, pattern_neg_secr_traq

    pattern_pos_secr = r"(\'[^\']*secrec[^\']*\')"
    pattern_neg_secr = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*secrec[^\']*\')"
    )

    if c == "secr":
        return pattern_pos_secr, pattern_neg_secr

    pattern_pos_puru = r"(\'[^\']*purul[^\']*\')"
    pattern_neg_puru = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*purul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*purul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*purul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*purul[^\']*\')"
    )

    if c == "puru":
        return pattern_pos_puru, pattern_neg_puru

    pattern_pos_dpoc = (
        r"(\'[^\']*dpoc[^\']*\')|"
        r"(\'[^\']*doen[^\']{1,50}pulm[^\']{1,50}obst[^\']{1,50}cr[^\']*\')"
    )
    pattern_neg_dpoc = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dpoc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dpoc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dpoc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dpoc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*doen((?!\'|com\s).){1,50}pulm((?!\'|com\s).){1,50}obst((?!\'|com\s).){1,50}cr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*doen((?!\'|com\s).){1,50}pulm((?!\'|com\s).){1,50}obst((?!\'|com\s).){1,50}cr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*doen[^\']{1,50}pulm[^\']{1,50}obst[^\']{1,50}cr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*doen((?!\'|com\s).){1,50}pulm((?!\'|com\s).){1,50}obst((?!\'|com\s).){1,50}cr[^\']*\')"
    )

    if c == "dpoc":
        return pattern_pos_dpoc, pattern_neg_dpoc

    pattern_pos_hemoptise = r"(\'[^\']*hemopt[^\']*\')"
    pattern_neg_hemoptise = (
        r"(\'[^\']*(?<![a-z])se(?![a-z])[^\']{1,50}hemopt[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemopt[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemopt[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemopt[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemopt[^\']*\')"
    )

    if c == "hemoptise":
        return pattern_pos_hemoptise, pattern_neg_hemoptise

    pattern_pos_leucemia = (
        r"(\'[^\']*leuce[^\']*\')|"
        r"(\'[^\']* cid(.?)90(\d?)[^\']*\')|"
        r"(\'[^\']* cid(.?)91.*\d[^\']*\')|"
        r"(\'[^\']* cid(.?)92.*\d[^\']*\')|"
        r"(\'[^\']* cid(.?)93.*\d[^\']*\')|"
        r"(\'[^\']* cid(.?)94.*\d[^\']*\')|"
        r"(\'[^\']* cid(.?)95.*\d[^\']*\')|"
        r"(\'[^\']* cid(.?)96.*\d[^\']*\')"
    )
    pattern_neg_leucemia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuce[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuce[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuce[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuce[^\']*\')"
    )

    if c == "leucemia":
        return pattern_pos_leucemia, pattern_neg_leucemia

    pattern_pos_esplenectomia = r"(\'[^\']*esplenec[^\']*\')"
    pattern_neg_esplenectomia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esplenec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esplenec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esplenec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esplenec[^\']*\')"
    )

    if c == "esplenectomia":
        return pattern_pos_esplenectomia, pattern_neg_esplenectomia

    pattern_pos_febre = r"(\'[^\']*febr[^\']*\')"
    pattern_neg_febre = (
        r"(\'[^\']*(?<![a-z])se(?![a-z])[^\']{1,50}febr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*febr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*febr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*febr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*febr[^\']*\')|"
        r"(\'[^\']*afebr[^\']*\')"
    )

    if c == "febre":
        return pattern_pos_febre, pattern_neg_febre

    pattern_pos_consol = r"(\'[^\']*consol[^\']*\')"
    pattern_neg_consol = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consol[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consol[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consol[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consol[^\']*\')"
    )

    if c == "consol":
        return pattern_pos_consol, pattern_neg_consol

    pattern_pos_linfoma = (
        r"(\'[^\']*linfoma[^\']*\')|"
        r"(\'[^\']*\scid(.?)81(\d?)[^\']*\')|"
        r"(\'[^\']*\scid(.?)82.*\d[^\']*\')|"
        r"(\'[^\']*\scid(.?)83.*\d[^\']*\')|"
        r"(\'[^\']*\scid(.?)84.*\d[^\']*\')|"
        r"(\'[^\']*\scid(.?)85.*\d[^\']*\')"
    )
    pattern_neg_linfoma = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*linfoma[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*linfoma[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*linfoma[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*linfoma[^\']*\')"
    )

    if c == "linfoma":
        return pattern_pos_linfoma, pattern_neg_linfoma

    pattern_pos_o2 = (
        r"(\'[^\']*o2[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*ox[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*o²[^\']{1,50}\s\dl[^\']*\')"
    )
    pattern_neg_o2 = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o2[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ox[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o²[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o2[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ox[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o²[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o2[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ox[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o²[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o2[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ox[^\']{1,50}\s\dl[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*o²[^\']{1,50}\s\dl[^\']*\')"
    )

    if c == "o2":
        return pattern_pos_o2, pattern_neg_o2
    
    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença
    pattern_pos_acinetobacter = r"(\'[^\']*acinetobac[^\']*\')"
    pattern_neg_acinetobacter = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*acinetobac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*acinetobac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*acinetobac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*acinetobac[^\']*\')"
    )

    if c == "acinetobacter":
        return pattern_pos_acinetobacter, pattern_neg_acinetobacter

    pattern_pos_amarelada = r"(\'[^\']*amarel[^\']*\')"
    pattern_neg_amarelada = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*amarel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*amarel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*amarel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*amarel[^\']*\')"
    )

    if c == "amarelada":
        return pattern_pos_amarelada, pattern_neg_amarelada

    pattern_pos_aspiracao = r"(\'[^\']*(?<![a-z])aspira[^\']*\')"
    pattern_neg_aspiracao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])aspira[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])aspira[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])aspira[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])aspira[^\']*\')"
    )

    if c == "aspiracao":
        return pattern_pos_aspiracao, pattern_neg_aspiracao

    pattern_pos_broncograma_aereo = r"(\'[^\']*broncog[^\']{1,50}aere[^\']*\')"
    pattern_neg_broncograma_aereo = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*broncog[^\']{1,50}aere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*broncog[^\']{1,50}aere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*broncog[^\']{1,50}aere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*broncog[^\']{1,50}aere[^\']*\')"
    )

    if c == "broncograma_aereo":
        return pattern_pos_broncograma_aereo, pattern_neg_broncograma_aereo

    pattern_pos_crepitante = r"(\'[^\']*crepit[^\']*\')"
    pattern_neg_crepitante = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*crepit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*crepit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*crepit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*crepit[^\']*\')"
    )

    if c == "crepitante":
        return pattern_pos_crepitante, pattern_neg_crepitante

    pattern_pos_enterobacter = r"(\'[^\']*enterobac[^\']*\')"
    pattern_neg_enterobacter = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterobac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterobac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterobac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterobac[^\']*\')"
    )

    if c == "enterobacter":
        return pattern_pos_enterobacter, pattern_neg_enterobacter

    pattern_pos_enterococcus = r"(\'[^\']*enterococ[^\']*\')"
    pattern_neg_enterococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterococ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterococ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterococ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*enterococ[^\']*\')"
    )

    if c == "enterococcus":
        return pattern_pos_enterococcus, pattern_neg_enterococcus

    pattern_pos_hemophylus = r"(\'[^\']*hemoph[^\']*\')|" r"(\'[^\']*haemoph[^\']*\')"
    pattern_neg_hemophylus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*haemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*haemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*haemoph[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*haemoph[^\']*\')"
    )

    if c == "hemophylus":
        return pattern_pos_hemophylus, pattern_neg_hemophylus

    pattern_pos_hipertermia = r"(\'[^\']*hiperter[^\']*\')"
    pattern_neg_hipertermia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperter[^\']*\')"
    )

    if c == "hipertermia":
        return pattern_pos_hipertermia, pattern_neg_hipertermia

    pattern_pos_imunossuprimido = r"(\'[^\']*imunossup[^\']*\')"
    pattern_neg_imunossuprimido = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*imunossup[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*imunossup[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*imunossup[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*imunossup[^\']*\')"
    )

    if c == "imunossuprimido":
        return pattern_pos_imunossuprimido, pattern_neg_imunossuprimido

    pattern_pos_infeccao = r"(\'[^\']*infec[^\']*\')"
    pattern_neg_infeccao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*infec[^\']*\')"
    )

    if c == "infeccao":
        return pattern_pos_infeccao, pattern_neg_infeccao

    pattern_pos_klebsiella = r"(\'[^\']*klebsiel[^\']*\')|" r"(\'[^\']*kpc[^\']*\')"
    pattern_neg_klebsiella = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*klebsiel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*klebsiel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*klebsiel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*klebsiel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*kpc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*kpc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*kpc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*kpc[^\']*\')"
    )

    if c == "klebsiella":
        return pattern_pos_klebsiella, pattern_neg_klebsiella

    pattern_pos_legionella = r"(\'[^\']*legionel[^\']*\')"
    pattern_neg_legionella = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*legionel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*legionel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*legionel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*legionel[^\']*\')"
    )

    if c == "legionella":
        return pattern_pos_legionella, pattern_neg_legionella

    pattern_pos_leucocitose = r"(\'[^\']*leucocitose[^\']*\')"
    pattern_neg_leucocitose = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*\')"
    )

    if c == "leucocitose":
        return pattern_pos_leucocitose, pattern_neg_leucocitose

    pattern_pos_leucopenia = r"(\'[^\']*(leucopen|neutropen)[^\']*\')"
    pattern_neg_leucopenia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(leucopen|neutropen)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(leucopen|neutropen)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(leucopen|neutropen)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(leucopen|neutropen)[^\']*\')"
    )

    if c == "leucopenia":
        return pattern_pos_leucopenia, pattern_neg_leucopenia

    pattern_pos_moraxella = r"(\'[^\']*moraxel[^\']*\')"
    pattern_neg_moraxella = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*moraxel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*moraxel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*moraxel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*moraxel[^\']*\')"
    )

    if c == "moraxella":
        return pattern_pos_moraxella, pattern_neg_moraxella

    pattern_pos_pneumococcus = r"(\'[^\']*pneumococ[^\']*\')"
    pattern_neg_pneumococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumococ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumococ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumococ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumococ[^\']*\')"
    )

    if c == "pneumococcus":
        return pattern_pos_pneumococcus, pattern_neg_pneumococcus

    pattern_pos_pseudomonas = r"(\'[^\']*pseudomon[^\']*\')"
    pattern_neg_pseudomonas = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pseudomon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pseudomon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pseudomon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pseudomon[^\']*\')"
    )

    if c == "pseudomonas":
        return pattern_pos_pseudomonas, pattern_neg_pseudomonas

    pattern_pos_sibilos = r"(\'[^\']*sibilo[^\']*\')"
    pattern_neg_sibilos = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibilo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibilo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibilo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibilo[^\']*\')"
    )

    if c == "sibilos":
        return pattern_pos_sibilos, pattern_neg_sibilos

    pattern_pos_intubacao = r"(\'[^\']*intub[^\']*\')"
    pattern_neg_intubacao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']*\')"
    )

    if c == "intubacao":
        return pattern_pos_intubacao, pattern_neg_intubacao

        # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença
    pattern_pos_staphylococcus_aureus = (
        r"(\'[^\']*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}aure[^\']*\')"
    )
    pattern_neg_staphylococcus_aureus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}aure[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}aure[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}aure[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}aure[^\']*\')"
    )

    if c == "staphylococcus_aureus":
        return pattern_pos_staphylococcus_aureus, pattern_neg_staphylococcus_aureus

    pattern_pos_sepse_pulmonar = r"(\'[^\']*sepse[^\']{1,50}pulmon[^\']*\')"
    pattern_neg_sepse_pulmonar = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}pulmon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}pulmon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}pulmon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}pulmon[^\']*\')"
    )

    if c == "sepse_pulmonar":
        return pattern_pos_sepse_pulmonar, pattern_neg_sepse_pulmonar

    pattern_pos_sepse_respiratoria = r"(\'[^\']*sepse[^\']{1,50}respir[^\']*\')"
    pattern_neg_sepse_respiratoria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}respir[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}respir[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}respir[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}respir[^\']*\')"
    )

    if c == "sepse_respiratoria":
        return pattern_pos_sepse_respiratoria, pattern_neg_sepse_respiratoria

    pattern_pos_sepse_urinaria = r"(\'[^\']*sepse[^\']{1,50}urinari[^\']*\')"
    pattern_neg_sepse_urinaria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sepse[^\']{1,50}urinari[^\']*\')"
    )

    if c == "sepse_urinaria":
        return pattern_pos_sepse_urinaria, pattern_neg_sepse_urinaria

    pattern_pos_broncograma_aereo = r"(\'[^\']*bronco[^\']{1,50}aere[^\']*\')"
    pattern_neg_broncograma_aereo = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bronco[^\']{1,50}aere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bronco[^\']{1,50}aere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bronco[^\']{1,50}aere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bronco[^\']{1,50}aere[^\']*\')"
    )

    if c == "broncograma_aereo":
        return pattern_pos_broncograma_aereo, pattern_neg_broncograma_aereo

    pattern_pos_insuficiencia_ventilatoria = (
        r"(\'[^\']*insufi[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*insufi[^\']{1,50}respirat[^\']*\')"
    )
    pattern_neg_insuficiencia_ventilatoria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*insufi[^\']{1,50}respirat[^\']*\')"
    )

    if c == "insuficiencia_ventilatoria":
        return (
            pattern_pos_insuficiencia_ventilatoria,
            pattern_neg_insuficiencia_ventilatoria,
        )

    pattern_pos_esforco_ventilatorio = (
        r"(\'[^\']*esforc[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*esforc[^\']{1,50}respirat[^\']*\')"
    )
    pattern_neg_esforco_ventilatorio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}ventila[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*esforc[^\']{1,50}respirat[^\']*\')"
    )

    if c == "esforco_ventilatorio":
        return pattern_pos_esforco_ventilatorio, pattern_neg_esforco_ventilatorio

    pattern_pos_lavado_broncoalveolar = r"(\'[^\']*lavad[^\']{1,50}broncoalv[^\']*\')"
    pattern_neg_lavado_broncoalveolar = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lavad[^\']{1,50}broncoalv[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lavad[^\']{1,50}broncoalv[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lavad[^\']{1,50}broncoalv[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lavad[^\']{1,50}broncoalv[^\']*\')"
    )

    if c == "lavado_broncoalveolar":
        return pattern_pos_lavado_broncoalveolar, pattern_neg_lavado_broncoalveolar

    pattern_pos_derrame_pleural = r"(\'[^\']*derram[^\']{1,50}pleur[^\']*\')"
    pattern_neg_derrame_pleural = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*derrame[^\']{1,50}pleur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*derrame[^\']{1,50}pleur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*derrame[^\']{1,50}pleur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*derrame[^\']{1,50}pleur[^\']*\')"
    )

    if c == "derrame_pleural":
        return pattern_pos_derrame_pleural, pattern_neg_derrame_pleural

    pattern_pos_escherichia_coli = r"(\'[^\']*escheric[^\']{1,50}coli[^\']*\')"
    pattern_neg_escherichia_coli = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*escheric[^\']{1,50}coli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*escheric[^\']{1,50}coli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*escheric[^\']{1,50}coli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*escheric[^\']{1,50}coli[^\']*\')"
    )

    if c == "escherichia_coli":
        return pattern_pos_escherichia_coli, pattern_neg_escherichia_coli

    pattern_pos_choque_septico = r"(\'[^\']*choq[^\']{1,50}septic[^\']*\')"
    pattern_neg_choque_septico = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']{1,50}septic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']{1,50}septic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']{1,50}septic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']{1,50}septic[^\']*\')"
    )

    if c == "choque_septico":
        return pattern_pos_choque_septico, pattern_neg_choque_septico

    pattern_pos_dor_pleuritica = (
        r"(\'[^\']*(?<![a-z])dor(?![a-z])[^\']{1,50}pleur[^\']*\')"
    )
    pattern_neg_dor_pleuritica = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}pleur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}pleur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}pleur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}pleur[^\']*\')"
    )

    if c == "dor_pleuritica":
        return pattern_pos_dor_pleuritica, pattern_neg_dor_pleuritica

    pattern_pos_dor_ventilatorio_dependente = (
        r"(\'[^\']*(?<![a-z])dor(?![a-z])[^\']{1,50}ventil[^\']{1,50}\sdepend[^\']*\')"
    )
    pattern_neg_dor_ventilatorio_dependente = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}ventil[^\']{1,50}\sdepend[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}ventil[^\']{1,50}\sdepend[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}ventil[^\']{1,50}\sdepend[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}ventil[^\']{1,50}\sdepend[^\']*\')"
    )

    if c == "dor_ventilatorio_dependente":
        return (
            pattern_pos_dor_ventilatorio_dependente,
            pattern_neg_dor_ventilatorio_dependente,
        )

    pattern_pos_pav = (
        r"(\'[^\']*(?<![a-z])pav(?![a-z])[^\']*\')|"
        r"(\'[^\']*pneum[^\']{1,50}assoc[^\']{1,50}ventil[^\']{1,50}\smecan[^\']*\')"
    )
    pattern_neg_pav = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pav(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pav(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pav(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pav(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneum[^\']{1,50}\sassoc[^\']{1,50}ventil[^\']{1,50}\smecan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneum[^\']{1,50}\sassoc[^\']{1,50}ventil[^\']{1,50}\smecan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneum[^\']{1,50}\sassoc[^\']{1,50}ventil[^\']{1,50}\smecan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneum[^\']{1,50}\sassoc[^\']{1,50}ventil[^\']{1,50}\smecan[^\']*\')"
    )

    if c == "pav":
        return pattern_pos_pav, pattern_neg_pav

    pattern_pos_ventilacao_mecanica = (
        r"(\'[^\']*(?<![a-z])vm(?![a-z])[^\']*\')|"
        r"(\'[^\']*ventil[^\']{1,50}mecan[^\']*\')"
    )
    pattern_neg_ventilacao_mecanica = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vm(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vm(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vm(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vm(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ventil[^\']{1,50}\smecan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ventil[^\']{1,50}\smecan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ventil[^\']{1,50}\smecan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ventil[^\']{1,50}\smecan[^\']*\')"
    )

    if c == "ventilacao_mecanica":
        return pattern_pos_ventilacao_mecanica, pattern_neg_ventilacao_mecanica

    pattern_pos_iot = (
        r"(\'[^\']*(?<![a-z])iot(?![a-z])[^\']*\')|"
        r"(\'[^\']*intub[^\']{1,50}orotraq[^\']*\')|"
        r"(\'[^\']*intub[^\']{1,50}endotraq[^\']*\')"
    )

    pattern_neg_iot = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])iot(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])iot(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])iot(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])iot(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}orotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}orotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}orotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}orotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}endotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}endotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}endotraq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intub[^\']{1,50}endotraq[^\']*\')"
    )

    if c == "iot":
        return pattern_pos_iot, pattern_neg_iot

    pattern_pos_padrao_ventilatorio = (
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*altera[^\']{1,50}padrao[^\']{1,50}ventil[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*altera[^\']{1,50}padrao[^\']{1,50}respi[^\']*\')|"
        r"(\'[^\']*mvud[^\']*\')"
    )
    pattern_neg_padrao_ventilatorio = (
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}normal[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}regul[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}estav[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}ventil[^\']{1,50}inalter[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}normal[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}regul[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}estav[^\']*\')|"
        r"(\'[^\']*padrao[^\']{1,50}respi[^\']{1,50}inalter[^\']*\')|"
        r"(\'[^\']*bom[^\']{1,50}padrao[^\']{1,50}ventil[^\']*\')|"
        r"(\'[^\']*bom[^\']{1,50}padrao[^\']{1,50}respi[^\']*\')|"
        r"(\'[^\']*mante[^\']{1,50}padrao[^\']{1,50}ventil[^\']*\')|"
        r"(\'[^\']*mante[^\']{1,50}padrao[^\']{1,50}respi[^\']*\')|"
        r"(\'[^\']*mvud[^a-z]{0,50}(?<![a-z]){0,50}sem[^a-z]{0,50}ra(?![a-z]){1,50}[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}padrao[^\']{1,50}respi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}padrao[^\']{1,50}ventil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mvud[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}padrao[^\']{1,50}respi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}padrao[^\']{1,50}ventil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mvud[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}ventil[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}altera[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}instav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}irreg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*padrao[^\']{1,50}respi[^\']{1,50}kuss[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}padrao[^\']{1,50}respi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}padrao[^\']{1,50}ventil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mvud[^\']*\')"
    )

    if c == "padrao_ventilatorio":
        return pattern_pos_padrao_ventilatorio, pattern_neg_padrao_ventilatorio

# todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença

    pattern_pos_endoftalmite = r"(\'[^\']*endoft[^\']*\')"
    pattern_neg_endoftalmite = (
        r"(\'[^\']*(?<![a-z])sem(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endoft[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endoft[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endoft[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endoft[^\']*\')"
    )

    if c == "endoftalmite":
        return pattern_pos_endoftalmite, pattern_neg_endoftalmite

    pattern_pos_eritema = r"(\'[^\']*erite[^\']*\')"
    pattern_neg_eritema = (
        r"(\'[^\']*(?<![a-z])sem(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*erite[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*erite[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*erite[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*erite[^\']*\')"
    )

    if c == "eritema":
        return pattern_pos_eritema, pattern_neg_eritema

    pattern_pos_hiperemia = r"(\'[^\']*hiperemi[^\']*\')"
    pattern_neg_hiperemia = (
        r"(\'[^\']*(?<![a-z])sem(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperemi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperemi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperemi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hiperemi[^\']*\')"
    )

    if c == "hiperemia":
        return pattern_pos_hiperemia, pattern_neg_hiperemia

    pattern_pos_mediastinite = r"(\'[^\']*mediastini[^\']*\')"
    pattern_neg_mediastinite = (
        r"(\'[^\']*(?<![a-z])sem(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mediastini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mediastini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mediastini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?<![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mediastini[^\']*\')"
    )

    if c == "mediastinite":
        return pattern_pos_mediastinite, pattern_neg_mediastinite

    pattern_pos_staphylococcus_coagulase_negativo = r"(\'[^\']*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}coagul[^\']{1,50}negat[^\']*\')"
    pattern_neg_staphylococcus_coagulase_negativo = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*staphylococ[^\']*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}coagul[^\']{1,50}negat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}coagul[^\']{1,50}negat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}coagul[^\']{1,50}negat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']{1,50}coagul[^\']{1,50}negat[^\']*\')"
    )

    if c == "staphylococcus_coagulase_negativo":
        return (
            pattern_pos_staphylococcus_coagulase_negativo,
            pattern_neg_staphylococcus_coagulase_negativo,
        )

    pattern_pos_supuracao = r"(\'[^\']*supur[^\']*\')"
    pattern_neg_supuracao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*supur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*supur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*supur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*supur[^\']*\')"
    )

    if c == "supuracao":
        return pattern_pos_supuracao, pattern_neg_supuracao

    pattern_pos_rubor = r"(\'[^\']*rubo[^\']*\')"
    pattern_neg_rubor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*rubo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*rubo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*rubo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*rubo[^\']*\')"
    )

    if c == "rubor":
        return pattern_pos_rubor, pattern_neg_rubor

    pattern_pos_mal_estar = r"(\'[^\']*mal[^\']{1,50}estar[^\']*\')"
    pattern_neg_mal_estar = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mal[^\']{1,50}estar[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mal[^\']{1,50}estar[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mal[^\']{1,50}estar[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*mal[^\']{1,50}estar[^\']*\')"
    )

    if c == "mal_estar":
        return pattern_pos_mal_estar, pattern_neg_mal_estar

    pattern_pos_abscesso = r"(\'[^\']*absces[^\']*\')"
    pattern_neg_abscesso = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*absces[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*absces[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*absces[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*absces[^\']*\')"
    )
    if c == "abscesso":
        return pattern_pos_abscesso, pattern_neg_abscesso

    pattern_pos_calor = r"(\'[^\']*calor[^\']*\')"
    pattern_neg_calor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calor[^\']*\')"
    )
    if c == "calor":
        return pattern_pos_calor, pattern_neg_calor

    pattern_pos_dreno = r"(\'[^\']*dren[^\']*\')"
    pattern_neg_dreno = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*\')|"
        r"(\'[^\']*(?<![a-z])imped((?!\'|com\s|,\srefere|,\sapresenta|,\smas,\sefet,\srealiz).)*dren[^\']*\')"
    )
    if c == "dreno":
        return pattern_pos_dreno, pattern_neg_dreno

    pattern_pos_edema = r"(\'[^\']*edema[^\']*\')"
    pattern_neg_edema = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*edema[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*edema[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*edema[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*edema[^\']*\')"
    )
    if c == "edema":
        return pattern_pos_edema, pattern_neg_edema

    pattern_pos_endocardite = r"(\'[^\']*endocardit[^\']*\')"
    pattern_neg_endocardite = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endocardit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endocardit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endocardit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*endocardit[^\']*\')"
    )
    if c == "endocardite":
        return pattern_pos_endocardite, pattern_neg_endocardite

    pattern_pos_antibiotico = r"(\'[^\']*antibiot[^\']*\')"
    pattern_neg_antibiotico = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*antibiot[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*antibiot[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*antibiot[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*antibiot[^\']*\')"
    )
    if c == "antibiotico":
        return pattern_pos_antibiotico, pattern_neg_antibiotico

    pattern_pos_bacteriologico = (
        r"(\'[^\']*bacteriologia[^\']*\')|"
        r"(\'[^\']*bacteriologic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])cultura[^\']*\')"
    )
    pattern_neg_bacteriologico = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriologic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cultura[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cultura[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cultura[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cultura[^\']*\')"
    )
    if c == "bacteriologico":
        return pattern_pos_bacteriologico, pattern_neg_bacteriologico

    pattern_pos_deiscencia = r"(\'[^\']*deisc[^\']*\')"
    pattern_neg_deiscencia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*deisc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*deisc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*deisc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*deisc[^\']*\')"
    )
    if c == "deiscencia":
        return pattern_pos_deiscencia, pattern_neg_deiscencia

    pattern_pos_resistente = r"(\'[^\']*resisten[^\']*\')"
    pattern_neg_resistente = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*resisten[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*resisten[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*resisten[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*resisten[^\']*\')"
    )
    if c == "resistente":
        return pattern_pos_resistente, pattern_neg_resistente

    pattern_pos_taquicardia = r"(\'[^\']*taquic[^\']*\')"
    pattern_neg_taquicardia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*taquic[^\']*\')"
    )
    if c == "taquicardia":
        return pattern_pos_taquicardia, pattern_neg_taquicardia



    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença
    pattern_pos_cateter = r"(\'[^\']*cateter[^\']*\')"
    pattern_neg_cateter = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']*\')"
    )

    if c == "cateter":
        return pattern_pos_cateter, pattern_neg_cateter

    pattern_pos_cateter_arterial = r"(\'[^\']*cateter[^\']{1,50}arterial[^\']*\')"
    pattern_neg_cateter_arterial = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}arterial[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}arterial[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}arterial[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}arterial[^\']*\')"
    )

    if c == "cateter_arterial":
        return pattern_pos_cateter_arterial, pattern_neg_cateter_arterial

    pattern_pos_cateter_urinario = r"(\'[^\']*cateter[^\']{1,50}urinar[^\']*\')"
    pattern_neg_cateter_urinario = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}urinar[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}urinar[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}urinar[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}urinar[^\']*\')"
    )

    if c == "cateter_urinario":
        return pattern_pos_cateter_urinario, pattern_neg_cateter_urinario

    pattern_pos_cvc = (
        r"(\'[^\']*cvc[^\']*\')|"
        r"(\'[^\']*cateter[^\']{1,50}venos[^\']{1,50}centr[^\']*\')"
    )
    pattern_neg_cvc = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cvc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cvc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cvc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cvc[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos[^\']{1,50}centr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos[^\']{1,50}centr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos[^\']{1,50}centr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos[^\']{1,50}centr[^\']*\')"
    )

    if c == "cvc":
        return pattern_pos_cvc, pattern_neg_cvc

    pattern_pos_cateter_venoso_periferico = (
        r"(\'[^\']*cateter[^\']{1,50}venos(?![^\']{1,50}perif)[^\']*\')"
    )
    pattern_neg_cateter_venoso_periferico = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos(?![^\']{1,50}perif)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos(?![^\']{1,50}perif)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos(?![^\']{1,50}perif)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cateter[^\']{1,50}venos(?![^\']{1,50}perif)[^\']*\')"
    )

    if c == "cateter_venoso_periferico":
        return (
            pattern_pos_cateter_venoso_periferico,
            pattern_neg_cateter_venoso_periferico,
        )

    pattern_pos_clorose = r"(\'[^\']*clorose[^\']*\')"
    pattern_neg_clorose = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorose[^\']*\')"
    )

    if c == "clorose":
        return pattern_pos_clorose, pattern_neg_clorose

    pattern_pos_instabilidade = r"(\'[^\']*instab[^\']*\')"
    pattern_neg_instabilidade = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*instab[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*instab[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*instab[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*instab[^\']*\')"
    )

    if c == "instabilidade":
        return pattern_pos_instabilidade, pattern_neg_instabilidade

    pattern_pos_oliguria = r"(\'[^\']*oligur[^\']*\')"
    pattern_neg_oliguria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*oligur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*oligur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*oligur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*oligur[^\']*\')"
    )

    if c == "oliguria":
        return pattern_pos_oliguria, pattern_neg_oliguria

    pattern_pos_hipotensao = r"(\'[^\']*hipotens[^\']*\')"
    pattern_neg_hipotensao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotens[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotens[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotens[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotens[^\']*\')"
    )

    if c == "hipotensao":
        return pattern_pos_hipotensao, pattern_neg_hipotensao

    pattern_pos_anuria = r"(\'[^\']*anur[^\']*\')"
    pattern_neg_anuria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*anur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*anur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*anur[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*anur[^\']*\')"
    )

    if c == "anuria":
        return pattern_pos_anuria, pattern_neg_anuria

    pattern_pos_bacteremia = r"(\'[^\']*bactere[^\']*\')"
    pattern_neg_bacteremia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bactere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bactere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bactere[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bactere[^\']*\')"
    )

    if c == "bacteremia":
        return pattern_pos_bacteremia, pattern_neg_bacteremia

    pattern_pos_bacteriuria = r"(\'[^\']*bacteriu[^\']*\')"
    pattern_neg_bacteriuria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriu[^\']*\')"
    )

    if c == "bacteriuria":
        return pattern_pos_bacteriuria, pattern_neg_bacteriuria

    pattern_pos_disuria = r"(\'[^\']*(disur|urodi)[^\']*\')"
    pattern_neg_disuria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(disur|urodi)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(disur|urodi)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(disur|urodi)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(disur|urodi)[^\']*\')"
    )

    if c == "disuria":
        return pattern_pos_disuria, pattern_neg_disuria

    pattern_pos_leucocituria = r"(\'[^\']*leucocitu[^\']*\')"
    pattern_neg_leucocituria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitu[^\']*\')"
    )

    if c == "leucocituria":
        return pattern_pos_leucocituria, pattern_neg_leucocituria

    pattern_pos_nitrito = r"(\'[^\']*nitrit[^\']*\')|" r"(\'[^\']*azotit[^\']*\')"
    pattern_neg_nitrito = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nitrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nitrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nitrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nitrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*azotit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*azotit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*azotit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*azotit[^\']*\')"
    )

    if c == "nitrito":
        return pattern_pos_nitrito, pattern_neg_nitrito

    pattern_pos_svd = (
        r"(\'[^\']*svd[^\']*\')|"
        r"(\'[^\']*sond[^\']{1,50}vesic[^\']{1,50}demor[^\']*\')"
    )
    pattern_neg_svd = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*svd[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*svd[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*svd[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*svd[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']{1,50}vesic[^\']{1,50}demor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']{1,50}vesic[^\']{1,50}demor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']{1,50}vesic[^\']{1,50}demor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']{1,50}vesic[^\']{1,50}demor[^\']*\')"
    )

    if c == "svd":
        return pattern_pos_svd, pattern_neg_svd

    pattern_pos_tsa = (
        r"(\'[^\']*tsa[^\']*\')|" r"(\'[^\']*test[^\']{1,50}sensib[^\']*\')"
    )
    pattern_neg_tsa = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tsa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tsa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tsa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tsa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*test[^\']{1,50}sensib[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*test[^\']{1,50}sensib[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*test[^\']{1,50}sensib[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*test[^\']{1,50}sensib[^\']*\')"
    )

    if c == "tsa":
        return pattern_pos_tsa, pattern_neg_tsa

    pattern_pos_choque = r"(\'[^\']*choq[^\']*\')"
    pattern_neg_choque = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*choq[^\']*\')"
    )

    if c == "choque":
        return pattern_pos_choque, pattern_neg_choque

    pattern_pos_staphylococcus = (
        r"(\'[^\']*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']*\')"
    )
    pattern_neg_staphylococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((e)?sta(ph|f)(i|y)lococ(c)?(o|u)?(s)?)[^\']*\')"
    )

    if c == "staphylococcus":
        return pattern_pos_staphylococcus, pattern_neg_staphylococcus

    pattern_pos_e_coli = r"(\'[^\']*e(\.|\s|s(ch|c)er)[^\']{1,50}coli(?![a-z])[^\']*\')"  # se não funcionar, inserir (?!(.{0,5})) ao invés de [^\'] em "...*e(\.|\s|s(ch|c)er)[^\']*coli..."
    pattern_neg_e_coli = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*e(\.|\s|s(ch|c)er)[^\']{1,50}coli(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*e(\.|\s|s(ch|c)er)[^\']{1,50}coli(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*e(\.|\s|s(ch|c)er)[^\']{1,50}coli(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*e(\.|\s|s(ch|c)er)[^\']{1,50}coli(?![a-z])[^\']*\')"
    )

    if c == "e_coli":
        return pattern_pos_e_coli, pattern_neg_e_coli

    pattern_pos_colecao = r"(\'[^\']*coleca[^\']*\')"
    pattern_neg_colecao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coleca[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coleca[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coleca[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coleca[^\']*\')"
    )

    if c == "colecao":
        return pattern_pos_colecao, pattern_neg_colecao

    pattern_pos_tremor = r"(\'[^\']*tremor[^\']*\')|" r"(\'[^\']*tremendo[^\']*\')"
    pattern_neg_tremor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremendo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremendo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremendo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tremendo[^\']*\')"
    )

    if c == "tremor":
        return pattern_pos_tremor, pattern_neg_tremor

    pattern_pos_calafrio = r"(\'[^\']*calafr[^\']*\')"
    pattern_neg_calafrio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calafr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calafr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calafr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*calafr[^\']*\')"
    )

    if c == "calafrio":
        return pattern_pos_calafrio, pattern_neg_calafrio
    
    
    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença

    pattern_pos_piuria = r"(\'[^\']*piuri[^\']*\')"
    pattern_neg_piuria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*piuri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*piuri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*piuri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*piuri[^\']*\')"
    )

    if c == "piuria":
        return pattern_pos_piuria, pattern_neg_piuria

    pattern_pos_urocultura = r"(\'[^\']*urocu[^\']*\')"
    pattern_neg_urocultura = (
        r"(\'[^\']*urocu[^\']*negat[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urocu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urocu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urocu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urocu[^\']*\')"
    )

    if c == "urocultura":
        return pattern_pos_urocultura, pattern_neg_urocultura

    pattern_pos_sondagem_vesical = r"(\'[^\']*sondag[^\']{1,50}vesic[^\']*\')"
    pattern_neg_sondagem_vesical = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}vesic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}vesic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}vesic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}vesic[^\']*\')"
    )

    if c == "sondagem_vesical":
        return pattern_pos_sondagem_vesical, pattern_neg_sondagem_vesical

    pattern_pos_sondagem_alivio = r"(\'[^\']*sondag[^\']{1,50}alivio[^\']*\')"
    pattern_neg_sondagem_alivio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}alivio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}alivio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}alivio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sondag[^\']{1,50}alivio[^\']*\')"
    )

    if c == "sondagem_alivio":
        return pattern_pos_sondagem_alivio, pattern_neg_sondagem_alivio

    pattern_pos_urgencia_miccional = r"(\'[^\']*urgenc[^\']{1,50}mic(c|s)?i[^\']*\')"
    pattern_neg_urgencia_miccional = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}mic(c|s)?i[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}mic(c|s)?i[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}mic(c|s)?i[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}mic(c|s)?i[^\']*\')"
    )

    if c == "urgencia_miccional":
        return pattern_pos_urgencia_miccional, pattern_neg_urgencia_miccional

    pattern_pos_urgencia_urinaria = r"(\'[^\']*urgenc[^\']{1,50}urinari[^\']*\')"
    pattern_neg_urgencia_urinaria = (
        r"(\'[^\']*sem((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*urgenc[^\']{1,50}urinari[^\']*\')"
    )

    if c == "urgencia_urinaria":
        return pattern_pos_urgencia_urinaria, pattern_neg_urgencia_urinaria

    pattern_pos_campylobacter = r"(\'[^\']*campylob[^\']*\')"
    pattern_neg_campylobacter = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*campylob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*campylob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*campylob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*campylob[^\']*\')"
    )

    if c == "campylobacter":
        return pattern_pos_campylobacter, pattern_neg_campylobacter

    pattern_pos_diarreia = r"(\'[^\']*diarr[^\']*\')"
    pattern_neg_diarreia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diarr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diarr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diarr[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diarr[^\']*\')"
    )

    if c == "diarreia":
        return pattern_pos_diarreia, pattern_neg_diarreia

    pattern_pos_dor_abdominal = (
        r"(\'[^\']*(?<![a-z])dor(?![a-z])[^\']{1,50}abdom(i)?n[^\']*\')"
    )
    pattern_neg_dor_abdominal = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}abdom(i)?n[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}abdom(i)?n[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}abdom(i)?n[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}abdom(i)?n[^\']*\')"
    )

    if c == "dor_abdominal":
        return pattern_pos_dor_abdominal, pattern_neg_dor_abdominal

    pattern_pos_dor_cabeca = r"(\'[^\']*(?<![a-z])dor(?![a-z])[^\']{1,50}cabec[^\']*\')"
    pattern_neg_dor_cabeca = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}cabec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}cabec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}cabec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}cabec[^\']*\')"
    )

    if c == "dor_cabeca":
        return pattern_pos_dor_cabeca, pattern_neg_dor_cabeca

    pattern_pos_giardia = r"(\'[^\']*giard[^\']*\')"
    pattern_neg_giardia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*giard[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*giard[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*giard[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*giard[^\']*\')"
    )

    if c == "giardia":
        return pattern_pos_giardia, pattern_neg_giardia

    pattern_pos_nausea = r"(\'[^\']*nause[^\']*\')"
    pattern_neg_nausea = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nause[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nause[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nause[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nause[^\']*\')"
    )

    if c == "nausea":
        return pattern_pos_nausea, pattern_neg_nausea

    pattern_pos_salmonela = r"(\'[^\']*salmonel[^\']*\')"
    pattern_neg_salmonela = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*salmonel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*salmonel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*salmonel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*salmonel[^\']*\')"
    )

    if c == "salmonela":
        return pattern_pos_salmonela, pattern_neg_salmonela

    pattern_pos_shigella = r"(\'[^\']*shigel[^\']*\')"
    pattern_neg_shigella = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shigel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shigel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shigel[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shigel[^\']*\')"
    )

    if c == "shigella":
        return pattern_pos_shigella, pattern_neg_shigella

    pattern_pos_vomito = r"(\'[^\']*vomit[^\']*\')"
    pattern_neg_vomito = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*vomit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*vomit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*vomit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*vomit[^\']*\')"
    )

    if c == "vomito":
        return pattern_pos_vomito, pattern_neg_vomito

    pattern_pos_yersinia = r"(\'[^\']*yersini[^\']*\')"
    pattern_neg_yersinia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*yersini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*yersini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*yersini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*yersini[^\']*\')"
    )

    if c == "yersinia":
        return pattern_pos_yersinia, pattern_neg_yersinia

    pattern_pos_colite_pseudomembranosa = r"(\'[^\']*colit[^\']{1,50}pseudome[^\']*\')"
    pattern_neg_colite_pseudomembranosa = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colit[^\']{1,50}pseudome[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colit[^\']{1,50}pseudome[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colit[^\']{1,50}pseudome[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colit[^\']{1,50}pseudome[^\']*\')"
    )

    if c == "colite_pseudomembranosa":
        return pattern_pos_colite_pseudomembranosa, pattern_neg_colite_pseudomembranosa

    pattern_pos_foco_urinario = r"(\'[^\']*foco[^\']{1,50}urinari[^\']*\')"
    pattern_neg_foco_urinario = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*foco[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*foco[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*foco[^\']{1,50}urinari[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*foco[^\']{1,50}urinari[^\']*\')"
    )

    if c == "foco_urinario":
        return pattern_pos_foco_urinario, pattern_neg_foco_urinario

    pattern_pos_dor_suprapubica = (
        r"(\'[^\']*(?<![a-z])dor(?![a-z])[^\']{1,50}suprapu[^\']*\')"
    )
    pattern_neg_dor_suprapubica = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}suprapu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}suprapu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}suprapu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])dor(?![a-z])[^\']{1,50}suprapu[^\']*\')"
    )

    if c == "dor_suprapubica":
        return pattern_pos_dor_suprapubica, pattern_neg_dor_suprapubica

    pattern_pos_pos_operatorio = (
        r"(\'[^\']*(?<![a-z])pos(\-|\s)?[^\']{1,50}operato[^\']*\')"
    )
    pattern_neg_pos_operatorio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pos(\-|\s)?[^\']{1,50}operato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pos(\-|\s)?[^\']{1,50}operato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pos(\-|\s)?[^\']{1,50}operato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pos(\-|\s)?[^\']{1,50}operato[^\']*\')"
    )

    if c == "pos_operatorio":
        return pattern_pos_pos_operatorio, pattern_neg_pos_operatorio




    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença
    pattern_pos_albumina = r"(\'[^\']*(?<![a-z])albumina[^\']*\')"
    pattern_neg_albumina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])albumina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])albumina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])albumina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])albumina[^\']*\')"
    )
    # 1
    if c == "albumina":
        return pattern_pos_albumina, pattern_neg_albumina

    pattern_pos_press_parc_co2 = (
        r"(\'[^\']*press[^\']*gas[^\']*carbonic[^\']*\')|"
        r"(\'[^\']*arter[^\']*pco[^\']*\')|"
        r"(\'[^\']*press[^\']*co2[^\']*\')|"
        r"(\'[^\']*paco2[^\']*\')|"
        r"(\'[^\']*pco2[^\']*\')"
    )
    pattern_neg_press_parc_co2 = (
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*press[^\']{1,50}gas[^\']{1,50}carbonic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*arter[^\']{1,50}pco[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*press[^\']{1,50}co2[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*paco2[^\']{1,50}\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pco2[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*press[^\']{1,50}gas[^\']{1,50}carbonic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*arter[^\']{1,50}pco[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*press[^\']{1,50}co2[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*paco2[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pco2[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*press[^\']{1,50}gas[^\']{1,50}carbonic[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*arter[^\']{1,50}pco[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*press[^\']{1,50}co2l[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*paco2[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pco2[^\']*\')"
    )
    #2
    if c == "press_parc_co2":
        return pattern_pos_press_parc_co2, pattern_neg_press_parc_co2

    pattern_pos_bicarbonato = r"(\'[^\']*bicarbonat[^\']*\')"
    pattern_neg_bicarbonato = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bicarbonat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bicarbonat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bicarbonat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bicarbonat[^\']*\')"
    )
    #3
    if c == "bicarbonato":
        return pattern_pos_bicarbonato, pattern_neg_bicarbonato

    pattern_pos_calcio = r"(\'[^\']*(?<![a-z])calci[^\']*\')"
    pattern_neg_calcio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])calci[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])calci[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])calci[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])calci[^\']*\')"
    )
    #4
    if c == "calcio":
        return pattern_pos_calcio, pattern_neg_calcio

    pattern_pos_creatinina = r"(\'[^\']*creatini[^\']*\')"
    pattern_neg_creatinina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*creatini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*creatini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*creatini[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*creatini[^\']*\')"
    )
    #5
    if c == "creatinina":
        return pattern_pos_creatinina, pattern_neg_creatinina

    pattern_pos_glicose = r"(\'[^\']*glicos[^\']*\')"
    pattern_neg_glicose = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicos[^\']*\')"
    )
    #6
    if c == "glicose":
        return pattern_pos_glicose, pattern_neg_glicose

    pattern_pos_hemoglobina = r"(\'[^\']*hemoglobina[^\']*\')"
    pattern_neg_hemoglobina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglobina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglobina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglobina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglobina[^\']*\')"
    )
    #7
    if c == "hemoglobina":
        return pattern_pos_hemoglobina, pattern_neg_hemoglobina

    pattern_pos_plaquetas = (
        r"(\'[^\']*plaqueta[^\']*\')|"
        r"(\'[^\']*plaquetop[^\']*\')|"
        r"(\'[^\']*trombocitop[^\']*\')"
    )
    pattern_neg_plaquetas = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaqueta[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaqueta[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaqueta[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaqueta[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaquetop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaquetop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaquetop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*plaquetop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*trombocitop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*trombocitop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*trombocitop[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*trombocitop[^\']*\')"
    )
    #8
    if c == "plaquetas":
        return pattern_pos_plaquetas, pattern_neg_plaquetas

    pattern_pos_potassio = r"(\'[^\']*potassio[^\']*\')"
    pattern_neg_potassio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*potassio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*potassio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*potassio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*potassio[^\']*\')"
    )
    #9
    if c == "potassio":
        return pattern_pos_potassio, pattern_neg_potassio

    pattern_pos_sodio = r"(\'[^\']*sodio[^\']*\')"
    pattern_neg_sodio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sodio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sodio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sodio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sodio[^\']*\')"
    )
    #10
    if c == "sodio":
        return pattern_pos_sodio, pattern_neg_sodio

    pattern_pos_bilirrubina = r"(\'[^\']*bilirrubin[^\']*\')"
    pattern_neg_bilirrubina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bilirrubin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bilirrubin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bilirrubin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bilirrubin[^\']*\')"
    )
    #11
    if c == "bilirrubina":
        return pattern_pos_bilirrubina, pattern_neg_bilirrubina

    pattern_pos_cardiomegalia = r"(\'[^\']*cardiomeg[^\']*\')"
    pattern_neg_cardiomegalia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cardiomeg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cardiomeg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cardiomeg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cardiomeg[^\']*\')"
    )
    #12
    if c == "cardiomegalia":
        return pattern_pos_cardiomegalia, pattern_neg_cardiomegalia

    pattern_pos_lesao_pulmonar = r"(\'[^\']*lesao[^\']*pulmon[^\']*\')"
    pattern_neg_lesao_pulmonar = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lesao[^\']{1,50}pulmon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lesao[^\']{1,50}pulmon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lesao[^\']{1,50}pulmon[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lesao[^\']{1,50}pulmon[^\']*\')"
    )
    #13
    if c == "lesao_pulmonar":
        return pattern_pos_lesao_pulmonar, pattern_neg_lesao_pulmonar

    pattern_pos_pneumonia = r"(\'[^\']*(pneumon|pnm(?![a-z]))[^\']*\')"
    pattern_neg_pneumonia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pneumon|pnm(?![a-z]))[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pneumon|pnm(?![a-z]))[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pneumon|pnm(?![a-z]))[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pneumon|pnm(?![a-z]))[^\']*\')"
    )
    #14
    if c == "pneumonia":
        return pattern_pos_pneumonia, pattern_neg_pneumonia

    pattern_pos_atelectasia = r"(\'[^\']*atelect[^\']*\')"
    pattern_neg_atelectasia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*atelect[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*atelect[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*atelect[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*atelect[^\']*\')"
    )
    #15
    if c == "atelectasia":
        return pattern_pos_atelectasia, pattern_neg_atelectasia

    pattern_pos_pneumotorax = r"(\'[^\']*pneumotor[^\']*\')"
    pattern_neg_pneumotorax = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumotor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumotor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumotor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumotor[^\']*\')"
    )
    #16
    if c == "pneumotorax":
        return pattern_pos_pneumotorax, pattern_neg_pneumotorax

    pattern_pos_fratura = r"(\'[^\']*fratu[^\']*\')"
    pattern_neg_fratura = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fratu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fratu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fratu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fratu[^\']*\')"
    )
    #17
    if c == "fratura":
        return pattern_pos_fratura, pattern_neg_fratura

    pattern_pos_freq_respiratoria = r"(\'[^\']*freq[^\']*respirat[^\']*\')"
    pattern_neg_freq_respiratoria = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}respirat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}respirat[^\']*\')"
    )
    #18
    if c == "freq_respiratoria":
        return pattern_pos_freq_respiratoria, pattern_neg_freq_respiratoria

    pattern_pos_freq_cardiaca = r"(\'[^\']*freq[^\']*cardiac[^\']*\')"
    pattern_neg_freq_cardiaca = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}cardiac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}cardiac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}cardiac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*freq[^\']{1,50}cardiac[^\']*\')"
    )
    #19
    if c == "freq_cardiaca":
        return pattern_pos_freq_cardiaca, pattern_neg_freq_cardiaca

    pattern_pos_pressao_sanguinea = (
        r"(\'[^\']*pressao[^\']{1,50}sanguin[^\']*\')|"
        r"(\'[^\']*sistoli[^\']*\')|"
        r"(\'[^\']*diastoli[^\']*\')"
    )
    pattern_neg_pressao_sanguinea = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pressao[^\']{1,50}sanguin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pressao[^\']{1,50}sanguin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pressao[^\']{1,50}sanguin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pressao[^\']{1,50}sanguin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sistoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sistoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sistoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sistoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diastoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diastoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diastoli[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diastoli[^\']*\')"
    )
    #20
    if c == "pressao_sanguinea":
        return pattern_pos_pressao_sanguinea, pattern_neg_pressao_sanguinea

    pattern_pos_saturacao_sangue = r"(\'[^\']*saturac[^\']*sangu[^\']*\')"
    pattern_neg_saturacao_sangue = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*saturac[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*saturac[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*saturac[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*saturac[^\']{1,50}sangu[^\']*\')"
    )
    #21
    if c == "saturacao_sangue":
        return pattern_pos_saturacao_sangue, pattern_neg_saturacao_sangue

    pattern_pos_hemocultura = r"(\'[^\']*hemocu[^\']*\')"
    pattern_neg_hemocultura = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemocu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemocu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemocu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemocu[^\']*\')"
    )
    #22
    if c == "hemocultura":
        return pattern_pos_hemocultura, pattern_neg_hemocultura
    
    
    
    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença

    pattern_pos_propionibacterium = (
        r"(\'[^\']*cutib[^\']*acne[^\']*\')|"
        r"(\'[^\']*propionib[^\']*acne[^\']*\')|"
        r"(\'[^\']*cutibac[^\']*\')|"
        r"(\'[^\']*propionibac[^\']*\')"
    )
    pattern_neg_propionibacterium = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionib[^\']*acne[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cutibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionibac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propionibac[^\']*\')"
    )

    if c == "propionibacterium":
        return pattern_pos_propionibacterium, pattern_neg_propionibacterium

    pattern_pos_cryptococcus = r"(\'[^\']*(cr(i|y)p(i)?tococ(c)?(o|u)?(s)?)[^\']*\')"
    pattern_neg_cryptococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cr(i|y)p(i)?tococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cr(i|y)p(i)?tococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cr(i|y)p(i)?tococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cr(i|y)p(i)?tococ(c)?(o|u)?(s)?)[^\']*\')"
    )

    if c == "cryptococcus":
        return pattern_pos_cryptococcus, pattern_neg_cryptococcus

    pattern_pos_pneumocystis = r"(\'[^\']*(p(i)?neumoc(i|y)st(t)?(i|y|e)(s)?)[^\']*\')"
    pattern_neg_pneumocystis = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(p(i)?neumoc(i|y)st(i|y|e)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(p(i)?neumoc(i|y)st(i|y|e)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(p(i)?neumoc(i|y)st(i|y|e)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cr(i|y)p(i)?tococ(c)?(o|u)?(s)?)[^\']*\')"
    )

    if c == "pneumocystis":
        return pattern_pos_pneumocystis, pattern_neg_pneumocystis

    pattern_pos_histoplasma = r"(\'[^\']*histoplasm[^\']*\')"
    pattern_neg_histoplasma = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*histoplasm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*histoplasm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*histoplasm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*histoplasm[^\']*\')"
    )

    if c == "histoplasma":
        return pattern_pos_histoplasma, pattern_neg_histoplasma

    pattern_pos_paracoccidioides = r"(\'[^\']*paracoc(c)?(i|y)d(i|y)o(i|y)d[^\']*\')"
    pattern_neg_paracoccidioides = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(paracoc(c)?(i|y)d(i|y)o(i|y)d)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(paracoc(c)?(i|y)d(i|y)o(i|y)d)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(paracoc(c)?(i|y)d(i|y)o(i|y)d)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(paracoc(c)?(i|y)d(i|y)o(i|y)d)[^\']*\')"
    )

    if c == "paracoccidioides":
        return pattern_pos_paracoccidioides, pattern_neg_paracoccidioides

    pattern_pos_bacteroides = r"(\'[^\']*(bacter(i)?oide(?!t))[^\']*\')"
    pattern_neg_bacteroides = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacter(i)?oide(?!t))[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacter(i)?oide(?!t))[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacter(i)?oide(?!t))[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacter(i)?oide(?!t))[^\']*\')"
    )

    if c == "bacteroides":
        return pattern_pos_bacteroides, pattern_neg_bacteroides

    pattern_pos_candida = r"(\'[^\']*candid[^\']*\')"
    pattern_neg_candida = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*candid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*candid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*candid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*candid[^\']*\')"
    )

    if c == "candida":
        return pattern_pos_candida, pattern_neg_candida

    pattern_pos_clostridium = (
        r"(\'[^\']*clostridi[^\']*\')|"
        r"(\'[^\']*colite[^\']*(pseudo)?membranos[^\']*\')"
    )
    pattern_neg_clostridium = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')"
    )

    if c == "clostridium":
        return pattern_pos_clostridium, pattern_neg_clostridium

    pattern_pos_fusobacterium = r"(\'[^\']*fusobacter[^\']*\')"
    pattern_neg_fusobacterium = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fusobacter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fusobacter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fusobacter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fusobacter[^\']*\')"
    )

    if c == "fusobacterium":
        return pattern_pos_fusobacterium, pattern_neg_fusobacterium

    pattern_pos_peptostreptococcus = (
        r"(\'[^\']*(pep(i)?tostrep(i)?tococ(c)?(o|u)?(s)?)[^\']*\')"
    )
    pattern_neg_peptostreptococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pep(i)?tostrep(i)?tococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pep(i)?tostrep(i)?tococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pep(i)?tostrep(i)?tococ(c)?(o|u)?(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(pep(i)?tostrep(i)?tococ(c)?(o|u)?(s)?)[^\']*\')"
    )

    if c == "peptostreptococcus":
        return pattern_pos_peptostreptococcus, pattern_neg_peptostreptococcus

    pattern_pos_sibilancia = r"(\'[^\']*(?<![a-z])sibil[^\']*\')"
    pattern_neg_sibilancia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sibil[^\']*\')"
    )

    if c == "sibilancia":
        return pattern_pos_sibilancia, pattern_neg_sibilancia

    pattern_pos_hipotensao = r"(\'[^\']*hipotensao[^\']*\')"
    pattern_neg_hipotensao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotensao[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotensao[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotensao[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotensao[^\']*\')"
    )

    if c == "hipotensao":
        return pattern_pos_hipotensao, pattern_neg_hipotensao

    pattern_pos_hipotermia = r"(\'[^\']*hipotermia[^\']*\')"
    pattern_neg_hipotermia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotermi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotermi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotermi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hipotermi[^\']*\')"
    )

    if c == "hipotermia":
        return pattern_pos_hipotermia, pattern_neg_hipotermia

    pattern_pos_apneia = r"(\'[^\']*ap(i)?nei[^\']*\')"
    pattern_neg_apneia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ap(i)?nei[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ap(i)?nei[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ap(i)?nei[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ap(i)?nei[^\']*\')"
    )

    if c == "apneia":
        return pattern_pos_apneia, pattern_neg_apneia

    pattern_pos_bradicardia = r"(\'[^\']*bradicardi[^\']*\')"
    pattern_neg_bradicardia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bradicardi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bradicardi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bradicardi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bradicardi[^\']*\')"
    )

    if c == "bradicardia":
        return pattern_pos_bradicardia, pattern_neg_bradicardia

    pattern_pos_streptococcus_viridans = r"(\'[^\']*((?<![a-z])(e)?strep(i)?tococ(c)?(o|u)?(s)?)[^\']{1,50}virid[^\']*\')"
    pattern_neg_streptococcus_viridans = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((?<![a-z])(e)?strep(i)?tococ(c)?(o|u)?(s)?)[^\']{1,50}virid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((?<![a-z])(e)?strep(i)?tococ(c)?(o|u)?(s)?)[^\']{1,50}virid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((?<![a-z])(e)?strep(i)?tococ(c)?(o|u)?(s)?)[^\']{1,50}virid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*((?<![a-z])(e)?strep(i)?tococ(c)?(o|u)?(s)?)[^\']{1,50}virid[^\']*\')"
    )

    if c == "streptococcus_viridans":
        return pattern_pos_streptococcus_viridans, pattern_neg_streptococcus_viridans

    pattern_pos_consciencia = r"(\'[^\']*consci[^\']*\')"
    pattern_neg_consciencia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consci[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consci[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consci[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*consci[^\']*\')"
    )

    if c == "consciencia":
        return pattern_pos_consciencia, pattern_neg_consciencia

    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença

    pattern_pos_pcr_covid = (
        r"(\'[^\']*(?<![a-z])pcr[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])pcr[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*detec[^\']*\')"
    )
    pattern_neg_pcr_covid = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*posit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*detec[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*covid[^\']*detec[^\']*\')"
    )

    if c == "pcr_covid":
        return pattern_pos_pcr_covid, pattern_neg_pcr_covid

    pattern_pos_peep = r"(\'[^\']*(?<![a-z])peep(?![a-z])[^\']*\')"
    pattern_neg_peep = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])peep(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])peep(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])peep(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])peep(?![a-z])[^\']*\')"
    )

    if c == "peep":
        return pattern_pos_peep, pattern_neg_peep

    pattern_pos_fio2 = r"(\'[^\']*(?<![a-z])fio(2|²)(?![a-z])[^\']*\')"
    pattern_neg_fio2 = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fio(2|²)(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fio(2|²)(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fio(2|²)(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fio(2|²)(?![a-z])[^\']*\')"
    )

    if c == "fio2":
        return pattern_pos_fio2, pattern_neg_fio2

    pattern_pos_spo2 = r"(\'[^\']*(?<![a-z])spo(2|²)(?![a-z])[^\']*\')"
    pattern_neg_spo2 = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])spo(2|²)(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])spo(2|²)(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])spo(2|²)(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])spo(2|²)(?![a-z])[^\']*\')"
    )

    if c == "spo2":
        return pattern_pos_spo2, pattern_neg_spo2

    pattern_pos_covid = (
        r"(\'[^\']*(?<![a-z])covid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])coronav[^\']*\')|"
        r"(\'[^\']*coron[^\']*vir[^\']*\')"
    )
    pattern_neg_covid = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])covid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])covid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])covid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])covid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])coronav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])coronav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])coronav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])coronav[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coron[^\']*vir[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coron[^\']*vir[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coron[^\']*vir[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*coron[^\']*vir[^\']*\')"
    )

    if c == "covid":
        return pattern_pos_covid, pattern_neg_covid

    pattern_pos_hcm = (
        r"(\'[^\']*(?<![a-z])hcm[^\']*\')|"
        r"(\'[^\']*hemoglob[^\']*corpusc[^\']*med[^\']*\')"
    )
    pattern_neg_hcm = (
        r"(\'[^\']*hcm[^\']*(negat|irrelev|ausen)[^\']*\')|"
        r"(\'[^\']*hemoglob[^\']*corpusc[^\']*med[^\']*(negat|irrelev|ausen)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hcm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hcm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hcm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hcm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*corpusc[^\']*med[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*corpusc[^\']*med[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*corpusc[^\']*med[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*corpusc[^\']*med[^\']*\')"
    )

    if c == "hcm":
        return pattern_pos_hcm, pattern_neg_hcm

    pattern_pos_hgm = (
        r"(\'[^\']*(?<![a-z])hgm[^\']*\')|"
        r"(\'[^\']*hemoglob[^\']*glob[^\']*med[^\']*\')"
    )
    pattern_neg_hgm = (
        r"(\'[^\']*hgm[^\']*(negat|irrelev|ausen)[^\']*\')|"
        r"(\'[^\']*hemoglob[^\']*glob[^\']*med[^\']*(negat|irrelev|ausen)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hgm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hgm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hgm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])hgm[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*glob[^\']*med[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*glob[^\']*med[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*glob[^\']*med[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemoglob[^\']*glob[^\']*med[^\']*\')"
    )

    if c == "hgm":
        return pattern_pos_hgm, pattern_neg_hgm

    pattern_pos_corynebacterium = r"(\'[^\']*(cor(i|y)nebacter)[^\']*\')"
    pattern_neg_corynebacterium = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cor(i|y)nebacter)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cor(i|y)nebacter)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cor(i|y)nebacter)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(cor(i|y)nebacter)[^\']*\')"
    )

    if c == "corynebacterium":
        return pattern_pos_corynebacterium, pattern_neg_corynebacterium

    pattern_pos_bacillus = r"(\'[^\']*(bacil(l)?(o|u)(s)?)[^\']*\')"
    pattern_neg_bacillus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacil(l)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacil(l)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacil(l)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(bacil(l)?(o|u)(s)?)[^\']*\')"
    )

    if c == "bacillus":
        return pattern_pos_bacillus, pattern_neg_bacillus

    pattern_pos_aerococcus = r"(\'[^\']*(aerococ(c)?(o|u)(s)?)[^\']*\')"
    pattern_neg_aerococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(aerococ(c)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(aerococ(c)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(aerococ(c)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(aerococ(c)?(o|u)(s)?)[^\']*\')"
    )

    if c == "aerococcus":
        return pattern_pos_aerococcus, pattern_neg_aerococcus

    pattern_pos_micrococcus = r"(\'[^\']*(micrococ(c)?(o|u)(s)?)[^\']*\')"
    pattern_neg_micrococcus = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(micrococ(c)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(micrococ(c)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(micrococ(c)?(o|u)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(micrococ(c)?(o|u)(s)?)[^\']*\')"
    )

    if c == "micrococcus":
        return pattern_pos_micrococcus, pattern_neg_micrococcus

    pattern_pos_coccidioides = r"(\'[^\']*(?<![a-z])(coc(c)?(i|y)oid(e|i)(s)?)[^\']*\')"
    pattern_neg_coccidioides = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])(coc(c)?(i|y)oid(e|i)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])(coc(c)?(i|y)oid(e|i)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])(coc(c)?(i|y)oid(e|i)(s)?)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])(coc(c)?(i|y)oid(e|i)(s)?)[^\']*\')"
    )

    if c == "coccidioides":
        return pattern_pos_coccidioides, pattern_neg_coccidioides

    pattern_pos_prevotella = r"(\'[^\']*(prevotel(l)?a)[^\']*\')"
    pattern_neg_prevotella = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(prevotel(l)?a)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(prevotel(l)?a)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(prevotel(l)?a)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(prevotel(l)?a)[^\']*\')"
    )

    if c == "prevotella":
        return pattern_pos_prevotella, pattern_neg_prevotella

    pattern_pos_veillonella = r"(\'[^\']*(veil(l)?onel(l)?a)[^\']*\')"
    pattern_neg_veillonella = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(veil(l)?onel(l)?a)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(veil(l)?onel(l)?a)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(veil(l)?onel(l)?a)[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(veil(l)?onel(l)?a)[^\']*\')"
    )

    if c == "veillonella":
        return pattern_pos_veillonella, pattern_neg_veillonella

    pattern_pos_temperatura = r"(\'[^\']*temperat[^\']*\')"
    pattern_neg_temperatura = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*temperat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*temperat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*temperat[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*temperat[^\']*\')"
    )
    #23
    if c == "temperatura":
        return pattern_pos_temperatura, pattern_neg_temperatura

    pattern_pos_ph_sangue = (
        r"(\'[^\']*ph[^\']{1,50}sangu[^\']{1,50}alterad[^\']*\')|"
        r"(\'[^\']*ph[^\']{1,50}sangu[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*altera[^\']{1,50}ph[^\']{1,50}sangu[^\']*\')"
    )
    pattern_neg_ph_sangue = (
        r"(\'[^\']*ph[^\']{1,50}sangu[^\']{1,50}(?<![a-z])normal[^\']*\')|"
        r"(\'[^\']*ph[^\']{1,50}sangu[^\']{1,50}estave[^\']*\')|"
        r"(\'[^\']*ph[^\']{1,50}sangu[^\']{1,50}estab[^\']*\')|"
        r"(\'[^\']*estab[^\']{1,50}ph[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}alterad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}alterad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}alterad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}alterad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ph[^\']{1,50}sangu[^\']{1,50}anormal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}ph[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}ph[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}ph[^\']{1,50}sangu[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*altera[^\']{1,50}ph[^\']{1,50}sangu[^\']*\')"
    )

    if c == "ph_sangue":
        return pattern_pos_ph_sangue, pattern_neg_ph_sangue
    
    
    
        # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença

    pattern_pos_avc = (
        r"(\'[^\']*(?<![a-z])avc(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ave(?![a-z])[^\']*\')|"
        r"(\'[^\']*aciden[^\']*vasc[^\']*cereb[^\']*\')|"
        r"(\'[^\']*aciden[^\']*vasc[^\']*encef[^\']*\')"
    )
    pattern_neg_avc = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])avc(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])avc(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])avc(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])avc(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ave(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ave(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ave(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ave(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*cereb[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*cereb[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*cereb[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*cereb[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*encef[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*encef[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*encef[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aciden[^\']*vasc[^\']*encef[^\']*\')"
    )

    if c == "avc":
        return pattern_pos_avc, pattern_neg_avc

    pattern_pos_sne = (
        r"(\'[^\']*(?<![a-z])sne(?![a-z])[^\']*\')|"
        r"(\'[^\']*sond[^\']*naso[^\']*enter[^\']*\')"
    )
    pattern_neg_sne = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sne(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sne(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sne(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sne(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']*naso[^\']*enter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']*naso[^\']*enter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']*naso[^\']*enter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sond[^\']*naso[^\']*enter[^\']*\')"
    )

    if c == "sne":
        return pattern_pos_sne, pattern_neg_sne

    pattern_pos_desnutricao = (
        r"(\'[^\']*(?<![a-z])desnutri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])emagrecim[^\']*\')"
    )
    pattern_neg_desnutricao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])desnutri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])desnutri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])desnutri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])desnutri[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])emagrecim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])emagrecim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])emagrecim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])emagrecim[^\']*\')"
    )

    if c == "desnutricao":
        return pattern_pos_desnutricao, pattern_neg_desnutricao

    pattern_pos_sedacao = (
        r"(\'[^\']*(?<![a-z])sedac[^\']*\')|" r"(\'[^\']*(?<![a-z])sedad[^\']*\')"
    )
    pattern_neg_sedacao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedac[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])sedad[^\']*\')"
    )

    if c == "sedacao":
        return pattern_pos_sedacao, pattern_neg_sedacao

    pattern_pos_vsg = (
        r"(\'[^\']*(?<![a-z])veloc[^\']*sediment[^\']*glob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])veloc[^\']*hemossedim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])vsg(?![a-z])[^\']*\')"
    )
    pattern_neg_vsg = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*sediment[^\']*glob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*sediment[^\']*glob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*sediment[^\']*glob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*sediment[^\']*glob[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*hemossedim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*hemossedim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*hemossedim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])veloc[^\']*hemossedim[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vsg(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vsg(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vsg(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])vsg(?![a-z])[^\']*\')"
    )

    if c == "vsg":
        return pattern_pos_vsg, pattern_neg_vsg

    pattern_pos_fosfatase_alcalina = r"(\'[^\']*(?<![a-z])fosfat[^\']*alcal[^\']*\')"
    pattern_neg_fosfatase_alcalina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fosfat[^\']*alcal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fosfat[^\']*alcal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fosfat[^\']*alcal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])fosfat[^\']*alcal[^\']*\')"
    )

    if c == "fosfatase_alcalina":
        return pattern_pos_fosfatase_alcalina, pattern_neg_fosfatase_alcalina

    pattern_pos_ldh = (
        r"(\'[^\']*(?<![a-z])ldh(?![a-z])[^\']*\')|"
        r"(\'[^\']*lactat[^\']*desidrog[^\']*\')"
    )
    pattern_neg_ldh = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ldh(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ldh(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ldh(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ldh(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lactat[^\']*desidrog[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lactat[^\']*desidrog[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lactat[^\']*desidrog[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lactat[^\']*desidrog[^\']*\')"
    )

    if c == "ldh":
        return pattern_pos_ldh, pattern_neg_ldh

    pattern_pos_cetamina = r"(\'[^\']*cetamin[^\']*\')|" r"(\'[^\']*ketamin[^\']*\')"
    pattern_neg_cetamina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cetamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cetamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cetamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cetamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ketamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ketamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ketamin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ketamin[^\']*\')"
    )

    if c == "cetamina":
        return pattern_pos_cetamina, pattern_neg_cetamina

    pattern_pos_propofol = r"(\'[^\']*propofol[^\']*\')"
    pattern_neg_propofol = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propofol[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propofol[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propofol[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*propofol[^\']*\')"
    )

    if c == "propofol":
        return pattern_pos_propofol, pattern_neg_propofol

    pattern_pos_clorpromazina = r"(\'[^\']*clorpromazina[^\']*\')"
    pattern_neg_clorpromazina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorpromazina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorpromazina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorpromazina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clorpromazina[^\']*\')"
    )

    if c == "clorpromazina":
        return pattern_pos_clorpromazina, pattern_neg_clorpromazina

    pattern_pos_fentanil = r"(\'[^\']*fentanil[^\']*\')"
    pattern_neg_fentanil = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fentanil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fentanil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fentanil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fentanil[^\']*\')"
    )

    if c == "fentanil":
        return pattern_pos_fentanil, pattern_neg_fentanil

    pattern_pos_pancuronio = r"(\'[^\']*pancuronio[^\']*\')"
    pattern_neg_pancuronio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pancuronio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pancuronio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pancuronio[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pancuronio[^\']*\')"
    )

    if c == "pancuronio":
        return pattern_pos_pancuronio, pattern_neg_pancuronio

    pattern_pos_noradrenalina = r"(\'[^\']*(?<![a-z])noradrenalina[^\']*\')"
    pattern_neg_noradrenalina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])noradrenalina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])noradrenalina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])noradrenalina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])noradrenalina[^\']*\')"
    )

    if c == "noradrenalina":
        return pattern_pos_noradrenalina, pattern_neg_noradrenalina

    pattern_pos_diazepan = r"(\'[^\']*diazepan[^\']*\')"
    pattern_neg_diazepan = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diazepan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diazepan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diazepan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diazepan[^\']*\')"
    )

    if c == "diazepan":
        return pattern_pos_diazepan, pattern_neg_diazepan

    pattern_pos_midazolan = r"(\'[^\']*midazolan[^\']*\')"
    pattern_neg_midazolan = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*midazolan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*midazolan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*midazolan[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*midazolan[^\']*\')"
    )

    if c == "midazolan":
        return pattern_pos_midazolan, pattern_neg_midazolan

    pattern_pos_lorazepan = r"(\'[^\']*lorazepa[^\']*\')"
    pattern_neg_lorazepan = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lorazepa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lorazepa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lorazepa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lorazepa[^\']*\')"
    )

    if c == "lorazepan":
        return pattern_pos_lorazepan, pattern_neg_lorazepan



    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença

    pattern_pos_flumazenil = r"(\'[^\']*flumazenil[^\']*\')"
    pattern_neg_flumazenil = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*flumazenil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*flumazenil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*flumazenil[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lorazflumazenilepan[^\']*\')"
    )

    if c == "flumazenil":
        return pattern_pos_flumazenil, pattern_neg_flumazenil

    pattern_pos_clonidina = r"(\'[^\']*clonidina[^\']*\')"
    pattern_neg_clonidina = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clonidina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clonidina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clonidina[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clonidina[^\']*\')"
    )

    if c == "clonidina":
        return pattern_pos_clonidina, pattern_neg_clonidina

    pattern_pos_npt = (
        r"(\'[^\']*(?<![a-z])npt(?![a-z])[^\']*\')|"
        r"(\'[^\']*nutri[^\']*parent[^\']*total[^\']*\')"
    )
    pattern_neg_npt = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])npt(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])npt(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])npt(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])npt(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nutri[^\']*parent[^\']*total[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nutri[^\']*parent[^\']*total[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nutri[^\']*parent[^\']*total[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*nutri[^\']*parent[^\']*total[^\']*\')"
    )

    if c == "npt":
        return pattern_pos_npt, pattern_neg_npt

    pattern_pos_cateter_monolumen = (
        r"(\'[^\']*catet[^\']*mono[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])cml(?![a-z])[^\']*\')"
    )
    pattern_neg_cateter_monolumen = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*mono[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*mono[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*mono[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*mono[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cml(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cml(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cml(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cml(?![a-z])[^\']*\')"
    )

    if c == "cateter_monolumen":
        return pattern_pos_cateter_monolumen, pattern_neg_cateter_monolumen

    pattern_pos_cateter_duplolumen = (
        r"(\'[^\']*catet[^\']*dupl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])cdl(?![a-z])[^\']*\')"
    )
    pattern_neg_cateter_duplolumen = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*dupl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*dupl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*dupl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*dupl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cdl(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cdl(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cdl(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])cdl(?![a-z])[^\']*\')"
    )

    if c == "cateter_duplolumen":
        return pattern_pos_cateter_duplolumen, pattern_neg_cateter_duplolumen

    pattern_pos_cateter_triplolumen = (
        r"(\'[^\']*catet[^\']*tripl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ctl(?![a-z])[^\']*\')"
    )
    pattern_neg_cateter_triplolumen = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*tripl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*tripl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*tripl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*tripl[^\']*lumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ctl(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ctl(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ctl(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])ctl(?![a-z])[^\']*\')"
    )

    if c == "cateter_triplolumen":
        return pattern_pos_cateter_triplolumen, pattern_neg_cateter_triplolumen

    pattern_pos_portocath = (
        r"(\'[^\']*portocath[^\']*\')|" r"(\'[^\']*port[^\']*cath[^\']*\')"
    )
    pattern_neg_portocath = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*portocath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*portocath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*portocath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*portocath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*port[^\']*cath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*port[^\']*cath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*port[^\']*cath[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*port[^\']*cath[^\']*\')"
    )

    if c == "portocath":
        return pattern_pos_portocath, pattern_neg_portocath

    pattern_pos_cateter_hickmann = r"(\'[^\']*catet[^\']*hickman[^\']*\')"
    pattern_neg_cateter_hickmann = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*hickman[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*hickman[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*hickman[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*catet[^\']*hickman[^\']*\')"
    )

    if c == "cateter_hickmann":
        return pattern_pos_cateter_hickmann, pattern_neg_cateter_hickmann

    pattern_pos_shilley = r"(\'[^\']*shilley[^\']*\')"
    pattern_neg_shilley = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shilley[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shilley[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shilley[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*shilley[^\']*\')"
    )

    if c == "shilley":
        return pattern_pos_shilley, pattern_neg_shilley

    pattern_pos_obesidade = (
        r"(\'[^\']*obeso(?![a-z])[^\']*\')|" r"(\'[^\']*obesid[^\']*\')"
    )
    pattern_neg_obesidade = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obeso(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obeso(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obeso(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obeso(?![a-z])[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obesid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obesid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obesid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*obesid[^\']*\')"
    )

    if c == "obesidade":
        return pattern_pos_obesidade, pattern_neg_obesidade

    pattern_pos_diabetes = r"(\'[^\']*diabet[^\']*\')"
    pattern_neg_diabetes = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diabet[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diabet[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diabet[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*diabet[^\']*\')"
    )

    if c == "diabetes":
        return pattern_pos_diabetes, pattern_neg_diabetes

    pattern_pos_neutropenia = r"(\'[^\']*neutropeni[^\']*\')"
    pattern_neg_neutropenia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*neutropeni[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*neutropeni[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*neutropeni[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*neutropeni[^\']*\')"
    )

    if c == "neutropenia":
        return pattern_pos_neutropenia, pattern_neg_neutropenia

    pattern_pos_tabagismo = r"(\'[^\']*tabagis[^\']*\')"
    pattern_neg_tabagismo = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tabagis[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tabagis[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tabagis[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*tabagis[^\']*\')"
    )

    if c == "tabagismo":
        return pattern_pos_tabagismo, pattern_neg_tabagismo


    
    # todas as expressões regulares possuem uma aspa (') como delimitador inicial de
    # sentença onde \' é o delimitador inicial, [^\']* é qualquer caractere que não
    # seja aspa, x é o termo procurado, [^\']* é qualquer caractere que não seja
    # aspa novamente, #\' é o delimitador final da sentença
    
    pattern_pos_int_alimentar = (
        r"(\'[^\']*intol[^\']*aliment[^\']*\')"
        r"(\'[^\']*reduz[^\']*apetit[^\']*\')"
        r"(\'[^\']*(?<![a-z])reduz[^\']*tolera[^\']*aliment[^\']*\')|"
    )
    pattern_neg_int_alimentar = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*aliment[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*aliment[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*aliment[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*aliment[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*reduz[^\']*apetit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*reduz[^\']*apetit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*reduz[^\']*apetit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*reduz[^\']*apetit[^\']*\')"
    )

    if c == "int_alimentar":
        return pattern_pos_int_alimentar, pattern_neg_int_alimentar
    
    pattern_pos_int_glicose = (
        r"(\'[^\']*intol[^\']*glicose[^\']*\')"
    )
    pattern_neg_int_glicose = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*glicose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*glicose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*glicose[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*intol[^\']*glicose[^\']*\')"
    )

    if c == "int_glicose":
        return pattern_pos_int_glicose, pattern_neg_int_glicose
    
    pattern_pos_letargia = (
        r"(\'[^\']*letarg[^\']*\')"
        r"(\'[^\']*lentid[^\']*\')"
    )
    pattern_neg_letargia = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*letarg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*letarg^[\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*letarg[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*letarg[^\']*\')"
       # r"(\'[^\']*melhora[^\']*letarg[^\']*\')"
       # r"(\'[^\']*melhora[^\']*lentid[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lentid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lentid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lentid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*lentid[^\']*\')"
    )

    if c == "letargia":
        return pattern_pos_letargia, pattern_neg_letargia
    
    pattern_pos_pcr = (
        r"(\'[^\']*pcr[^\']*alter[^\']*\')"
        r"(\'[^\']*pcr[^\']*elev[^\']*\')"
        r"(\'[^\']*pcr[^\']*aument[^\']*\')"
        r"(\'[^\']*(?<![a-z])prote[^\']*c[^\']*reat[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])prote[^\']*c[^\']*reat[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])prote[^\']*c[^\']*reat[^\']*aument[^\']*\')|"
    )
    pattern_neg_pcr = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*alter[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*elev[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*elev[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])pcr[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*aumen[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*(?<![a-z])prote[^\']*c[^\']*reat[^\']*aumen[^\']*\')"
    )

    if c == "pcr":
        return pattern_pos_pcr, pattern_neg_pcr
    
    pattern_pos_asp_bilioso = (
        r"(\'[^\']*asp[^\']*bilioso[^\']*\')"
        r"(\'[^\']*conte[^\']*bilioso[^\']*\')"
    )
    pattern_neg_asp_bilioso = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*asp[^\']*bilios[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*asp[^\']*bilios[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*asp[^\']*bilios[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*asp[^\']*bilios[^\']*\')"
       # r"(\'[^\']*aspi[^\']*normal[^\']*\')"
       # r"(\'[^\']*aspi[^\']*tipic[^\']*\')"
       # r"(\'[^\']*conte[^\']*gastr[^\']*normal[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*conte[^\']*bilios[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*conte[^\']*bilios[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*conte[^\']*bilios[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*conte[^\']*bilios[^\']*\')"
    )

    if c == "asp_bilioso":
        return pattern_pos_asp_bilioso, pattern_neg_asp_bilioso
    
    pattern_pos_dist_abdominal = (r"(\'[^\']*dist[^\']*abdomin[^\']*\')")
    pattern_neg_dist_abdominal = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dist[^\']*abdomin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dist[^\']*abdomin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dist[^\']*abdomin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dist[^\']*abdomin[^\']*\')"
    )

    if c == "dist_abdominal":
        return pattern_pos_dist_abdominal, pattern_neg_dist_abdominal
    
    pattern_pos_pneumoperitonio = (r"(\'[^\']*pneumoperit[^\']*\')")
    pattern_neg_pneumoperitonio = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumoperit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumoperit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumoperit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pneumoperit[^\']*\')"
    )

    if c == "pneumoperitonio":
        return pattern_pos_pneumoperitonio, pattern_neg_pneumoperitonio
    
    pattern_pos_convulsao = (r"(\'[^\']*convuls[^\']*\')")
    pattern_neg_convulsao = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*convuls[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*convuls[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*convuls[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*convuls[^\']*\')"
    )

    if c == "convulsao":
        return pattern_pos_convulsao, pattern_neg_convulsao
    
    pattern_pos_sangue_fezes = (
        r"(\'[^\']*PSOF[^\']*positivo[^\']*\')"
        r"(\'[^\']*PSOF[^\']*reagente[^\']*\')"
        r"(\'[^\']*TSOF[^\']*positivo[^\']*\')"
        r"(\'[^\']*TSOF[^\']*reagente[^\']*\')"
        r"(\'[^\']*sang[^\']*oculto[^\']*\')"
        r"(\'[^\']*sang[^\']*fezes[^\']*\')"
        )
    pattern_neg_sangue_fezes = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*positivo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*positivo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*positivo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*positivo[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*reagente[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*reagente[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*reagente[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*PSOF[^\']*reagente[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*positivo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*positivo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*positivo[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*positivo[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*reagente[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*reagente[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*reagente[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*TSOF[^\']*reagente[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*oculto[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*oculto[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*oculto[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*oculto[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*fezes[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*fezes[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*fezes[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*sang[^\']*fezes[^\']*\')"
    )
    if c == "sangue_fezes":
        return pattern_pos_sangue_fezes, pattern_neg_sangue_fezes
    
    pattern_pos_intestino_fixo = (
        r"(\'[^\']*alça[^\']*fixa[^\']*\')"
        r"(\'[^\']*alça[^\']*intestinal[^\']*fixa[^\']*\')"
        r"(\'[^\']*alça[^\']*ader[^\']*\')"
        r"(\'[^\']*cong[^\']*alça[^\']*\')"
        r"(\'[^\']*ades[^\']*alça[^\']*\')"
        )
    pattern_neg_intestino_fixo = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*fixa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*fixa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*fixa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*fixa[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*intestinal[^\']*fixa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*intestinal[^\']*fixa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*intestinal[^\']*fixa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*intestinal[^\']*fixa[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*ader[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*ader[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*ader[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*alça[^\']*ader[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cong[^\']*alça[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cong[^\']*alça[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cong[^\']*alça[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cong[^\']*alça[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ades[^\']*alça[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ades[^\']*alça[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ades[^\']*alça[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*ades[^\']*alça[^\']*\')"
    )
    if c == "intestino_fixo":
        return pattern_pos_intestino_fixo, pattern_neg_intestino_fixo
    
    pattern_pos_necrose_intestinal = (
        r"(\'[^\']*necros[^\']*intesti[^\']*\')"
        r"(\'[^\']*necros[^\']*intesti[^\']*exten[^\']*\')"
        r"(\'[^\']*necros[^\']*intesti[^\']*grand[^\']*\')"
        )
    pattern_neg_necrose_intestinal = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*exten[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*exten[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*exten[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*exten[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*grand[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*grand[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*grand[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*necros[^\']*intesti[^\']*grand[^\']*\')"
    )
    if c == "necrose_intestinal":
        return pattern_pos_necrose_intestinal, pattern_neg_necrose_intestinal
    
    pattern_pos_dren_serosa = (r"(\'[^\']*dren[^\']*serosa[^\']*\')")
    pattern_neg_dren_serosa = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*serosa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*serosa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*serosa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*dren[^\']*serosa[^\']*\')"
    )

    if c == "dren_serosa":
        return pattern_pos_dren_serosa, pattern_neg_dren_serosa
    
    pattern_pos_clostridium = (
        r"(\'[^\']*clostridi[^\']*\')|"
        r"(\'[^\']*colite[^\']*(pseudo)?membranos[^\']*\')"
    )
    pattern_neg_clostridium = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*clostridi[^\']*\')|"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*colite[^\']*(pseudo)?membranos[^\']*\')"
    )

    if c == "clostridium":
        return pattern_pos_clostridium, pattern_neg_clostridium

    pattern_pos_cultura_liquor = (
        r"(\'[^\']*cult[^\']*liquor[^\']*\')"
        r"(\'[^\']*bacteriol[^\']*liquor[^\']*\')"
        )
    pattern_neg_cultura_liquor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cult[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cult[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cult[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*cult[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriol[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriol[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriol[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriol[^\']*liquor[^\']*\')"
    )
    if c == "cultura_liquor":
        return pattern_pos_cultura_liquor, pattern_neg_cultura_liquor
    
    pattern_pos_irritabilidade = (
        r"(\'[^\']*irritabiidade[^\']*\')"
        r"(\'[^\']*comport[^\']*irrit[^\']*\')"
        )
    pattern_neg_irritabilidade = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*irritabiidade[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*irritabiidade[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*irritabiidade[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*irritabiidade[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*comport[^\']*irrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*comport[^\']*irrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*comport[^\']*irrit[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*comport[^\']*irrit[^\']*\')"
    )
    if c == "irritabilidade":
        return pattern_pos_irritabilidade, pattern_neg_irritabilidade
    
    pattern_pos_bacteria_liquor = (
        r"(\'[^\']*bacteriosc[^\']*posit[^\']*liquor[^\']*\')"
        r"(\'[^\']*bacteri[^\']*identi[^\']*liquor[^\']*\')"
        r"(\'[^\']*bacteri[^\']*liquor[^\']*\')"
        r"(\'[^\']*bacteri[^\']*presen[^\']*liquor[^\']*\')"
        )
    pattern_neg_bacteria_liquor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriosc[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriosc[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriosc[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteriosc[^\']*posit[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*identi[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*identi[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*identi[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*identi[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*presen[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*presen[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*presen[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*bacteri[^\']*presen[^\']*liquor[^\']*\')"
    )
    if c == "bacteria_liquor":
        return pattern_pos_bacteria_liquor, pattern_neg_bacteria_liquor
    
    pattern_pos_leuco_liquor = (
        r"(\'[^\']*leuco[^\']*posit[^\']*liquor[^\']*\')"
        r"(\'[^\']*leuco[^\']*aument[^\']*liquor[^\']*\')"
        r"(\'[^\']*leucocitose[^\']*liquor[^\']*\')"
        r"(\'[^\']*leuco[^\']*alter[^\']*liquor[^\']*\')"
        )
    pattern_neg_leuco_liquor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*posit[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*aument[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*aument[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*aument[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*aument[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leucocitose[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*leuco[^\']*alter[^\']*liquor[^\']*\')"
    )
    if c == "leuco_liquor":
        return pattern_pos_leuco_liquor, pattern_neg_leuco_liquor
    
    pattern_pos_prote_liquor = (
        r"(\'[^\']*prote[^\']*posit[^\']*liquor[^\']*\')"
        r"(\'[^\']*prote[^\']*aument[^\']*liquor[^\']*\')"
        r"(\'[^\']*prote[^\']*alter[^\']*liquor[^\']*\')"
        )
    pattern_neg_prote_liquor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*posit[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*posit[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*aument[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*aument[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*aument[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*aument[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*prote[^\']*alter[^\']*liquor[^\']*\')"
    )
    if c == "prote_liquor":
        return pattern_pos_prote_liquor, pattern_neg_prote_liquor
    
    pattern_pos_glicose_liquor = (
        r"(\'[^\']*glicose[^\']*reduz[^\']*liquor[^\']*\')"
        r"(\'[^\']*glicose[^\']*alter[^\']*liquor[^\']*\')"
        )
    pattern_neg_glicose_liquor = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*reduz[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*reduz[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*reduz[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*reduz[^\']*liquor[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*alter[^\']*liquor[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*glicose[^\']*alter[^\']*liquor[^\']*\')"
    )
    if c == "glicose_liquor":
        return pattern_pos_glicose_liquor, pattern_neg_glicose_liquor
    
    pattern_pos_fontanela_abaulada = (
        r"(\'[^\']*fontanela[^\']*anter[^\']*abaul[^\']*\')"
        r"(\'[^\']*fontanela[^\']*anter[^\']*proemin[^\']*\')"
        r"(\'[^\']*fontanela[^\']*anter[^\']*bombad[^\']*\')"
        r"(\'[^\']*fontanela[^\']*cheia[^\']*\')"
        r"(\'[^\']*fontanela[^\']*anter[^\']*tens[^\']*\')"
        r"(\'[^\']*fontanela[^\']*anter[^\']*rigid[^\']*\')"
        r"(\'[^\']*fontanela[^\']*anter[^\']*pinhal[^\']*\')"
        r"(\'[^\']*aument[^\']*tens[^\']*fontanela[^\']*\')"
        )
    pattern_neg_fontanela_abaulada = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*abaul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*abaul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*abaul[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*abaul[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*proemin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*proemin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*proemin[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*proemin[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*bombad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*bombad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*bombad[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*bombad[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*tens[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*tens[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*tens[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*tens[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*rigid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*rigid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*rigid[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*rigid[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*pinhal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*pinhal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*pinhal[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*anter[^\']*pinhal[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*cheia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*cheia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*cheia[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*fontanela[^\']*cheia[^\']*\')"
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aument[^\']*tens[^\']*fontanela[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aument[^\']*tens[^\']*fontanela[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aument[^\']*tens[^\']*fontanela[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*aument[^\']*tens[^\']*fontanela[^\']*\')"
    )
    if c == "fontanela_abaulada":
        return pattern_pos_fontanela_abaulada, pattern_neg_fontanela_abaulada
    
    pattern_pos_piora_troca_gasosa = r"(\'[^\']*pior[^\']*troca[^\']*gasosa[^\']*\')"
    pattern_neg_piora_troca_gasosa = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pior[^\']*troca[^\']*gasosa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pior[^\']*troca[^\']*gasosa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pior[^\']*troca[^\']*gasosa[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*pior[^\']*troca[^\']*gasosa[^\']*\')"
    )
    if c == "piora_troca_gasosa":
        return pattern_pos_piora_troca_gasosa, pattern_neg_piora_troca_gasosa
    
    pattern_pos_piora_troca_gasosa = r"(\'[^\']*hemogr[^\']*alter[^\']*\')"
    pattern_neg_piora_troca_gasosa = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemogr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemogr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemogr[^\']*alter[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*hemogr[^\']*alter[^\']*\')"
    )
    if c == "piora_troca_gasosa":
        return pattern_pos_piora_troca_gasosa, pattern_neg_piora_troca_gasosa
    
    pattern_pos_pneumatose = r"(\'[^\']*\spneumato[^\']*\')"
    pattern_neg_pneumatose = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\spneumato[^\']*\')"
    )
    if c == "pneumatose":
        return pattern_pos_pneumatose, pattern_neg_pneumatose
    
    pattern_pos_hipoativ = (
        r"(\'[^\']*\shipoativ[^\']*\')"
        r"(\'[^\']*(?<![a-z])diminui[çc][aã]o(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\satividad[^\']*\')"
    )
    pattern_neg_hipoativ = (
        r"(\'[^\']*(?<![a-z])sem(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\shipoativ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])neg((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\shipoativ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])ausen((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\shipoativ[^\']*\')|"
        r"(\'[^\']*(?<![a-z])nao(?![a-z])((?!\'|com\s|,\srefere|,\sapresenta|,\smas).)*\shipoativ[^\']*\')"
    )
    if c == "hipoativ":
        return pattern_pos_hipoativ, pattern_neg_hipoativ
