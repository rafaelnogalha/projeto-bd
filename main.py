from database import cursor, db

def criar_usuario(nome, senha, email):
  sql = ("INSERT INTO usuario(nome, senha, email) VALUES (%s, %s, %s)")
  cursor.execute(sql, (nome, senha, email))
  db.commit()
  id_usuario = cursor.lastrowid
  print("Usuario criado {}".format(id_usuario))
  
def selecionar_usuarios():
  sql = ("SELECT * FROM usuario ORDER BY criado DESC")
  cursor.execute(sql)
  results = cursor.fetchall()
  
  for row in results:
    print(row)

def selecionar_usuario(id_usuario):
  sql = ("SELECT * FROM usuario WHERE id_usuario = %s")
  cursor.execute(sql, (id_usuario,))
  result = cursor.fetchone()
  
  print(result)
  
def atualizar_usuario_senha(id_usuario, nova_senha):
  sql = ("UPDATE usuario SET senha = %s WHERE id_usuario = %s")
  cursor.execute(sql, (nova_senha, id_usuario,))
  db.commit()

  print("Senha atualizada para usuario com id {}".format(id_usuario))

def deletar_usuario(id_usuario):
  sql = ("DELETE FROM usuario WHERE id_usuario = %s")
  cursor.execute(sql, (id_usuario,))
  db.commit()

  print("Usuario com id {} deletado".format(id_usuario))

# criar_usuario('Christopher', 'pAsSwOrD', 'christopher@gmail.com')
# criar_usuario('John', 'doe123', 'john@gmail.com')
# criar_usuario('Jane', 'hello123', 'jane@gmail.com')
# criar_usuario('Joao', 'pAsSwOrD', 'christopher@gmail.com')
# criar_usuario('Joao', 'pAsSwOrD', 'joao@gmail.com')
# atualizar_usuario_senha(1, 'myNeWpAsSwOrD')
# deletar_usuario(1)
# selecionar_usuarios()