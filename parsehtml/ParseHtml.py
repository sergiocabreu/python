# coding: iso-8859-15

import urllib
from bs4 import BeautifulSoup
from bancodedados.entidades import Rodada


def parse_no_banco():
    url='http://www.cbf.com.br/competicoes/brasileiro-serie-a/tabela/2015#.V2rx6_krKCg'

    f = urllib.request.urlopen(url)

    html_doc = f.read()
    
    soup = BeautifulSoup(html_doc,"html5lib")

    tabela = soup.find(attrs={'class':'table table-striped table-condensed visible-print'})

    linhas  =  tabela.findAll("tr")

    for linha in linhas:    
        colunas = linha.findAll('td')

        if len(colunas) == 8:
            salvar(colunas)

            
            
            
            

def salvar(colunas):
    c1 = str(colunas[0].find(text=True))
    c2 = str(colunas[1].find(text=True))
    c3 = str(colunas[2].find(text=True))
    c4 = str(colunas[3].find(text=True))    
    c5 = str(colunas[4].find(text=True))
    c6 = str(colunas[5].find(text=True))
    c7 = str(colunas[6].find(text=True))
    
    Rodada(jogo=c1, rodada=c2,  data=c3, mandante=c4, placar=c5, visitante=c6, estadio=c7)
    
    