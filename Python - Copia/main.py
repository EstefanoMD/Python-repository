from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
# from selenium.webdriver.chrome.options import Options 
import openpyxl

# options = Options()
# options.add_experimental_option("detach", True)

nav = webdriver.Chrome()
nav.get("https://sistema.qualityentregas.com.br/") 
elem = nav.find_element(By.NAME, "FsLogin").send_keys("estefano.davel")
elem = nav.find_element(By.NAME, "FsSenha").send_keys("flamengo123")
elem = nav.find_element(By.NAME, "FbEnviar").click()

arquivo_planilha_teste = openpyxl.load_workbook(r"C:\Users\estef\Documents\Python\Projeto_quality_automatizacao\Planilha teste.xlsx")
planilha_teste = arquivo_planilha_teste['Planilha']
valores = int(planilha_teste['L3'].value)
valores_coluna = []

for linha in planilha_teste.iter_rows(min_row=3, min_col=12, values_only=True):
    valores = int(linha[0])
    valores_coluna.append(valores)
    
    elem = nav.find_element(By.NAME, "FsPesquisa").send_keys(linha[0])
    elem = nav.find_element(By.NAME, "FsPesquisa").send_keys(Keys.ENTER)







