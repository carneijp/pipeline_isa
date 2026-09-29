from ImpararePackage import dataRequest

def main():

    dataRequest.execute('DROP TABLE IF EXISTS "imparare2_prescricoesantibiotico_by_prontuario"')
    dataRequest.execute("""
        SET synchronous_commit = off;
        CREATE UNLOGGED TABLE "imparare2_prescricoesantibiotico_by_prontuario" AS
        SELECT 
            registro AS prontuario,
            dthr_prescricao AS dthr_prescricao,
            SUM("atb_COMUNITARIO") AS "ATB_COMUNITARIO_count",
            SUM("atb_TOPICO") AS "ATB_TOPICO_count",
            SUM("atb_INTERMEDIARIO") AS "ATB_INTERMEDIARIO_count",
            SUM("atb_HOSPITALAR") AS "ATB_HOSPITALAR_count",
            SUM("atb_MMR") AS "ATB_MMR_count",
            SUM("atb_ANTIFUNGICO") AS "ATB_ANTIFUNGICO_count",
            SUM("atb_OUTROS") AS "ATB_OUTROS_count",
            SUM("atb_PROFILATICO") AS "ATB_PROFILATICO_count",
            MAX ("atb_importancia") AS "atb_categ",
            MAX ("via_importancia") AS "via_categ" --,
            -- SUM("via_PARENTERAL") AS "via_PARENTERAL_count",
            -- SUM("via_ENTERAL") AS "via_ENTERAL_count",
            -- SUM("via_TOPICO") AS "via_TOPICO_count",
            -- SUM("via_OUTRO") AS "via_OUTRO_count"
        FROM "imparare2_prescricoesantibiotico_prepared_teste"
        GROUP BY registro, dthr_prescricao;
    """)
    #dataRequest.execute("""
        #SET synchronous_commit = off;
        #CREATE UNLOGGED TABLE "imparare2_prescricoesantibiotico_by_prontuario" AS
        #SELECT 
         #   registro AS prontuario,
          #  dthr_prescricao AS dthr_prescricao,
            #SUM("atb_ACICLOVIR") AS "ACICLOVIR_count",
            #SUM("atb_AMICACINA") AS "AMICACINA_count",            
            #SUM("atb_AMOXICILINA_CLAVULANATO") AS "AMOXICILINA_CLAVULANATO_count",
            #SUM("atb_AMOXICILINA") AS "AMOXICILINA_count",
            #SUM("atb_AMOXICILINA_SULBACTAM") AS "AMOXICILINA_SULBACTAM_count",
            #SUM("atb_AMPICILINA_SULBACTAM") AS "AMPICILINA_SULBACTAM_count",
            #SUM("atb_AMPICILINA") AS "AMPICILINA_count",
            #SUM("atb_AZITROMICINA") AS "AZITROMICINA_count",
            #SUM("atb_PENICILINAGBENZATINA") AS "PENICILINAGBENZATINA_count",
            #SUM("atb_PENICILINAGPOTASSICA") AS "PENICILINAGPOTASSICA_count",
            #SUM("atb_CEFALEXINA") AS "CEFALEXINA_count",
            #SUM("atb_CEFADROXILA") AS "CEFADROXILA_count",
            #SUM("atb_CEFALOTINA") AS "CEFALOTINA_count",
            #SUM("atb_CEFAZOLINA") AS "CEFAZOLINA_count",
            #SUM("atb_CEFOTAXIMA") AS "CEFOTAXIMA_count",
            #SUM("atb_CEFEPIMA") AS "CEFEPIMA_count",
            #SUM("atb_CEFTRIAXONA") AS "CEFTRIAXONA_count",
            #SUM("atb_CEFUROXIMA") AS "CEFUROXIMA_count",
            #SUM("atb_CEFTALOZANA_TAZOBACTAM") AS "CEFTALOZANA_TAZOBACTAM_count",
            #SUM("atb_CEFTAZIDIMA_AVIBACTAM") AS "CEFTAZIDIMA_AVIBACTAM_count",
            #SUM("atb_CEFTAZIDIMA") AS "CEFTAZIDIMA_count",
            #SUM("atb_CIPROFLOXACINO") AS "CIPROFLOXACINO_count",
            #SUM("atb_CLARITROMICINA") AS "CLARITROMICINA_count",
            #SUM("atb_CLINDAMICINA") AS "CLINDAMICINA_count",
            #SUM("atb_ERITROMICINA") AS "ERITROMICINA_count",
            #SUM("atb_ERTAPENEM") AS "ERTAPENEM_count",
            #SUM("atb_CLORANFENICOL") AS "CLORANFENICOL_count",
            #SUM("atb_FLUCONAZOL") AS "FLUCONAZOL_count",
            #SUM("atb_CETOCONAZOL") AS "CETOCONAZOL_count",
            #SUM("atb_NEOMICINA") AS "NEOMICINA_count",
            #SUM("atb_MOXIFLOXACINO") AS "MOXIFLOXACINO_count",
            #SUM("atb_GENTAMICINA") AS "GENTAMICINA_count",
            #SUM("atb_GANCICLOVIR") AS "GANCICLOVIR_count",
            #SUM("atb_LEVOFLOXACINO") AS "LEVOFLOXACINO_count",
            #SUM("atb_LINEZOLIDA") AS "LINEZOLIDA_count",
            #SUM("atb_MEROPENEM") AS "MEROPENEM_count",
            #SUM("atb_METRONIDAZOL") AS "METRONIDAZOL_count",
            #SUM("atb_MICAFUNGINA") AS "MICAFUNGINA_count",
            #SUM("atb_DOXICICLINA") AS "DOXICICLINA_count",
            #SUM("atb_IVERMECTINA") AS "IVERMECTINA_count",
            #SUM("atb_TEICOPLANINA") AS "TEICOPLANINA_count",  
            #SUM("atb_NISTATINA") AS "NISTATINA_count",
            #SUM("atb_MICONAZOL") AS "MICONAZOL_count",
            #SUM("atb_MUPIROCINA") AS "MUPIROCINA_count",
            #SUM("atb_SULFADIAZINA") AS "SULFADIAZINA_count",
            #SUM("atb_OXACILINA") AS "OXACILINA_count",
            #SUM("atb_PIPERACILINA_TAZOBACTAM") AS "PIPERACILINA_TAZOBACTAM_count",
            #SUM("atb_SULFAMETOXAZOL_TRIMETOPRIM") AS "SULFAMETOXAZOL_TRIMETOPRIM_count",
            #SUM("atb_POLIMIXINAB") AS "POLIMIXINAB_count",
            #SUM("atb_RIFAMPICINA") AS "RIFAMPICINA_count",
            #SUM("atb_TOBRAMICINA") AS "TOBRAMICINA_count",
            #SUM("atb_VANCOMICINA") AS "VANCOMICINA_count",
            #SUM("atb_VORICONAZOL") AS "VORICONAZOL_count",
            #SUM("atb_OUTRO") AS "OUTRO_count",
            #SUM("via_EV") AS "via_EV_count",
            #SUM("via_IM") AS "via_IM_count",
            #SUM("via_TOPICO") AS "via_TOPICO_count",
            #SUM("via_SNG") AS "via_SNG_count",
            #SUM("via_VO") AS "via_VO_count",
            #SUM("via_OUTRO") AS "via_OUTRO_count"
        #FROM "imparare2_prescricoesantibiotico_prepared"
        #GROUP BY registro, dthr_prescricao;
    #""")

if __name__ == "__main__":
    main()