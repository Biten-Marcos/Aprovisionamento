#importando formularios=====================================================================
from PyQt5 import uic,QtWidgets

app=QtWidgets.QApplication([])
login = uic.loadUi(r"C:\Users\6501510\OneDrive - Sotreq\Documents\SISTEMA DE CONFERÊNCIA DE PEÇAS\INTERFACES\login.ui")

tela_Principal = uic.loadUi(r"C:\Users\6501510\OneDrive - Sotreq\Documents\SISTEMA DE CONFERÊNCIA DE PEÇAS\INTERFACES\tela_principal.ui")
#===========================================================================================

import sys
from MODULOS.funcoes import Logon, mainw

#funções====================================================================================





    
#============================================================================================

login.pushButton.clicked.connect(lambda:Logon.adm1(tela_Principal, login))



tela_Principal.pushButton_5.clicked.connect(lambda:mainw.sair(tela_Principal, login))



login.show()
Logon.inicializar_login(login)
app.exec()


