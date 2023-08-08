def exerc6():
    lista_de_numeros = []
    impares = []
    pares = []
    for i in range(1,21):
        lista_de_numeros.append(i)
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print("Lista de números",lista_de_numeros)
    print("pares",pares)
    print("impares",impares)