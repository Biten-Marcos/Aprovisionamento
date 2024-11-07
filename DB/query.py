#id, PRIMATY KEY AUTOICREMENT
# nome, TEXT
# usuário, TEXT
# senha, TEXT
# tipo de perfil, INTEGER
import sqlite3
from MODULOS.funcoes import Logon

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
    

    def captura_login(login, telaPrincipal, telaPrincipal_widget, login_widget):
        db = sqlite_db("Users.db")
        usu = login.lineEdit.text()
        senh = login.lineEdit_2.text()  
        print("indo para a função")
        db.check_user(usu, senh,telaPrincipal, telaPrincipal_widget, login_widget) 
        
        
        
        
        
        
        
    def ver_Perfil(Perfil, Nome, Matricula, Função, telaPrincipal, telaPrincipal_widget, login_widget):
        if Perfil == "Adm":
            Logon.login_Adm(telaPrincipal, telaPrincipal_widget, login_widget)
        elif Perfil == "Padrão":
            Logon.login_Padrao(Nome, Matricula, Função, telaPrincipal, telaPrincipal_widget, login_widget)
            
    
            

    

    def check_user(self, usu, senh, telaPrincipal, telaPrincipal_widget, login_widget):
        
        try:
            print ("try")
            cur = db.cursor
            cur.execute("""
             
                SELECT * FROM USUARIOS;
            
            """)
            
            for coluna in cur.fetchall():
                #if coluna[2].upper() == usu.upper() and coluna[3].upper() == senh.upper() and coluna[4] == 0:
                print("1")
                if coluna[2].upper() == usu.upper() and coluna[3].upper() == senh.upper():
                    if coluna[4] == 1:
                        Perfil = "Adm"
                        Nome = coluna[1]
                        Matricula = coluna[2].upper()
                        Função = "Aprovisionador"
                        sqlite_db.ver_Perfil(Perfil, Nome, Matricula, Função, telaPrincipal, telaPrincipal_widget, login_widget)
                    else:
                        Perfil = "Padrão"
                        Nome = coluna[1]
                        Matricula = coluna[2].upper()
                        Função = "Aprovisionador"
                        sqlite_db.ver_Perfil(Perfil, Nome, Matricula, Função, telaPrincipal, telaPrincipal_widget, login_widget)
                continue
            return "Sem acesso"
        except:
            pass





db = sqlite_db("Users.db")


#db.criar_tabelas()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

