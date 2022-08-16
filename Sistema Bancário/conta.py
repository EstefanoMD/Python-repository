from abc import ABC, abstractmethod
class Conta(ABC):
    def __init__(self, agencia=int , limite=float , numero_conta=int , saldo=float):
        self._agencia = agencia
        self._limite = limite
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.getter
    def saldo(self ):
        return self._saldo
        
    def ExibirExtrato(self):
        limite_total = self._limite
        print(f"Agência : {self._agencia} \nNúmero de conta : {self._numero_conta} \nSaldo : {self._saldo} \nLimite dispónivel : {self._limite} / {limite_total}")

    
    def depositar(self,valor):
        self._saldo += valor
        return self._saldo
    
    @abstractmethod
    def sacar (self, valor ):
        pass

class ContaCorrente(Conta):
            def sacar(self,valor=float):
                if  valor > (self._saldo + self._limite) :
                    print("Valor insuficiente!")
                    return
                
                elif  valor <= self._saldo :
                    self._saldo -= valor
                    print("Saque realizado com sucesso!")
                    return
                
                elif valor <= (self._saldo + self._limite):
                    self._limite = self._limite - valor 
                    if (self._saldo - valor) < 1:
                        self._saldo = 0 

                    print("Saque realizado com limite com sucesso!")

class ContaPoupança(Conta):
    def sacar(self,valor):
        if self._saldo < valor:
            print("Valor insuficiente!")
            return
        
        
        self._saldo -= valor
        self.ExibirExtrato()
           
            
                
    

    
