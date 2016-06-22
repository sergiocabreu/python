from sqlobject import *
import sys, os

'''db_caminho_banco = 'C:/PythonSQL/bancodedados.db'
db_filename_sqllite =  'sqlite:/' + db_caminho_banco
print(db_filename_sqllite)


print("Sergio")

db_filename = os.path.abspath('data.db')
print(db_filename)'''
from fileinput import filename


db_filename = os.path.abspath('data.db')
print(db_filename)
if os.path.exists(db_filename):
    os.unlink(db_filename)
else:
    print("Nao existe")
connection_string = 'sqlite:' + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection