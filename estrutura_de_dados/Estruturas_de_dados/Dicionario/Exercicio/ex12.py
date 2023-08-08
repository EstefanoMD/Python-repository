"""
Crie um dicionário que atribua valores numéricos a cada letra do alfabeto, de acordo com as pontuações do jogo de Scrabble. 
Escreva uma função que recebe uma palavra como entrada e retorna a pontuação total da palavra de acordo com os valores das letras no dicionário.
"""

pontuacoes_scrabble = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4,
    "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3,
    "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
    "Y": 4, "Z": 10
}

def resultado_scrabble ():
    pontuacao = []
    palavra = input("Digite uma palavra para saber sua pontuação: ")
    for letra in palavra.upper():
        if letra in pontuacoes_scrabble:
            pontos = pontuacoes_scrabble[letra]
            pontuacao.append(pontos)
    pontuacao = sum(pontuacao)
    return pontuacao


joga = resultado_scrabble()

print(joga)