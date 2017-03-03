# coding: iso-8859-15
"""Realiza testes com o modulo pyoo 1.2
Manipulação do Libre office Calc
"""
from pyexcel_ods3 import get_data

if __name__ == "__main__":
    print('inicio')
    ARQUIVO_ODS = get_data('C:\\arquivo_com_planilha.ods')

    #pode trabalhar com json.
    #resultado_json = json.dumps(ARQUIVO_ODS)

    PLANILHA = ARQUIVO_ODS['Planilha1']
    
    QUEBRA_LINHA = '\n'
    RESULTADO = ''
    for linha in PLANILHA:
        coluna1 = linha[0]
        RESULTADO += coluna1 + QUEBRA_LINHA

    #salva em um arquivo
    ARQUIVO = open('C:\\resultado_gravado.sql', 'w')
    ARQUIVO.write(RESULTADO)
    ARQUIVO.close()
    print('fim')
