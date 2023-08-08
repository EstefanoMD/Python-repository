"""
1-Crie um dicionário que represente um cardápio de restaurante, onde as chaves são os nomes dos pratos e os valores são os preços. Use a função .items() para imprimir o cardápio.

2-Dado um dicionário que mapeia nomes de frutas para suas cores, use um loop para imprimir as frutas e suas cores separadamente.

3-Crie um dicionário com o nome e a idade de algumas pessoas. Utilize a função .items() para calcular a média das idades.

4-Crie um dicionário com palavras como chaves e suas respectivas traduções como valores. Crie uma frase em outro idioma e use um loop para traduzir cada palavra.

5-Crie um dicionário com nomes de países e suas capitais. Peça ao usuário para digitar um país e use o dicionário para mostrar a capital correspondente.

6-Crie um dicionário com nomes de animais e a quantidade de pernas que eles têm. Use um loop para imprimir apenas os animais que têm quatro pernas.

7-Crie um dicionário com nomes de alunos e suas notas. Calcule a média das notas usando a função .items().

8-Crie um dicionário com nomes de carros e suas velocidades máximas. Use um loop para encontrar o carro mais rápido.

9- Crie um dicionário com nomes de produtos e seus preços. Peça ao usuário para digitar o nome de um produto e use o dicionário para mostrar o preço.

10-Crie um dicionário com palavras como chaves e suas definições como valores. Peça ao usuário para digitar uma palavra e use o dicionário para mostrar a definição.

Esses exercícios ajudarão você a praticar o uso da função .items() e a aprimorar suas habilidades com dicionários em Python.

"""



# 1-Crie um dicionário que represente um cardápio de restaurante, onde as chaves são os nomes dos pratos e os valores são os preços. Use a função .items() para imprimir o cardápio.



# pratos_tipicos = {
#     "Feijoada": 35.00,
#     "Acarajé": 7.50,
#     "Moqueca de Peixe": 42.00,
#     "Coxinha": 2.50,
#     "Bobó de Camarão": 50.00
# }

# contador = 1

# for prato , valor in pratos_tipicos.items():
#     print(f" {contador} - {prato} R$ {valor}")
#     contador += 1

#2-Dado um dicionário que mapeia nomes de frutas para suas cores, use um loop para imprimir as frutas e suas cores separadamente.

# frutas_cores = {
#     "maçã": "vermelha",
#     "banana": "amarela",
#     "laranja": "laranja",
#     "uva": "roxa",
#     "limão": "verde"
# }

# # Usando um loop para imprimir as frutas e suas cores
# for fruta, cor in frutas_cores.items():
#     print(f"A fruta {fruta} é da cor {cor}.")


#3-Crie um dicionário com o nome e a idade de algumas pessoas. Utilize a função .items() para calcular a média das idades.

# dados_pessoais = {
#     "Alice": 20,
#     "Bob": 30,
#     "Carol": 28,
#     "David": 22,
#     "Eve": 33
# }

# lista_de_idades = []

# for nomes , idade in dados_pessoais.items():

#     lista_de_idades.append(idade)

# lista_de_idades = sum(lista_de_idades) / len(lista_de_idades)
# print(lista_de_idades)

# 4-Crie um dicionário com palavras como chaves e suas respectivas traduções como valores. Crie uma frase em outro idioma e use um loop para traduzir cada palavra.

# Definindo o dicionário que relaciona palavras em inglês com suas traduções em português
# dicionario_ingles_portugues = {
#     "The": "O",
#     "sun": "sol",
#     "is": "está",
#     "shining": "brilhando",
#     "and": "e",
#     "birds": "pássaros",
#     "are": "estão",
#     "singing": "cantando",
#     "in": "no",
#     "the": "o",
#     "sky": "céu"
# }

# # Definindo a frase em inglês que será traduzida
# frase = "The sun is shining and the birds are singing in the sky ."

# # Dividindo a frase em palavras individuais e armazenando-as em uma lista
# palavras = frase.split()

# # Criando uma lista vazia para armazenar as palavras traduzidas
# frase_traduzida = []

# # Iterando sobre cada palavra na lista de palavras
# for palavra in palavras:
#     # Verificando se a palavra está no dicionário de tradução
#     if palavra in dicionario_ingles_portugues:
#         # Se estiver, obtemos a tradução correspondente
#         traducao = dicionario_ingles_portugues[palavra]
#         # Adicionamos a tradução à lista de palavras traduzidas
#         frase_traduzida.append(traducao)
#     else:
#         # Se a palavra não estiver no dicionário, mantemos a palavra original
#         frase_traduzida.append(palavra)

# # Juntando as palavras traduzidas de volta em uma frase usando espaço como separador
# frase_traduzida = " ".join(frase_traduzida)

# # Imprimindo a frase traduzida
# print(frase_traduzida)

#5-Crie um dicionário com nomes de países e suas capitais. Peça ao usuário para digitar um país e use o dicionário para mostrar a capital correspondente.

# paises_capitais = {
#     "Brasil": "Brasília",
#     "Estados Unidos": "Washington, D.C.",
#     "França": "Paris",
#     "Japão": "Tóquio",
#     "Alemanha": "Berlim",
#     "Austrália": "Camberra",
#     "Canadá": "Ottawa",
#     "Índia": "Nova Deli",
#     "Itália": "Roma",
#     "China": "Pequim"
# }

# capital = input("Digite um país para obter a capital: ")

# if capital in paises_capitais:
#     print(f"Capital {paises_capitais[capital]}")







































