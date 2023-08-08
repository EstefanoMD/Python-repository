#Foram anotadas as idades e alturas de 30 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random 

def idades():
    lista_de_idade = []
    for i in range(30):    
        idade_aleatoria = random.randrange(8,16)
        lista_de_idade.append(idade_aleatoria)
    
    print(lista_de_idade)

    return lista_de_idade

def altura():
    lista_de_altura = []
    for i in range(30):    
        altura_aleatoria = random.uniform(1.30,1.90)
        altura_aleatoria = round(altura_aleatoria, 2)
        lista_de_altura.append(altura_aleatoria)
    
    media_altura = sum(lista_de_altura)/len(lista_de_altura)
    media_altura = round(media_altura,2)
    
    print(f"Lista de altura : {lista_de_altura}")
    print(f"Média de altura : {media_altura}")
    
    return media_altura, lista_de_altura

lista_de_idade = idades()
media_altura ,lista_de_altura = altura()

contador = 0
for i , j in zip(lista_de_idade, lista_de_altura):
    
    if i > 13 and j < media_altura :
        contador +=  1

print("Alunos com mais de 13 anos e com altura inferior a média : ", contador)