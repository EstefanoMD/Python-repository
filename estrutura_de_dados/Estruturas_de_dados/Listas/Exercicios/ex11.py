#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista_1 = []
lista_2 = []

for i in range(10):
    lista_1.append(i)

for i in range(10,21):
    lista_2.append(i)

lista_3 = []
for i , j in zip(lista_1 , lista_2):
    lista_3.append(i)
    lista_3.append(j)


print(lista_3)