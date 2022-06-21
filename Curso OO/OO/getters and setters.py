
class Produto:
    def __init__(self , nome , preco):
        self.preco = preco
        self.nome = nome

    def desconto(self,percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self , valor):
        self._nome = valor.title()
    
    
    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$' , ''))
        self._preco = valor



p1 = Produto("CAMISA" , 15)
p1.desconto(10)
print(p1.nome,p1.preco)
p2 = Produto("CENEKÃO - PERSONALIZADO" , 'R$12')
p2.desconto(10)
print(p2.nome , p2.preco)