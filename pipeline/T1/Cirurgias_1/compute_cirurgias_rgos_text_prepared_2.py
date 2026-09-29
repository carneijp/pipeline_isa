from ImpararePackage import dataRequest
from ImpararePackage import maestro

def main():
    query = """
        SELECT * FROM "imparare2_t1_cirurgias_4_4"
    """

    df = dataRequest.get_data(queryText= query)
    pos = 0
    for c in df:

        c = maestro.remove_nan(df= c, column= "texto_cirurgia")

        c = maestro.normalize(df= c, column= "texto_cirurgia")

        c = maestro.trim(df= c, column= "texto_cirurgia")

        tuplas = [
            ("\n", ". "),
            (r"\|", "."),
            (r"\s\.\s", "."),
            (r"\s\s", ".")
        ]
        c = maestro.replace_values_list(df= c, column= "texto_cirurgia", arrayDeTuplas= tuplas )
        
        dataRequest.set_data_on_sql(df= c, nomeTabelaDestino= "imparare2_t1_cirurgias_4_5", if_exists= "replace" if int(pos) == 0 else "append")
        pos +=1

if __name__ == "__main__":
    main()