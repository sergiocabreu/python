'''
Created on 23 de jun de 2016

@author: sergio
'''
from sqlobject import *


def criar_tabelas():
    Rodada.createTable(ifNotExists=True)

class Rodada(SQLObject):
    jogo = StringCol()
    rodada = StringCol()
    data = StringCol()
    mandate = StringCol()
    placar = StringCol()
    visitante = StringCol()
    estadio = StringCol()