class Cliente:
    def __init__(self, nome , idade):
        self.nome = nome
        self.nome = idade
        self.enderecos = []

    def insere_enderecos(self , cidade , estado):
        self.enderecos.append(Enderecos(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.cidade)


class Enderecos:
    def __init__(self , cidade , estado): 
        self.cidade = cidade
        self.estado = estado
