from random import randint
class Pessoa:
    ano_atual = 2019
    #Métodos de instância da classe
    
    def __init__(self,nome , idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self,idade):
        print(self.ano_atual - self.idade)
    
    #Métodos da classe em si, funciona no escopo geral da classe
    
    @classmethod
    def por_ano_nascimento(cls , nome , ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome , idade)
    
    #Método da static , funciona como uma função normal, que não usa a instãncia e nem a classe
    
    @staticmethod
    def gera_id():
        id = randint(1000 , 9999)
        return id


#p1 = Pessoa.por_ano_nascimento("Estéfano", 2000)

p1 = Pessoa ("Estéfano" , 65)
p1.get_ano_nascimento(65)
print(p1.gera_id())
print(Pessoa.gera_id())



    
