def exerc4():
    notas = []

    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))

    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    notas.append(nota4)
    media = sum(notas)/len(notas)
    print("Nota 1 : ",notas[0], "\nNota 2 : ",notas[1],"\nNota 3 : " ,notas[2],"\nNota 4 : ",notas[3],"\nMédia: ",media)