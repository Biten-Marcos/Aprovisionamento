#id, PRIMATY KEY AUTOICREMENT
# nome, TEXT
# usuário, TEXT
# senha, TEXT
# tipo de perfil, INTEGER
import sqlite3

#CRIAR BANCO DE DADOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class sqlite_db:
    def __init__(self,banco=None): 
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("conexão criada com sucesso!")
        except sqlite3.Error as e:
            print("Não foi possível estabelecer conexão")

#CRIAR TABELAS
    def criar_tabelas(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE USUARIOS(
            id integer primary key autoincrement,
            nome text NOT NULL,
            usuário text NOT NULL,
            senha text NOT NULL,
            tipo integer
            )""")
        
    def inserir_apaga_atualiza(self, query): 
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def pegaDados(self, query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
    

db = sqlite_db("Users.db")



#db.criar_tabelas()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

