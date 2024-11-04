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
  


    
    def login_Padrao(tela_principal, login):
        tela_principal.show()
        tela_principal.pushButton_4.setVisible(False)
        




    def adm1 (tela_Principal, login):
        adm = "adm"
        admsen = "adm"
        
        user = login.lineEdit.text()
        senha = login.lineEdit_2.text()
        if user == adm and senha == admsen:
            
            tela_Principal.label_4.setText("ADM")
            tela_Principal.label_5.setText("ADM")
            tela_Principal.label_6.setText("ADM")
          
            tela_Principal.show()
            login.hide()
        else:
            login.hide()
            Logon.login_Padrao(tela_Principal, login)

            
 





class mainw():
    def sair (tela_Principal,login):
        login.show()
        Logon.inicializar_login(login)
        tela_Principal.hide()
    
