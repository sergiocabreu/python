from sqlobject import *
import sys, os
from bancodedados import entidades

db_banco = 'sqlite:/'
db_filename = 'bancodedados.db'
db_diretorio = 'C:/PythonSQL/'


def criar_banco():
    
    if os.path.exists(db_diretorio+db_filename):
        os.unlink(db_diretorio+db_filename)
    else:
        os.mkdir(db_diretorio)

    connection_string = db_banco + db_diretorio + db_filename
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection

    entidades.criar_tabelas()
