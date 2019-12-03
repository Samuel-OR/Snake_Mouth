from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem,QFileDialog
from PyQt5.QtCore import *

from tela_login import Ui_Tela_Login 
from tela_cadastrar import Ui_Tela_Cadastrar
from tela_Professor import Ui_Tela_Professor
from tela_team import Ui_Tela_Team

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

from sockets_cliente import *
from userlogado import *

from random import randint

import PyQt5, sys, os
import os
import time

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)
        self.client_socket = ClientSocket()
        self.user_logado = UserLogado()
        self.time_buscado = TimeBuscado()
        self.exerciciosAtivos = Exercicio()

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
        self.tela_Professor.pushButton_10.clicked.connect(self.listarTimes)


        self.tela_team.pushButton.clicked.connect(self.submeter)
        self.tela_team.pushButton_2.clicked.connect(self.atualizarHistorico)
        self.tela_team.pushButton_3.clicked.connect(self.atualizarClassi)
        self.tela_team.pushButton_5.clicked.connect(self.selectFile_entradaTIME)
        self.tela_team.pushButton_7.clicked.connect(self.voltarLogin)
        
        self.tela_cadastrar.pushButton.clicked.connect(self.voltarLogin)
        self.tela_cadastrar.pushButton_2.clicked.connect(self.cadastrarProfessor)


    def selectFile_entrada(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.file_size = str(os.path.getsize(filename[0]))
        name = self.path.split("/")
        name = name[len(name)-1]
        #self.tela_Professor.lineEdit_7.setText(name)
        self.tela_Professor.lineEdit_7.setText(filename[0])

    def selectFile_saida(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.file_size = str(os.path.getsize(filename[0]))
        name = self.path.split("/")
        name = name[len(name)-1]
        #self.tela_Professor.lineEdit_17.setText(name)
        self.tela_Professor.lineEdit_17.setText(filename[0])

    def selectFile_entradaTIME(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.file_size = str(os.path.getsize(filename[0]))
        name = self.path.split("/")
        name = name[len(name)-1]
        #self.tela_team.label_6.setText(name)
        self.tela_team.label_6.setText(filename[0])

    def openTelaCadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def entrar(self):

        user = self.tela_login.lineEdit.text()
        password = self.tela_login.lineEdit_2.text()
        
        if( not self.tela_login.radioButton.isChecked() and not self.tela_login.radioButton_2.isChecked()):
        
            QMessageBox.about(None, "LOGIN", "Selecione a opção de login (Time ou professor).   ")  

        elif( self.tela_login.radioButton_2.isChecked() ):

            print("PROFESSOR")
            string_login = "login,"
            string_login+=user+","+password
            user_logado = self.client_socket.enviar_dados(string_login)
            if user_logado:
                
                print("User Logado:",user_logado)
                QMessageBox.about(None, "LOGIN PROFESSOR", "Login efetuado com sucesso.")  

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
                QMessageBox.about(None, "LOGIN PROFESSOR", "Login professor invalido.")  

        else:
            print("TIME")
            string_login = "loginTime,"
            string_login+=user+","+password
            user_logado = self.client_socket.enviar_dados(string_login)
            
            if user_logado:   
                QMessageBox.about(None, "LOGIN TIME", "Login efetuado com sucesso.")  

                self.time_buscado.id = user_logado[1]
                self.time_buscado.prof = user_logado[2]
                self.time_buscado.nome = user_logado[4]
                self.time_buscado.c1 = user_logado[6]
                self.time_buscado.c2 = user_logado[7]
                self.time_buscado.c3 = user_logado[8]
                self.time_buscado.c4 = user_logado[9]

                self.pegarExercicios()

                self.tela_team.lineEdit_1.setText(user_logado[6])
                self.tela_team.lineEdit_1.setDisabled(True)
                self.tela_team.lineEdit_3.setText(user_logado[7])
                self.tela_team.lineEdit_3.setDisabled(True)
                self.tela_team.lineEdit_4.setText(user_logado[8])
                self.tela_team.lineEdit_4.setDisabled(True)
                self.tela_team.lineEdit_5.setText(user_logado[9])
                self.tela_team.lineEdit_5.setDisabled(True)
                
                for x,y in self.exerciciosAtivos.nome.items():
                    self.tela_team.comboBox.addItem(y)

                self.QtStack.setCurrentIndex(3)
            else:
                QMessageBox.about(None, "LOGIN TIME", "Login professor invalido.")  


        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
    
    def pegarExercicios(self):
       
        string_pegar_exercicios = "pegarExercicios,"
        string_pegar_exercicios += self.time_buscado.prof
        
        achado = self.client_socket.enviar_dados(string_pegar_exercicios)
        if achado:
            res = achado[1:]
            
            for x in res:
                x = x.split(',')
                self.exerciciosAtivos.Name_id[x[1]] = x[0]
                self.exerciciosAtivos.idQuestion[x[0]] = x[0]
                self.exerciciosAtivos.nome[x[0]] = x[1]
                self.exerciciosAtivos.entrada[x[0]] = x[2]
                self.exerciciosAtivos.saida[x[0]] = x[3]
                self.exerciciosAtivos.tempo[x[0]] = x[3]
            
            #QMessageBox.about(None, "ATENÇÃO", "Edição Efetuada.") 
        else:
            QMessageBox.about(None, "User Professor", "Erro pegar time.")       
        
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
        
        if self.client_socket.enviar_dados(string_editar_time):
            QMessageBox.about(None, "User Professor", "Edição do time efetuada com sucesso.") 
        else:
            QMessageBox.about(None, "User Professor", "Erro ao editar time.")         

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

        if self.client_socket.enviar_dados(string_cadastro):
            QMessageBox.about(None, "User Professor", "Professor cadastrado com sucesso.") 
            self.voltarLogin()
        else:
            QMessageBox.about(None, "User Professor", "Erro ao cadastrar o professor.") 

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
        senha = self.tela_Professor.lineEdit_200.text()

        string_cadastro_time+=nameTeam+","+C1+","+C2+","+C3+","+C4+","+self.user_logado.id+","+senha

        if self.client_socket.enviar_dados(string_cadastro_time):
            QMessageBox.about(None, "User Professor", "Time cadastro com sucesso.") 
            #self.textBrowser.setText(str(BD.BDteacher[code].teamCadastrados()))
            self.user_logado.times+=1
            self.tela_Professor.textBrowser.setText(str(self.user_logado.times))
        else:
            QMessageBox.about(None, "User Professor", "Erro ao cadastrar o time.")

        self.tela_Professor.lineEdit_2.setText("")
        self.tela_Professor.lineEdit_9.setText("")
        self.tela_Professor.lineEdit.setText("")
        self.tela_Professor.lineEdit_10.setText("")
        self.tela_Professor.lineEdit_8.setText("")
        self.tela_Professor.lineEdit_200.setText()
        
    def cadastrarExer(self):
        string_cadastro_exer = "cadastrarExer,"

        nameExer = self.tela_Professor.lineEdit_6.text()
        entrada = self.tela_Professor.lineEdit_7.text()
        saida = self.tela_Professor.lineEdit_17.text()
        describe = self.tela_Professor.plainTextEdit.toPlainText()
        time = self.tela_Professor.spinBox.text()

        string_cadastro_exer+= nameExer+","+entrada+","+saida+","+describe+","+time+","+str(self.user_logado.id)
        
        if self.client_socket.enviar_dados(string_cadastro_exer):
            QMessageBox.about(None, "User Professor", "Exercício cadastrado com sucesso.") 
            #self.textBrowser.setText(str(BD.BDteacher[code].teamCadastrados()))
            self.user_logado.exercicios+=1
            self.tela_Professor.label_18.setText(str(self.user_logado.exercicios))
        else:
            QMessageBox.about(None, "User Professor", "Erro ao cadastrar o exercício.") 

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
        
        if self.client_socket.enviar_dados(string_editar_prof):
            QMessageBox.about(None, "User Professor", "Atualização de dados efetuada.") 
        else:
            QMessageBox.about(None, "User Professor", "Erro ao atualizar seus dados.")      

    def listarTimes(self):
        string_listar_time = "listarTimes,"
        string_listar_time += self.user_logado.id
        
        achado = self.client_socket.enviar_dados(string_listar_time)
        if achado:
            res = achado[1:]
            self.tela_Professor.tableWidget.setRowCount(0)
            for x in res:
                x = x.split(',')
                rowPosition = self.tela_Professor.tableWidget.rowCount()
                self.tela_Professor.tableWidget.insertRow(rowPosition)
                self.tela_Professor.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(x[3]))
                self.tela_Professor.tableWidget.setItem(rowPosition , 1, QTableWidgetItem("250"))
                self.tela_Professor.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(str(x[4])))    
            
            #QMessageBox.about(None, "ATENÇÃO", "Edição Efetuada.") 
        else:
            QMessageBox.about(None, "User Professor", "Erro ao listar times.")         
    '''
    def submeter(self):
        
        nome = self.tela_team.comboBox.currentText()
        idQuestion = self.exerciciosAtivos.Name_id[nome]
        print(idQuestion)
        
        string_submeter = "submeter,"
        string_submeter += self.time_buscado.id+','
        string_submeter += self.exerciciosAtivos.entrada[idQuestion]+','
        string_submeter += self.exerciciosAtivos.saida[idQuestion]+','
        string_submeter += self.exerciciosAtivos.tempo[idQuestion]+','
        string_submeter += self.tela_team.label_6.text()
        print(string_submeter)
        
        achado = self.client_socket.enviar_dados(string_submeter)
        if achado:
            QMessageBox.about(None, "User TIME", "Submissão efetuada.") 
        else:
            QMessageBox.about(None, "User TIME", "Erro na Submissão.")
    '''
    def submeter(self):
        
        nome = self.tela_team.comboBox.currentText()
        idQuestion = self.exerciciosAtivos.Name_id[nome]
        
        idTime = self.time_buscado.id
        entrada = self.exerciciosAtivos.entrada[idQuestion]
        saida = self.exerciciosAtivos.saida[idQuestion]
        tempo = self.exerciciosAtivos.tempo[idQuestion]
        codigo = self.tela_team.label_6.text()
        
        solucao = str("ERRO NO ARQUIVO")
        try:
            tempoLimite = 1000
            
            timeINI = time.clock()
            os.system("nohuppython3 {} < {} > saidaAPRES.txt".format(codigo, entrada))
            timeFIM = time.clock()

            print("TEMPO mili: ", (timeFIM- timeINI)*100000)
        
            saidaAPRES = open('saidaAPRES.txt', 'r')
            saidaAPRES = (saidaAPRES.readlines())
            saidaAPRES = ' '.join(saidaAPRES)

            if("Traceback" in saidaAPRES or "NameError" in saidaAPRES):
                solucao = "ERRO DE SINTAXE"
                print("ERRO DE SINTAXE")
            else:

                if(((timeFIM- timeINI)*100000) > tempoLimite):
                    solucao = "ESTOURO DE TEMPO."
                    print("ESTOURO DE TEMPO.")
                else:

                    os.system("python3 {} < {} > saidaBRUTO.txt".format(codigo, entrada))
                    saidaPROF = open(saida, 'r')
                    saidaPROF = (saidaPROF.readlines())
                
                    saidaBRUTO=open('saidaBRUTO.txt', 'r')
                    saidaBRUTO = (saidaBRUTO.readlines())
                
                    if saidaPROF == saidaBRUTO:
                        solucao = "RESPOSTA CORRETA"
                        print("RESPOSTA CORRETA")
                    else:
                        #VERIFICAR ERRO DE APRESENTAÇÃO
                            #-i = remove case sentitive
                            #-w = Ignora espaços em branco
                            #-b = Ignore as mudanças na quantidade de espaço em branco.
                            #-B = Ignore as alterações cujas linhas estão todas em branco.  
                        os.system("diff -b -B -w -i saidaPROF.txt saidaBRUTO.txt > resulEXEC.txt")
                        resulEXEC = open('resulEXEC.txt', 'r')
                
                        if(len(resulEXEC.readlines())==0):
                            solucao = "ERRO DE APRESENTAÇÃO"
                            print("ERRO DE APRESENTAÇÃO")
                        else:
                            solucao = "RESPOSTA INCORRETA"
                            print("RESPOSTA INCORRETA")
                        os.system("rm resulEXEC.txt")
                    os.system("rm saidaBRUTO.txt")
                os.system("rm saidaAPRES.txt")
               
            QMessageBox.about(None, "User TIME", "Submissão efetuada.") 
        except:
            QMessageBox.about(None, "User TIME", "Erro na Submissão.")
        
        string_Historico = "cadastrarHist,"
        string_Historico+= self.exerciciosAtivos.nome[idQuestion]+','
        string_Historico+= '2019/09:30,'
        string_Historico+= solucao+','
        string_Historico+= str(idTime)

        self.client_socket.enviar_dados(string_Historico)
    

        self.atualizarHistorico()

    def atualizarHistorico(self):
        string_atualizar_hist = "atualizarHistorico,"
        string_atualizar_hist += self.time_buscado.id
        achado = self.client_socket.enviar_dados(string_atualizar_hist)
        
        if achado:
            res = achado[1:]
            self.tela_team.tableWidget_3.setRowCount(0)
            for x in res:
                x = x.split(',')
                rowPosition = self.tela_team.tableWidget_3.rowCount()
                self.tela_team.tableWidget_3.insertRow(rowPosition)
                self.tela_team.tableWidget_3.setItem(rowPosition , 0, QTableWidgetItem(x[1]))
                self.tela_team.tableWidget_3.setItem(rowPosition , 1, QTableWidgetItem(x[2]))
                self.tela_team.tableWidget_3.setItem(rowPosition , 2, QTableWidgetItem(str(x[3])))    
            
            #QMessageBox.about(None, "ATENÇÃO", "Edição Efetuada.") 
        else:
            QMessageBox.about(None, "User TIME", "Erro ao atualizar o histórico.")

    def atualizarClassi(self):
        string_listar_time = "listarTimes,"
        string_listar_time += self.time_buscado.prof
        
        achado = self.client_socket.enviar_dados(string_listar_time)
        if achado:
            res = achado[1:]
            self.tela_team.tableWidget_2.setRowCount(0)
            for x in res:
                x = x.split(',')
                rowPosition = self.tela_team.tableWidget_2.rowCount()
                self.tela_team.tableWidget_2.insertRow(rowPosition)
                self.tela_team.tableWidget_2.setItem(rowPosition , 0, QTableWidgetItem(x[3]))
                self.tela_team.tableWidget_2.setItem(rowPosition , 1, QTableWidgetItem("10"))
                self.tela_team.tableWidget_2.setItem(rowPosition , 2, QTableWidgetItem(str(x[4])))    
            
            #QMessageBox.about(None, "ATENÇÃO", "Edição Efetuada.") 
        else:
            QMessageBox.about(None, "User Professor", "Erro ao listar times.")

    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())