import re

frase = "Esse filho da puta está atrasando a porra da equipe"

dicionario_censura = {
    "puta" : "****",
    "porra" : "****",
    "caralho" : "****",
    "desgraçado" : "****",
    "desgraça" : "****",
    "burro" : "****",
    "macaco" : "****",
    "lixo" : "****",
    "vagabundo" : "****",
    "bosta" : "****",


}

palavras = frase.split()
frase_censurada = []

for palavra in palavras:
    palavra_formatada = re.sub(r'[^\w\s]', '', palavra.lower())  # Remove pontuação e converte para minúsculas
    if palavra_formatada in dicionario_censura:
        censura = dicionario_censura[palavra_formatada]
        frase_censurada.append(censura)
    else:
        frase_censurada.append(palavra)

frase_censurada = " ".join(frase_censurada)
print(frase_censurada)
