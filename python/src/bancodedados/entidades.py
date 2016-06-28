'''
Created on 23 de jun de 2016

@author: sergio
'''
from sqlobject import *


class Rodada(SQLObject):
        
    jogo = StringCol()
    rodada = StringCol()
    data = StringCol()
    mandante = StringCol()
    placar = StringCol()
    visitante = StringCol()
    estadio = StringCol()
    
def criar_tabelas():
    Rodada.createTable(ifNotExists=True)