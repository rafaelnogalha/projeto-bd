from mysql.connector import errorcode
import mysql.connector as connector
from database import cursor

DB_NAME = 'redeSocial'

TABLES = {}

TABLES['usuario'] = (
    "CREATE TABLE `usuario` ("
    " `id_usuario` int(11) NOT NULL AUTO_INCREMENT,"
    " `nome` varchar(255) NOT NULL,"
    " `senha` varchar(255) NOT NULL,"
    " `email` varchar(255) NOT NULL,"
    " `criado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id_usuario`),"
    "CONSTRAINT UC_usuario UNIQUE (email)"
    ") ENGINE=InnoDB"
)
TABLES['grupo'] = (
    "CREATE TABLE `grupo` ("
    " `id_grupo` int(11) NOT NULL AUTO_INCREMENT,"
    " `nome` varchar(255) NOT NULL,"
    " `criado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id_grupo`)"
    ") ENGINE=InnoDB"
)
TABLES['grupo_usuario'] = (
    "CREATE TABLE `grupo_usuario` ("
    " `id_grupo_usuario` int(11) NOT NULL AUTO_INCREMENT,"
    " `id_usuario` int(11) NOT NULL,"
    " `id_grupo` int(11) NOT NULL,"
    " `criado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id_grupo_usuario`),"
    "  CONSTRAINT `grupo_usuario_fk_1` FOREIGN KEY (`id_usuario`) "
    "     REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,"
    "  CONSTRAINT `grupo_usuario_fk_2` FOREIGN KEY (`id_grupo`) "
    "     REFERENCES `grupo` (`id_grupo`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

# |grupo_usuario|
# |id   |grupo_id|usuario_id|criado    | 
# |1    |23      |1          12/10/2012|
# |2    |23      |2

def create_database():
  try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Banco de Dados {} criado!".format(DB_NAME))
  except connector.Error as err:
    if err.errno == errorcode.ER_DATABASE_EXISTS_ERROR:
      print("Banco de Dados ({}) jah existe".format(DB_NAME))
    else:
      print(err.msg)

def create_tables():
  cursor.execute("USE {}".format(DB_NAME))

  for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
      print("Criando Tabela ({})".format(table_name))
      cursor.execute(table_description)
    except connector.Error as err:
      if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Tabela ({}) jah existe".format(table_name))
      else:
        print(err.msg)

create_database()
create_tables()