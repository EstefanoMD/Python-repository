"""
A compreensão de dicionário (dictionary comprehension) em Python é uma construção concisa que permite criar dicionários de forma eficiente em uma única linha de código. 
Assim como as list comprehensions, as dictionary comprehensions são uma maneira elegante e poderosa de criar dicionários de forma mais compacta.
"""

#A estrutura geral de uma dictionary comprehension é a seguinte:

#novo_dicionario = {chave: valor for elemento in sequencia}

"""
chave é a expressão que define a chave para cada par chave-valor no novo dicionário.
valor é a expressão que define o valor correspondente para cada par chave-valor.
elemento é cada item na sequência de onde as chaves e valores serão extraídos.
"""


#Aqui está um exemplo simples de uma dictionary comprehension que cria um novo dicionário com o dobro dos valores de um dicionário original:

dicionario_original = {"a": 1, "b": 2, "c": 3}
dicionario_dobrado = {chave: valor * 2 for chave, valor in dicionario_original.items()}
print(dicionario_dobrado)  # Saída: {'a': 2, 'b': 4, 'c': 6}
