from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.chrome.options import Options 
import openpyxl
import time



arquivo_planilha_teste = openpyxl.load_workbook(r"C:\Users\estef\Documents\Python\Projeto_quality_automatizacao\Planilha teste.xlsx")
#Abrindo o aquivo .xlsx 

planilha_teste = arquivo_planilha_teste['Planilha']
#Selecionando a planilha do arquivo


valores_coluna = []
#Lista onde será armazenado todas as notas fiscais da planilha 

for linha in planilha_teste.iter_rows(min_row=3, min_col=12, values_only=True):
    valores = int(linha[0])
    valores_coluna.append(valores)
    
    '''Buscador(iterador) do número das notas fiscais na planilha selecionada . 
    Usando parâmetros  para indicar a linha "min_row=3" e a coluna "min_col=12" que queremos começar a iterar . "
    "values_only=True" é um parâmetro para retorna apenas o valor da célula .
    Vai ler todas as células que estiverem preenchidas, o número será armazenar numa lista,
    e essa lista será usado como referência pro selenium 
    puxar o número da nota da lista para o sistema da Quality
    '''

#options = Options()
#options.add_experimental_option("detach", True)
#nav = webdriver.Chrome(options=options)
# Essa opção permite que a janela do navegador Chrome permaneça aberta mesmo após o término da execução do script Selenium. (Caso seja melhor pesquisar as notas fiscais abrindo o navegador apenas uma vez )

for notafiscal in valores_coluna :
#Iterando sobre o valor da lista criada acima(Que são os números das notas fiscais)

    nav = webdriver.Chrome()
    nav.get("https://sistema.qualityentregas.com.br/") 
    nav.find_element(By.NAME, "FsLogin").send_keys("estefano.davel")
    nav.find_element(By.NAME, "FsSenha").send_keys("flamengo123")
    nav.find_element(By.NAME, "FbEnviar").click()   
    nav.find_element(By.NAME, "FsPesquisa").send_keys(notafiscal)
    nav.find_element(By.NAME, "FsPesquisa").send_keys(Keys.ENTER)

    time.sleep(8)
    #timezinho apenas para ilustrar o funcionamento do script 
    
    nav.quit()





