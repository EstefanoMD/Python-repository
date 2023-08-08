#Exemplo 1
texto = "Python Python Python é uma linguagem de programação poderosa e fácil de aprender."

frequencia_palavras = {}
for palavra in texto.split():
    frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1

print(frequencia_palavras)
# Saída: {'Python': 1, 'é': 1, 'uma': 1, 'linguagem': 1, 'de': 1, 'programação': 1, 'poderosa': 1, 'e': 1, 'fácil': 1, 'aprender.': 1}

#Exemplo 2

frase = "A batata é um alimento muito versátil e nutritivo."
frequencia_letras = {}
for letra in frase:
        frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1
print(frequencia_letras)
# Saída: {'A': 1, 'b': 1, 'a': 4, 't': 3, 'u': 5, 'e': 3, 'l': 2, 'i': 3, 'm': 3, 'n': 3, 'v': 1, 'r': 3, 's': 3}

frase = "A batata é um alimento muito versátil e nutritivo."
frequencia_letras = {letra: frase.count(letra) for letra in frase if letra != ' '}
print(frequencia_letras)
