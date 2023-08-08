#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import random 
random_numbers = []
for _ in range(5):
    random_numbers.append(random.randrange(1,11))

def soma():
    soma = sum(random_numbers)
    print(soma)

def multi():
    resultado_da_multiplicação = 1
    for i in random_numbers:
        resultado_da_multiplicação *= i
    print(resultado_da_multiplicação)

print(random_numbers)
soma()
multi()



"""
1-import random: Esta linha importa o módulo random, que é uma biblioteca padrão do Python para trabalhar com geração de números pseudoaleatórios.
2-random_numbers = []: Esta linha cria uma lista vazia chamada random_numbers, que será usada para armazenar os números inteiros aleatórios.
3-for _ in range(10):: Esta é a estrutura do loop for, que irá executar o bloco de código que está indentado abaixo dele 10 vezes. 
O loop usa range(10), que gera uma sequência de números de 0 a 9 (ou seja, 10 elementos), mas o valor real não é usado (indicado pelo _, que é uma convenção para indicar que o valor não será utilizado).
4-random_numbers.append(random.randrange(1, 101)): Dentro do loop for, esta linha adiciona um número inteiro aleatório à lista random_number
5-print : mostra na tela o resultado
"""