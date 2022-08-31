import json
from dados import *
#Convertando uma lista em formato Python para Json
lista = [1,2,3,4]
lista_json = json.dumps(lista)



#Convertando dados Json para dicinário em Python]
dicionario = json.loads(clientes_json)

#Exibindo o novo dicionário

for key , value in dicionario.items():
    print(key)
    print(value)


#Criando um arquivo em JSON


with open('cliente.json' , 'w') as arquivo:
    json.dump(clientes_dicionarios,arquivo, indent= 4)

#Transformando o arquivo criado em JSON para um dicionário em Python


with open('cliente.json' , 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)









    



