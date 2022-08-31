import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'

response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

print(html)