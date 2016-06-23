'''
Created on 23 de jun de 2016

@author: sergio
'''
from bancodedados import banco
from bancodedados.entidades import Rodada
from parsehtml.ParseHtml import parse_no_banco

if __name__ == '__main__':
    
    banco.criar_banco()
    print("Banco criado com sucesso")
    parse_no_banco();
    print("Pronto")
    
    
            
    #Rodada(jogo="UM", rodada="DOIS",  data="TRES", mandate="QUATRO", placar="CINCO", visitante="SEIS", estadio="SETE")
    pass