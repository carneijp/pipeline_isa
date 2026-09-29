with open("logErrorTrain.txt", "w") as file:
    print("iniciando suspeita")
    import time
    import datetime
    inicio = time.time()

    try: 
        import compute_suspeita_v2_prepared_2 as um
        inicio_meio = time.time()
        um.main()
        fim_meio= time.time()
        dif = fim_meio - inicio_meio
        resultado = f"Fim do suspeita 1: {datetime.timedelta(seconds= dif)}\n" 
        file.write(resultado)
        print(resultado)

        import compute_suspeita_2 as dois
        inicio_meio = time.time()
        dois.main()
        fim_meio= time.time()
        dif = fim_meio - inicio_meio
        resultado = f"Fim do suspeita 2: {datetime.timedelta(seconds= dif)}\n" 
        file.write(resultado)
        print(resultado)

    except Exception as error:
        file.write(str(error))

    fim = time.time()
    diferenca = fim - inicio
    humanredable = datetime.timedelta(seconds= diferenca)
    print("Tempo suspeita: ", humanredable)
    tempo = 'Tempo gasto suspeita: ' + str(humanredable) + '\n'
    file.write(tempo)
