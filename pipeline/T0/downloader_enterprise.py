from ImpararePackage import dataRequest

def main():
    """Esse script baixa 10 linhas não tem porque paralelizar"""
    print("Iniciando downloader_enterprise")
    query_dowloader = "select * FROM public.enterprise"
    replace = True

    df = dataRequest.get_data(queryText= query_dowloader, isWellheadEngine=True)
    count = 0
    for c in df:
        count += len(c)
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "enterprise", if_exists= "replace" if replace else "append")
        replace = False
    print(f"Baixado no total: {count} linhas em enterprise - downloader_enterprise")
    
if __name__ == "__main__":
    main()