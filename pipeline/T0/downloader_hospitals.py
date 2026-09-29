from ImpararePackage import dataRequest

def main():
    """Esse script baixa 10 linhas não tem porque paralelizar"""
    print("Iniciando downloader_hospitals")
    query_dowloader = "select * FROM public.hospital"
    replace = True

    df = dataRequest.get_data(queryText= query_dowloader, isWellheadEngine=True)
    count = 0
    for c in df:
        count += len(c)
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "hospitals", if_exists= "replace" if replace else "append")
        replace = False
    print(f"Baixado no total: {count} linhas em hospitals - downloader_hospitals")
    
if __name__ == "__main__":
    main()