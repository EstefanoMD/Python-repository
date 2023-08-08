def contar_letras():
    qualquer_coisa = input("Digite qualquer coisas:")
    dic_letras = {}
    for letra in qualquer_coisa :
        dic_letras[letra] = dic_letras.get(letra,0) + 1
    print(dic_letras)

contar_letras()