#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
#Imprima a idade e a altura na ordem inversa a ordem lida.

lista_idade = []
lista_altura = []
for i in range(5):
    altura = float(input(f"Pessoa {i+1} digite sua altura: "))
    lista_altura.append(altura)
    
    idade = int(input(f"Pessoa {i+1} digite sua idade: "))
    lista_idade.append(idade)

def inverte_e_imprime():
    lista_idade_invertida =lista_idade[::-1]
    lista_altura_invertida = lista_altura[::-1]
    print("Lista de altura : ", lista_altura_invertida)
    print("Lista de idade : ", lista_idade_invertida)

    print("Lista de altura:")
    for altura in lista_altura_invertida:
        print(f"{altura} metros")
    
    print("Lista de idade:")
    for idade in lista_idade_invertida:
        print(f"{idade} anos")


inverte_e_imprime()