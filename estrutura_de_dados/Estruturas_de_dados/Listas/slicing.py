"""o slicing (também conhecido como fatiamento) é uma técnica poderosa para extrair partes específicas de uma sequência, como uma lista, uma string ou uma tupla. 
A ideia básica do slicing é criar uma sub-sequência, selecionando elementos em posições específicas dentro da sequência original"""

# Criando uma lista de exemplo
numeros = [1,2,3,4,5,6,7,8,9,10]

# Extraindo elementos usando slicing
numeros_cortados = numeros[3:9]

print(numeros_cortados)

"""O slicing com índices negativos em Python permite selecionar elementos de uma sequência contando a partir do final, onde -1 representa o último elemento, -2 o penúltimo, e assim por diante. 
Isso oferece uma forma conveniente de acessar elementos no final da sequência."""
 
# Criando uma lista de exemplo
frutas = ["Maça", "Laranja","Uva","Pêssego","Tomate"]

# Selecionando elementos usando slicing
frutas_compradas = frutas[-2:]

print(frutas_compradas)

"""O slicing com steps em Python permite extrair sub-sequências espaçadas de elementos de uma sequência usando a sintaxe sequencia[inicio:fim:passo]. 
Isso é útil para manipular listas, strings e tuplas de forma eficiente."""

# Criando uma lista de exemplo
lista = [1,2,3,4,5,6,7,8,9]

# Editando elementos usando slicing
step_slice = lista[1::2]

print(step_slice)

"""Edição de elementos com slicing em listas permite alterar valores específicos de uma sequência, atribuindo novos elementos a uma subsequência definida pelo slicing. 
É uma técnica eficiente e direta para modificar partes da lista."""


# Criando uma lista de exemplo
lista = [10, 20, 30, 40, 50]

# Editando elementos usando slicing
lista[1:4] = [25, 35, 45]

print(lista)
