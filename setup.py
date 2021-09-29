from mysql.connector import errorcode
import mysql.connector as connector
from database import cursor

DB_NAME = 'redeSocial'

TABLES = {}

TABLES['users'] = (
    "CREATE TABLE `users` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `username` varchar(255) NOT NULL,"
    " `password` varchar(255) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
  cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
  print("Database {} created!".format(DB_NAME))

def create_tables():
  cursor.execute("USE {}".format(DB_NAME))

  for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
      print("Creating table ({})".format(table_name))
      cursor.execute(table_description)
    except connector.Error as err:
      if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Table ({}) already exists".format(table_name))
      else:
        print(err.msg)


create_database()
create_tables()