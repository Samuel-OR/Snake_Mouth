from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem,QFileDialog
from tela_login import Ui_Tela_Login 
from tela_cadastrar import Ui_Tela_Cadastrar
from tela_Professor import Ui_Tela_Professor
from tela_team import Ui_Tela_Team

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

from sockets_cliente import *
from userlogado import *

import PyQt5, sys, os

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)
        self.client_socket = ClientSocket()
        self.user_logado = UserLogado()
        self.time_buscado = TimeBuscado
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
    
        self.tela_Professor.pushButton.clicked.connect(self.editarProfessor)
        self.tela_Professor.pushButton_2.clicked.connect(self.cadastrarTime)
        self.tela_Professor.pushButton_3.clicked.connect(self.buscar_time)
        self.tela_Professor.pushButton_4.clicked.connect(self.cadastrarExer)
        self.tela_Professor.pushButton_5.clicked.connect(self.selectFile_entrada)
        self.tela_Professor.pushButton_6.clicked.connect(self.editar_time)
        self.tela_Professor.pushButton_7.clicked.connect(self.voltarLogin)
        self.tela_Professor.pushButton_9.clicked.connect(self.selectFile_saida)


        self.tela_team.pushButton_7.clicked.connect(self.voltarLogin)
        
        self.tela_cadastrar.pushButton.clicked.connect(self.voltarLogin)
        self.tela_cadastrar.pushButton_2.clicked.connect(self.cadastrarProfessor)


    def selectFile_entrada(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.file_size = str(os.path.getsize(filename[0]))
        name = self.path.split("/")
        name = name[len(name)-1]
        self.tela_Professor.lineEdit_7.setText(name)

    def selectFile_saida(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.file_size = str(os.path.getsize(filename[0]))
        name = self.path.split("/")
        name = name[len(name)-1]
        self.tela_Professor.lineEdit_17.setText(name)

    def openTelaCadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def entrar(self):
        string_login = "login,"

        user = self.tela_login.lineEdit.text()
        password = self.tela_login.lineEdit_2.text()
        
        string_login+=user+","+password
        user_logado = self.client_socket.enviar_dados(string_login)

        if user_logado:
            
            print(user_logado)
            QMessageBox.about(None, "LOGIN", "Login efetuado.")  
            

            self.user_logado.id = user_logado[1]
            self.user_logado.siape = user_logado[2]
            self.user_logado.nome = user_logado[3]
            self.user_logado.email = user_logado[4]
            self.user_logado.senha = user_logado[5]
            self.user_logado.times = int(user_logado[6])
            self.user_logado.exercicios = int(user_logado[7])

            self.tela_Professor.lineEdit_1.setText(user_logado[2])
            self.tela_Professor.lineEdit_3.setText(user_logado[3])
            self.tela_Professor.lineEdit_4.setText(user_logado[4])
            self.tela_Professor.lineEdit_5.setText(user_logado[5])
            self.tela_Professor.textBrowser.setText(user_logado[6])
            self.tela_Professor.textBrowser_2.setText(user_logado[7])

            self.QtStack.setCurrentIndex(2)



        else:
            QMessageBox.about(None, "LOGIN", "Login invalido.")  

        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
    
    def buscar_time(self):
        time = self.tela_Professor.lineEdit_11.text()
        string = "buscaTime,"
        string+=time
        achado = self.client_socket.enviar_dados(string)
        if achado:
            self.tela_Professor.lineEdit_12.setText(achado[6])
            self.tela_Professor.lineEdit_13.setText(achado[7])
            self.tela_Professor.lineEdit_14.setText(achado[8])
            self.tela_Professor.lineEdit_15.setText(achado[9])

            self.time_buscado.id = achado[1]
            print(self.time_buscado.id)
            self.time_buscado.nome = achado[5]
            self.time_buscado.c1 = achado[6]
            self.time_buscado.c2 = achado[7]
            self.time_buscado.c3 = achado[8]
            self.time_buscado.c4 = achado[9]

    def editar_time(self):
        string_editar_time = "editarTime,"
    
        nameTeam = self.tela_Professor.lineEdit_11.text()
        C1 = self.tela_Professor.lineEdit_12.text()
        C2 = self.tela_Professor.lineEdit_13.text()
        C3 = self.tela_Professor.lineEdit_14.text()
        C4 = self.tela_Professor.lineEdit_15.text()

        string_editar_time+=nameTeam+","+C1+","+C2+","+C3+","+C4+","+self.time_buscado.id
        print(string_editar_time)
        

        if self.client_socket.enviar_dados(string_editar_time):
            QMessageBox.about(None, "ATENÇÃO", "Edição Efetuada.") 
        else:
            QMessageBox.about(None, "ATENÇÃO", "Edição NÃO Efetuada.")         

        self.tela_Professor.lineEdit_11.setText("")
        self.tela_Professor.lineEdit_12.setText("")
        self.tela_Professor.lineEdit_13.setText("")
        self.tela_Professor.lineEdit_14.setText("")
        self.tela_Professor.lineEdit_15.setText("")

    def cadastrarProfessor(self):
        string_cadastro = "cadastro,"

        email = self.tela_cadastrar.lineEdit.text()
        password = self.tela_cadastrar.lineEdit_2.text()
        name = self.tela_cadastrar.lineEdit_3.text()
        siape = self.tela_cadastrar.lineEdit_5.text()


        string_cadastro+=name+","+email+","+password+","+siape

        print(string_cadastro)
        if self.client_socket.enviar_dados(string_cadastro):
            QMessageBox.about(None, "ATENÇÃO", "Cadastro Efetuado.") 
            self.voltarLogin()
        else:
            QMessageBox.about(None, "ATENÇÃO", "Cadastro NÃO Efetuado.") 

        self.tela_cadastrar.lineEdit.setText("")
        self.tela_cadastrar.lineEdit_2.setText("")
        self.tela_cadastrar.lineEdit_3.setText("")
        self.tela_cadastrar.lineEdit_5.setText("")

    def cadastrarTime(self):
        string_cadastro_time = "cadastroTime,"

        nameTeam = self.tela_Professor.lineEdit_2.text()
        C1 = self.tela_Professor.lineEdit_9.text()
        C2 = self.tela_Professor.lineEdit.text()
        C3 = self.tela_Professor.lineEdit_10.text()
        C4 = self.tela_Professor.lineEdit_8.text()

        string_cadastro_time+=nameTeam+","+C1+","+C2+","+C3+","+C4+","+self.user_logado.id
        print(string_cadastro_time)
        

        if self.client_socket.enviar_dados(string_cadastro_time):
            QMessageBox.about(None, "ATENÇÃO", "Cadastro Efetuado.") 
            #self.textBrowser.setText(str(BD.BDteacher[code].teamCadastrados()))
            self.user_logado.times+=1
            self.tela_Professor.textBrowser.setText(str(self.user_logado.times))
        else:
            QMessageBox.about(None, "ATENÇÃO", "Cadastro NÃO Efetuado.")

        self.tela_Professor.lineEdit_2.setText("")
        self.tela_Professor.lineEdit_9.setText("")
        self.tela_Professor.lineEdit.setText("")
        self.tela_Professor.lineEdit_10.setText("")
        self.tela_Professor.lineEdit_8.setText("")
        
    def cadastrarExer(self):
        string_cadastro_exer = "cadastrarExer,"

        nameExer = self.tela_Professor.lineEdit_6.text()
        entrada = self.tela_Professor.lineEdit_7.text()
        saida = self.tela_Professor.lineEdit_17.text()
        describe = self.tela_Professor.plainTextEdit.toPlainText()
        time = self.tela_Professor.spinBox.text()

        string_cadastro_exer+= nameExer+","+entrada+","+saida+","+describe+","+time+","+str(self.user_logado.id)
        print("String:",string_cadastro_exer)
        
        if self.client_socket.enviar_dados(string_cadastro_exer):
            QMessageBox.about(None, "Exercício", "Cadastro Efetuado.") 
            #self.textBrowser.setText(str(BD.BDteacher[code].teamCadastrados()))
            self.user_logado.exercicios+=1
            self.tela_Professor.label_18.setText(str(self.user_logado.exercicios))
        else:
            QMessageBox.about(None, "Exercício", "Cadastro NÃO Efetuado.") 

        self.tela_Professor.lineEdit_6.setText("")
        self.tela_Professor.lineEdit_7.setText("")
        self.tela_Professor.lineEdit_17.setText("")
        self.tela_Professor.plainTextEdit.setPlainText("")

    def editarProfessor(self):
        string_editar_prof = "editarProfessor,"
    
        siape = self.tela_Professor.lineEdit_1.text()
        nome = self.tela_Professor.lineEdit_3.text()
        email = self.tela_Professor.lineEdit_4.text()
        senha = self.tela_Professor.lineEdit_5.text()

        string_editar_prof+=siape+","+nome+","+email+","+senha+","+str(self.user_logado.id)
        print(string_editar_prof)
        
        if self.client_socket.enviar_dados(string_editar_prof):
            QMessageBox.about(None, "Professor", "Atualização de dados efetuada.") 
        else:
            QMessageBox.about(None, "Professor", "Erro ao atualizar seus dados.")      


    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())