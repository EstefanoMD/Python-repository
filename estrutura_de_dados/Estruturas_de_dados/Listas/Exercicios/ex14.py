#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import random

lista_de_temp_mes = []

for i in range(12):
    temp_meses = random.randrange(10,40)
    lista_de_temp_mes.append(temp_meses)


def media():
    media_anual = sum(lista_de_temp_mes)/len(lista_de_temp_mes)
    return media_anual

media_anual = media()

lista_indice = []
temp_acima_media = []
meses_extenso = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

for i , temperatura in enumerate(lista_de_temp_mes):
    if temperatura > media_anual:
        temp_acima_media.append(temperatura)
        lista_indice.append(i + 1)
        
print("Temperaturas acima da média")
for i, mes in enumerate(lista_indice):
    print(f"{meses_extenso[mes]} - {temp_acima_media[i]}°C")