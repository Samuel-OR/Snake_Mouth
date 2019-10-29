from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem

from tela_login import Ui_Tela_Login 
from tela_cadastrar import Ui_Tela_Cadastrar
from tela_Professor import Ui_Tela_Professor
from tela_team import Ui_Tela_Team

from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot

from sockets_cliente import *


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)
        self.client_socket = ClientSocket()

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastrar = Ui_Tela_Cadastrar()
        self.tela_cadastrar.setupUi(self.stack1)

        self.tela_Professor = Ui_Tela_Professor()
        self.tela_Professor.setupUi(self.stack2)

        self.tela_team = Ui_Tela_Team()
        self.tela_team.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tela_login.pushButton.clicked.connect(self.openTelaCadastrar)
        self.tela_login.pushButton_2.clicked.connect(self.entrar)
        self.tela_cadastrar.pushButton.clicked.connect(self.voltarLogin)
        #self.tela_cadastrar.pushButton_2.clicked.connect(self.voltarLogin)
        self.tela_Professor.pushButton_7.clicked.connect(self.voltarLogin)
        self.tela_Professor.pushButton_2.clicked.connect(self.cadastrarTime)
        self.tela_team.pushButton_7.clicked.connect(self.voltarLogin)

        self.tela_cadastrar.pushButton_2.clicked.connect(self.cadastrar)


    def openTelaCadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def entrar(self):
        string_login = "login,"

        user = self.tela_login.lineEdit.text()
        password = self.tela_login.lineEdit_2.text()
        string_login+=user+","+password
        #self.client_socket.enviar_dados(string_login)
        self.QtStack.setCurrentIndex(2)



    def cadastrar(self):
        string_cadastro = "cadastro,"

        email = self.tela_cadastrar.lineEdit.text()
        password = self.tela_cadastrar.lineEdit_2.text()
        name = self.tela_cadastrar.lineEdit_3.text()

        string_cadastro+=name+","+email+","+password

        print(string_cadastro)
        if self.client_socket.enviar_dados(string_cadastro):
            QMessageBox.about(None, "ATENÇÃO", "Cadastro Efetuado.") 
            self.voltarLogin()
        else:
            QMessageBox.about(None, "ATENÇÃO", "Cadastro NÃO Efetuado.") 

    def cadastrarTime(self):
        string_cadastro_time = "cadastroTime,"

        nameTeam = self.tela_Professor.lineEdit_2.text()
        C1 = self.tela_Professor.lineEdit_9.text()
        C2 = self.tela_Professor.lineEdit.text()
        C3 = self.tela_Professor.lineEdit_10.text()
        C4 = self.tela_Professor.lineEdit_8.text()

        string_cadastro_time+=nameTeam+","+C1+","+C2+","+C3+","+C4
        print(string_cadastro_time)
        

        if self.client_socket.enviar_dados(string_cadastro_time):
            QMessageBox.about(None, "ATENÇÃO", "Cadastro Efetuado.") 
            self.voltarLogin()
        else:
            QMessageBox.about(None, "ATENÇÃO", "Cadastro NÃO Efetuado.") 
        
    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())