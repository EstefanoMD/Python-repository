def media_alunos(notas_alunos):
    media_alunos = {}
    for aluno , notas in notas_alunos.items():
        media = sum(notas)/len(notas)
        media_arredondada = round(media, 2)
        media_alunos[aluno] = media_arredondada

    return media_alunos




notas_alunos = {
    "Ana":[9.2 , 6.4 , 8.8],
    "Paulo":[10.0, 8.4 , 3.9],
    "Roberta":[8.8, 9.6, 10]
}

media = media_alunos(notas_alunos)
print(media)