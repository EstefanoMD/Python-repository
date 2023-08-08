#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista_1 = []
lista_2 = []
lista_3 = []

for i in range(1,11):
    lista_1.append(i)

for i in range(10,110,10):
    lista_2.append(i)

for i in range(100,1100,100):
    lista_3.append(i)

lista_final = []
for i , j , k in zip(lista_1,lista_2,lista_3):
    lista_final.append(i)
    lista_final.append(j)
    lista_final.append(k)

print(lista_final)