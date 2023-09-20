import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.viamobilidade.com.br/")

soup = BeautifulSoup(r.content, "html.parser")

numLinhas = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15]

nomeLinhas = []
txtStatus = []
corStatus = []

for x in numLinhas:
    elementos_li = soup.find_all("li", class_=f"line-{x}")
    
    for elemento_li in elementos_li:
        div_da_linha = elemento_li.find("div", class_="status")
        
        if div_da_linha:
            txtStatus.append(div_da_linha.text)
            corStatus.append(div_da_linha['class'][1])

print(corStatus)