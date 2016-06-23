# coding: iso-8859-15

import urllib
from bs4 import BeautifulSoup



print("inicio")
url='http://www.cbf.com.br/competicoes/brasileiro-serie-a/tabela/2015#.V2rx6_krKCg'
#url = 'http://www.dicionariodoaurelio.com/'
f = urllib.request.urlopen(url)

print("recuperou url")

html_doc = f.read()
print("leu arquivo")

soup = BeautifulSoup(html_doc,"html5lib")
print("converteu para soup")


#resultado = soup.find(attrs={'class':'table table-striped table-condensed visible-print'})

tabela = soup.find(attrs={'class':'table table-striped table-condensed visible-print'})

linhas  =  tabela.findAll("tr")

for linha in linhas:    
    colunas = linha.findAll('td')
#    states=linha.findAll('th')
    if len(colunas) == 8:
        celula1 = colunas[0].find(text=True)
        celula2 = colunas[1].find(text=True)
        celula3 = colunas[2].find(text=True)
        celula4 = colunas[3].find(text=True)    
        celula5 = colunas[4].find(text=True)
        celula6 = colunas[5].find(text=True)
        celula7 = colunas[6].find(text=True)    
        #celula8 = colunas[7].find(text=True)
    
        print("Jogo: " + celula1)
        print("Rodada: " + celula2)
        print("Data: " + celula3)
        print("Mandante: " + celula4)
        print("Placar: " + celula5)
        print("Visitante: " + celula6)
        print("Estadio: " + celula7)
        print("\n")



#print(soup.find('table'))


