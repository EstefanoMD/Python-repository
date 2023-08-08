#Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
def calcular_media(notas):
    return sum(notas) / len(notas)

alunos_com_media_maior_que_sete = 0

quantidade_alunos = int(input("Digite a quantidade de aluno : "))  
for i in range(quantidade_alunos):
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {i+1} : "))
        notas_aluno.append(nota)

    media_aluno = calcular_media(notas_aluno)
    print(f"Média do aluno {i+1} : {media_aluno:.2f}")

    if media_aluno > 7.0:
        alunos_com_media_maior_que_sete += 1
print(f'Números de alunos com média maior  ou igual a 7.0: {alunos_com_media_maior_que_sete}')