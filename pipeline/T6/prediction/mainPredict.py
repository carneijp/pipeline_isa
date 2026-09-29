import time
import datetime
from multiprocessing import freeze_support
        
def main():
    with open("logErrorPredict.txt", "w") as file:
        print("iniciando predict caso infeccao")
        inicio = time.time()

        pos = 0
        try: 
            import predictInfection as um
            inicio_meio = time.time()
            um.main()
            pos += 1
            fim_meio= time.time()
            dif = fim_meio - inicio_meio
            resultado = f"Fim do {pos}: {datetime.timedelta(seconds= dif)}\n" 
            file.write(resultado)
            print(resultado)

            import predictCommunityOrIRAS as dois
            inicio_meio = time.time()
            dois.main()
            pos += 1
            fim_meio= time.time()
            dif = fim_meio - inicio_meio
            resultado = f"Fim do {pos}: {datetime.timedelta(seconds= dif)}\n" 
            file.write(resultado)
            print(resultado)

            import compute_new_isa_set_scored_casos_infeccao_rescaled_2 as tres
            inicio_meio = time.time()
            tres.main()
            pos += 1
            fim_meio= time.time()
            dif = fim_meio - inicio_meio
            resultado = f"Fim do {pos}: {datetime.timedelta(seconds= dif)}\n" 
            file.write(resultado)
            print(resultado)

            import compute_new_isa_set_scored_casos_comunitaria_or_iras_rescaled as quatro
            inicio_meio = time.time()
            quatro.main()
            pos += 1
            fim_meio= time.time()
            dif = fim_meio - inicio_meio
            resultado = f"Fim do {pos}: {datetime.timedelta(seconds= dif)}\n" 
            file.write(resultado)
            print(resultado)

            import compute_new_isa_infeccao_2 as cinco
            inicio_meio = time.time()
            cinco.main()
            pos += 1
            fim_meio= time.time()
            dif = fim_meio - inicio_meio
            resultado = f"Fim do {pos}: {datetime.timedelta(seconds= dif)}\n" 
            file.write(resultado)
            print(resultado)

            import compute_isa_suspeita_v2_2 as seis
            inicio_meio = time.time()
            seis.main()
            pos += 1
            fim_meio= time.time()
            dif = fim_meio - inicio_meio
            resultado = f"Fim do {pos}: {datetime.timedelta(seconds= dif)}\n" 
            file.write(resultado)
            print(resultado)

        except Exception as error:
            file.write(str(error))
        
        fim = time.time()
        diferenca = fim - inicio
        humanredable = datetime.timedelta(seconds= diferenca)
        print("Tempo predict caso infeccao: ", humanredable)
        tempo = 'Tempo gasto predict caso infeccao: ' + str(humanredable) + '\n'
        file.write(tempo)
    
if __name__ == "__main__":
    freeze_support()
    main()