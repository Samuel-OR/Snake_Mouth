from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem

from tela_login import Ui_Tela_Login 
from tela_cadastrar import Ui_Tela_Cadastrar
from tela_professor import Ui_Tela_Professor
from tela_team import Ui_Tela_Team

from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot


import BancoDeDados as BD


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastrar = Ui_Tela_Cadastrar()
        self.tela_cadastrar.setupUi(self.stack1)

        self.tela_professor = Ui_Tela_Professor()
        self.tela_professor.setupUi(self.stack2)

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

        self.tela_professor.pushButton_7.clicked.connect(self.voltarLogin)

        self.tela_team.pushButton_7.clicked.connect(self.voltarLogin)
        '''self.tela_principal.ver_acervo.clicked.connect(self.openAcervoLivro)
        self.tela_principal.sair.clicked.connect(self.voltarInicio)

        self.tela_cadastro_livro.botao_salvar_livro.clicked.connect(self.cadastrarLivro)
        self.tela_cadastro_livro.buttonVoltar.clicked.connect(self.voltarPrincipal)

        self.tela_acervo.sair.clicked.connect(self.entrar)'''

    def openTelaCadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def entrar(self):

        user = self.tela_login.lineEdit.text()
        password = self.tela_login.lineEdit_2.text()
        cad = BD.login(user, password)
        if(cad[2] == 2):
            BD.codTEACHE = user
            self.QtStack.setCurrentIndex(2) #tela de login do professor
        elif cad[2] == 1:
            BD.codTeam = user
            self.QtStack.setCurrentIndex(3) #tela de login do aluno
        else:
            QMessageBox.about(self, "ATENÇÃO", "Usúario ou Senha inválidos.") 
            #self.show()
    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)

    '''def criarConta(self):
        self.QtStack.setCurrentIndex(0)

    def openCadastrarLivro(self):
        self.QtStack.setCurrentIndex(3)

    def openAcervoLivro(self):
        self.QtStack.setCurrentIndex(4)

    def voltarPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def cadastrarLivro(self):
        self.QtStack.setCurrentIndex(2) '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())