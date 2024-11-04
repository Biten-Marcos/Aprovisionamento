#importando formularios=====================================================================
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog

import sys
app=QtWidgets.QApplication([])

#===========================================================================================


class Logon():
    
    def inicializar_login(login):
        login.lineEdit.setText("")
        login.lineEdit_2.setText("")
  


    
    def login_Padrao(telaPrincipal_widget, login):
        telaPrincipal_widget.show()
        telaPrincipal_widget.pushButton_4.setVisible(False)
        




    def adm1 (telaPrincipal, telaPrincipal_widget, login, login_widget):
        adm = "adm"
        admsen = "adm"
        
        user = login.lineEdit.text()
        senha = login.lineEdit_2.text()
        if user == adm and senha == admsen:
            
            telaPrincipal.label_4.setText("ADM")
            telaPrincipal.label_5.setText("ADM")
            telaPrincipal.label_6.setText("ADM")
          
            telaPrincipal_widget.show()
            login_widget.hide()
        else:
            login_widget.hide()
            Logon.login_Padrao(telaPrincipal_widget, login)

            
 





class mainw():
    def sair (telaPrincipal_widget,login):
        login.show()
        Logon.inicializar_login(login)
        telaPrincipal_widget.hide()
    
