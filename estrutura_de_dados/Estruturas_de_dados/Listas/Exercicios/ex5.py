#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
def exerc5():
    letras = ['a','b','c','d','e','f','g','h','i','j']
    consoantes = []
    vogais = ['a','e','i','o','u']

    for letra in letras:
        if letra not in vogais:
            consoantes.append(letra)
        
    print("Cosoante lidas:")
    print(" ".join(consoantes   ))
    print("Quantidade de consoantes lidas:", len(consoantes))s