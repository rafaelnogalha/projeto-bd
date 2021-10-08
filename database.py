import mysql.connector as connector

config = {
  'user': 'root',
  #'password': 
  'password': '',
  'host': 'localhost',
  'database': 'redeSocial' # tirar para estabelecer conexao, colocar para acessar o baanco de dados
}

db = connector.connect(**config)
cursor = db.cursor()
