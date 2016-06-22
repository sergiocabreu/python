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

soup = BeautifulSoup(html_doc)
print("converteu para soup")

#print(soup)
print(soup.find('table'))
