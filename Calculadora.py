import math

def Somar(*num):
    numeros_soma =[]
    n1 = int(input("Digite o 1 número: ")) 
    numeros_soma.append(n1)
    n2 = int(input("Digite o 2 número: "))
    numeros_soma.append(n2)
    c  = 2
    acrescenta_numero = input("Deseja acrescentar mais número ? (S) para sim e (N) para não? \n").upper()
    if acrescenta_numero == 'S':
        while acrescenta_numero == 'S':
            c += 1
            num  = int(input(f"\nDigite outro número: "))
            numeros_soma.append(num)
            acrescenta_numero = input("Deseja acrescentar mais número ? (S) para sim e (N) para não? \n").upper()
        return print(f"O resultado da operação é :\n{sum(numeros_soma)}")
    else :
        return print(f"O resultado da operação é :\n{sum(numeros_soma)}")
def Subtrai(*num):
        numeros_sub = []
        n1 = int(input("Digite o 1 número: ")) 
        numeros_sub.append(n1)
        n2 = int(input("Digite o 2 número: "))
        numeros_sub.append(n2)
               
        acrescenta_numero = input("Deseja acrescentar mais número ? (S) para sim e (N) para não? \n").upper()
        if acrescenta_numero == 'S':
            while acrescenta_numero == 'S':
                num  = int(input(f"\nDigite outro número: "))
                numeros_sub.append(num)
                acrescenta_numero = input("Deseja acrescentar mais número ? (S) para sim e (N) para não? \n").upper()                
            
            numeros_sub,*tail = numeros_sub
            for a in tail:
                numeros_sub -= a
            return print(numeros_sub)        
        else:
            numeros_sub,*tail = numeros_sub
            for a in tail:
                numeros_sub -= a
            return print(numeros_sub)
def Dividi(*num):
    n1 = int(input("Digite o 1 número: ")) 
    n2 = int(input("Digite o 2 número: "))   
    print(n1 / n2)
    
    repete_operacao = input("Deseja fazer uma nova operação  ? (S) para sim e (N) para não? \n").upper()
    if repete_operacao == 'S':
        while repete_operacao == 'S':
                n1 = int(input("Digite o 1 número: ")) 
                n2 = int(input("Digite o 2 número: "))
                print(n1 / n2)
                repete_operacao = input("Deseja fazer uma nova operação  ? (S) para sim e (N) para não? \n").upper()

    elif repete_operacao == 'N':
        print("Operação encerrada!")
def Multiplica(*num):
    numeros_multiplicacao =[]
    n1 = int(input("Digite o 1 número: ")) 
    numeros_multiplicacao.append(n1)
    n2 = int(input("Digite o 2 número: "))
    numeros_multiplicacao.append(n2)
    c  = 2
    acrescenta_numero = input("Deseja acrescentar mais número ? (S) para sim e (N) para não? \n").upper()
    if acrescenta_numero == 'S':
        while acrescenta_numero == 'S':
            c += 1
            num  = int(input(f"\nDigite outro número: "))
            numeros_multiplicacao.append(num)
            acrescenta_numero = input("Deseja acrescentar mais número ? (S) para sim e (N) para não? \n").upper()
        return print(f"O resultado da operação é :\n{math.prod(numeros_multiplicacao)}")
    else :
        return print(f"O resultado da operação é :\n{sum(numeros_multiplicacao)}")
def Linhas():
    print("=-"*30)
def Cabecalho():
    Linhas()
    print("Calculadora iniciada!")
    Linhas()
    print("Adição - digite (+)")
    print("Subtração - digite (-)")
    print("Divisão - digite (/)")
    print("Multiplicação - digite (*)")

Cabecalho()

operacao = str(input("Escolha qual operação deseja realizar: "))

if operacao == "+":
    Linhas()
    
    print("Adição selecionado!")
    
    Linhas()
    
    Somar()
elif operacao == "-":  
    Linhas()
    
    print("Subtração selecionado!")
    
    Linhas()
    Subtrai()
elif operacao == "/":
    Linhas()
    
    print("Divisão selecionado!")
    
    Linhas()
    Dividi()
elif operacao == "*":
    Linhas()
    
    print("Multiplicação selecionado!")
    
    Linhas()
    Multiplica()




        










