#sys.path é uma variável embutida no módulo sys. 
# Ele contém uma lista de diretórios que o interpretador irá pesquisar para o módulo necessário. 
#Quando um módulo (um módulo é um arquivo Python) é importado dentro de um arquivo Python, o interpretador primeiro procura o módulo especificado entre seus módulos integrados. 
# Se não for encontrado, ele verifica a lista de diretórios (um diretório é uma pasta que contém módulos relacionados) definida por sys.path
import sys 
sys.path.append('C:/Users/Vanshi/Desktop') 
sys.path 