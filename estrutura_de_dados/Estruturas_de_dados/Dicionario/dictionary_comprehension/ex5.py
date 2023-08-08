#Dado um dicionário com nomes de produtos como chaves e seus preços como valores, crie um novo dicionário que tenha os mesmos produtos como chaves e os preços aumentados em 10% como valores.

produto_valor_original = {
    "maçã": 2.5,
    "banana": 1.0,
    "laranja": 1.2,
    "uva": 3.0,
    "morango": 4.0
}
produto_valor_novo = {produto : round(valor*1.1,2) for produto,valor in produto_valor_original.items()}
print(produto_valor_novo)