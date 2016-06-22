from sqlobject import *
import sys, os
'''
Created on 17 de jun de 2016

@author: sergio
'''

'''
sqlite:///full/path/to/database
sqlite:/C:/full/path/to/database
sqlite:/:memory:
'''



#db_caminho_banco = 'C:/PythonSQL/bancodedados.db'
#db_caminho_banco = 'bancodedados.db'
#db_filename_sqllite =  'sqlite:/' + db_caminho_banco
#sqlhub.processConnection = connectionForURI('sqlite:/:memory:')

#db_filename = os.path.abspath('data.db')

#db_filename = os.path.abspath('data.db')
#db_filename = 'cbancodedados.db'
db_filename = 'C:/PythonSQL/'

if os.path.exists(db_filename):
    print("existe")
    os.unlink('C:/PythonSQL/')
else:
    print("Nao existe")
    print("Criando...")
    os.mkdir('C:/PythonSQL/')
    print("Criado...")    

connection_string = 'sqlite:' + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

print("Conexao relizada com sucesso")
class Person(SQLObject):
    fname = StringCol()
    mi = StringCol(length=1, default=None)
    lname = StringCol()

Person.createTable()

print("Tudo Certo")