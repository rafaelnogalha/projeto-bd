from database import cursor, db
from flask import Flask, request, jsonify, make_response
import json
# import dart:convert show JSON


def criar_usuario(nome, senha, email):
  sql = ("INSERT INTO usuario(nome, senha, email) VALUES (%s, %s, %s)")
  cursor.execute(sql, (nome, senha, email))
  db.commit()
  id_usuario = cursor.lastrowid
  print("Usuario criado {}".format(id_usuario))
  
# dynamic myEncode(dynamic item) {
#   if(item is DateTime) {
#     return item.toIso8601String();
#   }
#     return item;
# }

def selecionar_usuarios():
  sql = ("SELECT id_usuario,nome,senha,email FROM usuario ORDER BY criado DESC")
  cursor.execute(sql)
  results = cursor.fetchall()
  # json_string = json.dumps({'id_usuario':results[0][0], 'nome': results[0][1]})
  # var str = JSON.encode(dt, toEncodable: myEncode);
  # lst =  [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 

  keys = ['id_usuario', 'nome', 'senha', 'email']

  dicionario = [dict(zip(keys, row)) for row in results]
  
  # for row in results:
  #   json_string = json.dumps({'id_usuario':row[i], 'nome': row[i+1], 'email': row[i+3]})
    #json_string.append(json.dumps({'id_usuario':row[i], 'nome': row[i+1], 'email': row[i+3]}))
  # print(results)
  # usuarios = product_schema.dump(results)
  json_string = json.dumps(dicionario)
  print(json_string['id_usuario'])
  #print(dicionario[0].get('id_usuario'))
  return json_string
#  return results

def selecionar_usuario(id_usuario):
  sql = ("SELECT * FROM usuario WHERE id_usuario = %s")
  cursor.execute(sql, (id_usuario,))
  result = cursor.fetchone()
  # return jsonify(
  #   nome=g.user.username,
  #   email=g.user.email,
  #   id=g.user.id,
  # )
  print(result)
  
def atualizar_usuario_senha(id_usuario, nova_senha):
  sql = ("UPDATE usuario SET senha = %s WHERE id_usuario = %s")
  cursor.execute(sql, (nova_senha, id_usuario,))
  db.commit()

  print("Senha atualizada para usuario com id {}".format(id_usuario))

def deletar_usuario(email):
  sql = ("DELETE FROM usuario WHERE email = %s")
  cursor.execute(sql, (email,))
  db.commit()

  print("Usuario com id {} deletado".format(email))
  
# @app.route('/usuario', methods = ['GET'])
# def index():
#   selecionar_usuario = selecionar_usuarios()
#   product_schema = ProductSchema(many=True)
#   products = product_schema.dump(get_products)
#   return make_response(jsonify({"product": products}))

# criar_usuario('Christopher', 'pAsSwOrD', 'christopher@gmail.com')
# criar_usuario('John', 'doe123', 'john@gmail.com')
# criar_usuario('Jane', 'hello123', 'jane@gmail.com')
# criar_usuario('Joao', 'pAsSwOrD', 'christopher@gmail.com')
# criar_usuario('Joao', 'pAsSwOrD', 'joao@gmail.com')
# atualizar_usuario_senha(1, 'myNeWpAsSwOrD')
# deletar_usuario('christopher@gmail.com')
selecionar_usuarios()