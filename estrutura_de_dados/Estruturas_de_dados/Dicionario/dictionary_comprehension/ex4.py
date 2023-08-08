#Crie um dicionário que mapeie cada letra de uma string para o número de vezes que ela aparece na string. Ignore espaços em branco.
string = "A lua é uma extensão da terra"
dicionario_repeticao = {letra : string.count(letra) for letra in string if letra != " "}
print(dicionario_repeticao)