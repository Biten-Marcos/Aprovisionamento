#importando formularios=====================================================================
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog

import sys
app=QtWidgets.QApplication([])

#===========================================================================================

class mainw():

    def sair(telaPrincipal_widget, login, login_widget):
        telaPrincipal_widget.hide()
        login_widget.show()
        Logon.inicializar_login(login)

    def tabela(telaPrincipal,tabela):
        telaPrincipal.stackedWidget.setCurrentWidget(tabela)

    def logo(telaPrincipal,logo):
        telaPrincipal.stackedWidget.setCurrentWidget(logo)
    
    def cadastroColab(telaPrincipal,cadastroColab):
        telaPrincipal.stackedWidget.setCurrentWidget(cadastroColab)
        
    def cadastroUser(telaPrincipal, CadastroUser):
        telaPrincipal.stackedWidget.setCurrentWidget(CadastroUser)

    def config(telaPrincipal, Config):
        telaPrincipal.stackedWidget.setCurrentWidget(Config)

class Logon():
    
    def inicializar_login(login):
        login.lineEdit.setText("")
        login.lineEdit_2.setText("")        

    def login_Padrao(Nome, Matricula, Função, telaPrincipal, telaPrincipal_widget, login_widget):
        telaPrincipal.label_4.setText(Nome)
        telaPrincipal.label_5.setText(Matricula)
        telaPrincipal.label_6.setText(Função)
        telaPrincipal.pushButton_4.setVisible(False)
        telaPrincipal_widget.show()
        login_widget.hide()

    def login_Adm (telaPrincipal, telaPrincipal_widget, login_widget):
            telaPrincipal.label_4.setText("ADM")
            telaPrincipal.label_5.setText("ADM")
            telaPrincipal.label_6.setText("ADM")
            telaPrincipal.pushButton_4.setVisible(True)
            telaPrincipal_widget.show()
            login_widget.hide()

            
 





        
    
