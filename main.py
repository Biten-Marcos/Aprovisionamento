#importando formularios=====================================================================
from PyQt5 import uic,QtWidgets
import sys
from MODULOS.funcoes import Logon, mainw
from INTERFACES.login import Ui_Login
from INTERFACES.telaPrincipal import Ui_MainWindow
from MODULOS.cadastrar import  cadastrar
app=QtWidgets.QApplication([])


#===========================================================================================


login_widget = QtWidgets.QWidget()  # Criando o QWidget
login = Ui_Login()                  # Instanciando a classe Ui_Login
login.setupUi(login_widget)         # Configurando a interface no QWidget

telaPrincipal_widget = QtWidgets.QMainWindow()  # Usando QMainWindow ao invés de QWidget
telaPrincipal = Ui_MainWindow()
telaPrincipal.setupUi(telaPrincipal_widget)         # Configurando a interface no QWidget


#DANDO NOMES PARA AS TELAS DO STACKED WINDOW====================================================================================

tabela = telaPrincipal.pg_Tabela
logo = telaPrincipal.pg_Logo
cadastroColab = telaPrincipal.pg_CadastroColaborador
CadastroUser = telaPrincipal.pg_CadastroUser

#============================================================================================

login.pushButton.clicked.connect(lambda:Logon.adm1(telaPrincipal, telaPrincipal_widget, login, login_widget))



#telaPrincipal.pushButton_5.clicked.connect(lambda:mainw.sair(telaPrincipal_widget, login_widget, login))

telaPrincipal.pushButton_5.clicked.connect(lambda:mainw.sair(telaPrincipal_widget, login, login_widget))
telaPrincipal.pushButton_8.clicked.connect(lambda:mainw.tabela(telaPrincipal, tabela))
telaPrincipal.pushButton_16.clicked.connect(lambda:mainw.logo(telaPrincipal,logo))
telaPrincipal.pushButton_3.clicked.connect(lambda:mainw.cadastroColab(telaPrincipal,cadastroColab))
telaPrincipal.pushButton_4.clicked.connect(lambda:mainw.cadastroUser(telaPrincipal,CadastroUser))
telaPrincipal.pushButton_14.clicked.connect(lambda: cadastrar.add(telaPrincipal))
telaPrincipal.pushButton_20.clicked.connect(lambda: cadastrar.limpar(telaPrincipal))

login_widget.show()      
Logon.inicializar_login(login)
app.exec()


