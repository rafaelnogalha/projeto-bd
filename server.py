# import http.server
# import socketserver

# PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

from http.server  import BaseHTTPRequestHandler, HTTPServer
import mysql.connector as connector
from flask import Flask

config = {
  'user': 'root',
  #'password': 'L@g0n1c0',
  'password': 'mysql12',
  'host': 'localhost',
  'database': 'redeSocial' # tirar para estabelecer conexao, colocar para acessar o baanco de dados
}

db = connector.connect(**config)
cursor = db.cursor()

app = Flask(__name__)
#cnx = mysql.connector.connect(user='root', password = 'mysql12', host = '127.0.0.1', port = '3306', database = 'redesocial')
#cursor = cnx.cursor()

@app.route('/')
def hello_world():
    return 'Hello Tutorialspoint'

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        # Assuming the value to insert is just provided in the URL
        # path. e.g., "http://127.0.0.1/<val>"
        i_slash = self.path.index('/')
        val = self.path[(i_slash + 1):]
        #criar_usuario("Pedro, senha, pedro@gmail.com")


def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    app.run()
    #criar_usuario("pedro", "senha", "pedro@gmail.com")
    httpd.serve_forever()

#@app.route('/')
# def insert(val):
#     #cursor.execute("INSERT INTO t_events (eid) VALUES ('%s');" % val)
#     cursor.execute("INSERT INTO usuario VALUES ('%s %s %s');" "pedro", "senha", "pedro@gmail.com")
#     print("inseriu")

# def criar_usuario(nome, senha, email):
#   sql = ("INSERT INTO usuario(nome, senha, email) VALUES (%s, %s, %s)")
#   cursor.execute(sql, (nome, senha, email))
#   db.commit()
#   id_usuario = cursor.lastrowid
#   print("Usuario criado {}".format(id_usuario))

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))

    else:
        run()


