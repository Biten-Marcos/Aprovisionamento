#importando formularios=====================================================================
from PyQt5 import uic,QtWidgets
import sys
from MODULOS.funcoes import Logon, mainw
from INTERFACES.login import Ui_Login
from INTERFACES.telaPrincipal import Ui_MainWindow
app=QtWidgets.QApplication([])


#===========================================================================================
login_widget = QtWidgets.QWidget()  # Criando o QWidget
login = Ui_Login()                  # Instanciando a classe Ui_Login
login.setupUi(login_widget)         # Configurando a interface no QWidget

telaPrincipal_widget = QtWidgets.QMainWindow()  # Usando QMainWindow ao invés de QWidget
telaPrincipal = Ui_MainWindow()
telaPrincipal.setupUi(telaPrincipal_widget)         # Configurando a interface no QWidget
#funções====================================================================================





    
#============================================================================================

login.pushButton.clicked.connect(lambda:Logon.adm1(telaPrincipal, telaPrincipal_widget, login, login_widget))



#telaPrincipal.pushButton_5.clicked.connect(lambda:mainw.sair(telaPrincipal_widget, login_widget, login))

telaPrincipal.pushButton_5.clicked.connect(lambda: mainw.sair(telaPrincipal_widget, login, login_widget))

login_widget.show()      
Logon.inicializar_login(login)
app.exec()


