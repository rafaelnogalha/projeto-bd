import mysql.connector as connector

config = {
  'user': 'root',
  'password': 'L@g0n1c0',
  'host': 'localhost'
}

db = connector.connect(**config)
cursor = db.cursor()