#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

lista_de_numeros = []
for i in range(1,11) :
    lista_de_numeros.append(i**2)

def soma_dos_quadrados():
    soma_dos_quadrados = sum(lista_de_numeros)
    print(soma_dos_quadrados)

soma_dos_quadrados()
