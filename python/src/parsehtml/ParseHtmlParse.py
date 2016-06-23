'''
Created on 23 de jun de 2016

@author: sergio
'''


import urllib
from bs4 import BeautifulSoup
from cgitb import text
def getHtml():
    html_data = '''
        <html>
            
            <body>
                <table class="table table-striped table-condensed visible-print">
                    <tr> 
                        <td>linha 1 coluna 1</td>
                        <td>linha 1 coluna 2</td>
                    </tr>
                    <tr> 
                        <td>linha 2 coluna 1</td>
                        <td>linha 2 coluna 2</td>
                    </tr>
                    <tr> 
                        <td>linha 3 coluna 1</td>
                        <td>linha 3 coluna 2</td>
                    </tr>
                    <tr> 
                        <td>linha 4 coluna 1</td>
                        <td>linha 4 coluna 2</td>
                    </tr>                                                            
                </table>
            </body>
        </html>'''
        
    return html_data



soup = BeautifulSoup(getHtml(),"html5lib")

#print(soup)
#print(soup.find('table'))

##for tr in soup.findAll('tr'):
##  print(tr)
tabela = soup.find(attrs={'class':'table table-striped table-condensed visible-print'})

linhas  =  tabela.findAll("tr")

for linha in linhas:
    colunas = linha.findAll('td')
    celula1 = colunas[0].find(text=True)
    celula2 = colunas[1].find(text=True)
    print(celula1)
    print(celula2)
pass







