'''
Created on 28 de jun de 2016

@author: sergio
'''
from bancodedados.entidades import Rodada
from bancodedados.banco import abrir_banco

def jogos_em_casa():
    
    abrir_banco()
    
    rodada = Rodada.select()
    
    total_jogos = len(list(rodada))
    vitoria_mandante = 0
    vitoria_visitante = 0
    empate = 0
    
    for partida in list(rodada):
                                
        placar_mandante = int(partida.placar.split('x')[0])
        placar_visitante = int(partida.placar.split('x')[1])
                
        if placar_mandante > placar_visitante:
            vitoria_mandante+=1
        elif placar_mandante < placar_visitante:
            vitoria_visitante+=1
        else: 
            empate+=1
        
         

    print('Total de jogos: ', total_jogos)
    print('Mandantes     : ', vitoria_mandante)
    print('Visitantes    : ', vitoria_visitante)
    print('Empate        : ', empate)
    print('------------------------------------------')
    print('Mandantes  %  : ', vitoria_mandante * 100 / total_jogos)
    print('Mandantes  %  : ', vitoria_visitante * 100 / total_jogos)
    print('Mandantes  %  : ', empate * 100 / total_jogos)
    
    
    

jogos_em_casa()