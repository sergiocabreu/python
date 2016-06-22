# coding: iso-8859-15

import urllib
from bs4 import BeautifulSoup

url = 'http://www.dicionariodoaurelio.com/'
f = urllib.request.urlopen(url)
html_doc = f.read()
soup = BeautifulSoup(html_doc)
print(soup)
