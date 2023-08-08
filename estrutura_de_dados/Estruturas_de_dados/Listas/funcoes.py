#Criação de uma lista 
lista_de_compras = []

#Adicionando item em uma lista ao fim da lista
lista_de_compras.append("Banana")

print("------------------------------")
print("Método append")
print("Lista principal após o método" ,lista_de_compras)
print("------------------------------")

#Adcionando um item em uma posição da lista específica
lista_de_compras.insert(0,"Iorgute")

print("------------------------------")
print("Método insert")
print("Lista após o método" ,lista_de_compras)
print("------------------------------")

#Extendendo a lista com uma nova lista
complemento_de_lista = ["Maça","Uva","Biscoito"]
lista_de_compras.extend(complemento_de_lista)

print("------------------------------")
print("Método extend")
print("Itens da outra lista que foram adicionados a lista principal = ",complemento_de_lista )
print("Lista principal após o método" ,lista_de_compras)
print("------------------------------")

#Removendo o item da lista
lista_de_compras.remove("Biscoito")


print("Metódo remove")
print("item removido da lista = Biscoito")
print("itens restantes da lista de compras" ,lista_de_compras)
print("------------------------------")

#Retirando um item específico da lista e ao mesmo tempo retornando o valor desse item, caso o índice não seja específicado, o último da lista será removido

item_removido = lista_de_compras.pop(1)
print("Metódo pop")
print("item removido da lista e armazenado na variavél item_removido = ",item_removido)
print("itens restantes da lista de compras" ,lista_de_compras)
print("------------------------------")

#Método ".clear()" remove todos os itens da lista 

lista_de_compras.clear()

print("Método clear")
print("Lista após o método lista = ", lista_de_compras)
print("------------------------------")

#Método ".count()" devolve a quantidade de vezes que um x item da lista aparece 

lista_de_compras = ["Banana","Banana","Banana","Banana"]
Quantidade_bananas = lista_de_compras.count("Banana")

print("Método count()")
print("Quantidade de bananas armezanadas na varívavel 'quantidade_banana' = " ,Quantidade_bananas)
print("------------------------------")

#Método ".index(x[, start[, end]])" é uma função que busca um certo item da lista e retorna sua posição(índice)

lista_de_compras = ["Fita adesiva" , "Sacaria" , "Plástico bolha" , "Papelão"]
posicao_papelao = lista_de_compras.index("Papelão")

print("Método index()")
print("Índice de item 'Papelão' buscado na lista = " ,posicao_papelao)
print("------------------------------")

#Método ".sort()" é uma função que organiza em ordem crescente ou decrescente uma lista

lista_de_compras = ["Abacaxi" , "Linguiça" , "Mandioca" , "Enérgetico"]
lista_de_compras.sort()

print("Método sort()")
print("lista ordenada em modo crescente = " ,lista_de_compras)

lista_de_compras.sort(reverse=True)

print("lista ordenada em modo decrescente = " ,lista_de_compras)
print("------------------------------")

#Método "sorted()" é uma função que organiza em ordem crescente ou decrescente uma lista, sem alterar a lista original

lista_de_compras = ["HB20" , "Relógio" , "Tênis" , "Cadeira"]
lista_de_compra_ordenada = sorted(lista_de_compras)

print("Método sorted()")
print("lista ordenada em modo crescente = " ,lista_de_compra_ordenada)
print("lista original = " ,lista_de_compras)
print("------------------------------")

lista_de_compra_ordenada = sorted(lista_de_compras, reverse=True)

print("lista ordenada em modo decrescente = " ,lista_de_compra_ordenada)
print("lista original = " ,lista_de_compras)
print("------------------------------")

#Método ".reverse()" inverte os itens da lista

lista_de_compras = ["Fita adesiva" , "Sacaria" , "Plástico bolha" , "Papelão"]
lista_de_compras.reverse()

print("Método reverse()")
print("lista invertida " ,lista_de_compras)
print("------------------------------")

#Método "copy()" faz uma cópia rasa da lista

lista_de_compras = ["Fita adesiva" , "Sacaria" , "Plástico bolha" , "Papelão"]
copia_lista_de_compras = lista_de_compras.copy()

print("Método copy()")
print("lista copiada " ,copia_lista_de_compras)
print("------------------------------")