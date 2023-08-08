"""Crie um programa que funcione como uma agenda de contatos simples. 
O programa deve permitir adicionar novos contatos, atualizar informações existentes, remover contatos e buscar informações de um contato específico (por exemplo, por nome). 
Use um dicionário para armazenar os contatos, onde as chaves são os nomes e os valores são dicionários contendo informações como número de telefone, e-mail, etc."""


import json

# Especifique o caminho completo para o arquivo JSON
caminho_arquivo = r"C:\Users\estef\Documents\Python\Estruturas_de_dados\Dicionario\Exercicio\contatos.json"


# Carregar contatos do arquivo (se existir)
try:
    with open(caminho_arquivo, "r") as arquivo:
        agenda = json.load(arquivo)  # Carrega o conteúdo do arquivo JSON para a variável 'agenda'
except FileNotFoundError:
    agenda = {}  # Cria um dicionário vazio 'agenda' se o arquivo não existir

def adicionar_contato():
    nome = input("Digite o nome do contato que deseja adicionar: ")
    telefone = int(input("Digite o número do contato: "))
    email = input("Digite o e-mail do contato: ")
    
    novo_contato = {
        "Telefone": telefone,
        "email": email
    }
    
    agenda[nome] = novo_contato  # Adiciona o novo contato ao dicionário 'agenda'
    
    # Salvar os contatos no arquivo
    with open("contatos.json", "w") as arquivo:
        json.dump(agenda, arquivo, indent=4)  # Salva o dicionário 'agenda' no arquivo JSON

adicionar_contato()  # Chama a função para adicionar um novo contato

# Imprimir todos os contatos na agenda
for nome, contato in agenda.items():
    print("Nome:", nome)
    print("Telefone:", contato["Telefone"])
    print("Email:", contato["email"])
    print()


#proxima etapa armezar os contatos em arquivos JSON (estudar JSON)