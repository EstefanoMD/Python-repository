"""
Crie um dicionário que funcione como um tradutor simples de palavras. 
Ele deve conter algumas palavras em inglês como chaves e suas traduções em português como valores. 
Escreva uma função que recebe uma palavra em inglês como entrada e retorna a tradução em português, ou uma mensagem caso a palavra não esteja no dicionário.
"""


traducoes = {
    "hello": "olá",
    "world": "mundo",
    "cat": "gato",
    "dog": "cachorro",
    "tree": "árvore",
    "book": "livro",
    "computer": "computador",
    "sun": "sol",
    "moon": "lua",
    "flower": "flor",
    "water": "água",
    "friend": "amigo",
    "family": "família",
    "food": "comida",
    "love": "amor"
}


def trudutor (): 
    palavra_original = input("Digite uma palavra em inglês para ser traduzida: ")
    if palavra_original in traducoes:
        palavra_traduzida = traducoes[palavra_original]
        return palavra_traduzida
    else :
        return "Palavra não encontrada no dicionario !!!!"

palavra_traduzida = trudutor()
print(palavra_traduzida)