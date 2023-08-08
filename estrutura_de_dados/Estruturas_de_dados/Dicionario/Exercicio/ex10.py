def mesclar_dicionario(dict1, dict2):
    novo_dicionario = {nome : idade for nome,idade in dict1.items() }
    novo_dicionario.update({nome : idade for nome , idade in dict2.items()})
    return novo_dicionario

dict1 = { "Matheus" :23, "Brenno" : 53}

dict2 = {"Alice" : 36,"Gabi" : 16,"Alex" : 27}

novo_dicionario = mesclar_dicionario(dict1,dict2)
print(novo_dicionario)