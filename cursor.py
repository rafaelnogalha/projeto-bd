from connection import connection

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE mydatabase")