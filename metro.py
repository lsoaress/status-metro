import requests
from bs4 import BeautifulSoup


def inicializar():
    r = requests.get("https://www.viamobilidade.com.br/")
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


nomeLinhas = ['Linha 1 - Azul', 'Linha 2 - Verde', 'Linha 3 - Vermelha', 'Linha 4 - Amarela', 'Linha 5 - Lilás', 'Linha 7 - Rubi', 'Linha 8 - Diamante', 'Linha 9 - Esmeralda', 'Linha 10 - Turquesa', 'Linha 11 - Coral', 'Linha 12 - Safira', 'Linha 13 - Jade', 'Linha 15 - Prata']
txtStatus = []
corStatus = []

def filtrar_linhas():

    soup = inicializar()
    numLinhas = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15]
    for x in numLinhas:
        elementos_li = soup.find_all("li", class_=f"line-{x}")
        
        for elemento_li in elementos_li:
            div_da_linha = elemento_li.find("div", class_="status")
            
            if div_da_linha:
                txtStatus.append(div_da_linha.text)
                corStatus.append(div_da_linha['class'][1])



def montar_txt():
    filtrar_linhas()
    res = ''
    for x in range(len(nomeLinhas)):
        cor_emoji = ''
        if corStatus[x] == 'verde':
            cor_emoji = "\U0001F7E2"
        elif corStatus[x] == 'amarelo':
            cor_emoji = '\U0001F7E1'
        else:
            cor_emoji = '\U0001F534'
        res += f'{nomeLinhas[x]} : {cor_emoji}\n' 

    return res
