from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
import sys
from MODULOS.funcoes import Logon, mainw
from INTERFACES.login import Ui_Login

from INTERFACES.telaPrincipal import Ui_MainWindow

from DB.query import sqlite_db

class cadastrar(QDialog):
    
    def add(telaPrincipal):
        db = sqlite_db("Users.db")
        name = telaPrincipal.lineEdit.text()
        usu = telaPrincipal.lineEdit_2.text()
        senha = telaPrincipal.lineEdit_3.text()

        if telaPrincipal.comboBox.currentText() == "Usuário":
            tip = 1
        else:
            tip = 0

        if name == "" or usu == "" or senha == "":
            QMessageBox.information(QMessageBox(),"opa pa", "Insira todos os dados!")
        else:
            db.inserir_apaga_atualiza("INSERT INTO USUARIOS (nome, usuário, senha, tipo) VALUES ('{}','{}','{}','{}')".format(name, usu, senha, tip))
            QMessageBox.information(QMessageBox(),"opa pa", "Dados gravados com sucesso!")

        #adm = 0
        #usu = 1


    def limpar(telaPrincipal):
        telaPrincipal.lineEdit.setText("")
        telaPrincipal.lineEdit_2.setText("")
        telaPrincipal.lineEdit_3.setText("")
        telaPrincipal.lineEdit_4.setText("")





