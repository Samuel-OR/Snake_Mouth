# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Professor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 20, 531, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 40, 411, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout_2.addWidget(self.lineEdit_1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 81, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(400, 240, 89, 25))
        self.pushButton.setStyleSheet("background-color: #c4c245;\n"
"border-radius: 7px;\n"
"padding: 4px;\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 280, 165, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 111, 17))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(180, 320, 91, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 280, 91, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(30, 50, 71, 17))
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 451, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 280, 151, 31))
        self.pushButton_2.setStyleSheet("background-color: #4ebf6d;\n"
"border-radius: 7px;\n"
"padding: 4px;\n"
"color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 66, 101, 37))
        self.label_11.setObjectName("label_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 361, 29))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 471, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_6.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_6.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_5.addWidget(self.lineEdit_9)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_5.addWidget(self.lineEdit_10)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_5.addWidget(self.lineEdit_8)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 220, 450, 70))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(450, 70))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(40, 160, 161, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(40, 29, 222, 20))
        self.label_15.setObjectName("label_15")
        self.checkBox = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox.setGeometry(QtCore.QRect(210, 160, 86, 22))
        self.checkBox.setObjectName("checkBox")
        self.spinBox = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox.setGeometry(QtCore.QRect(350, 130, 91, 27))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(500)
        self.spinBox.setMaximum(9999)
        self.spinBox.setSingleStep(1)
        self.spinBox.setProperty("value", 500)
        self.spinBox.setObjectName("spinBox")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(40, 190, 161, 17))
        self.label_16.setObjectName("label_16")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 50, 351, 29))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(410, 30, 101, 20))
        self.label_17.setObjectName("label_17")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 320, 141, 31))
        self.pushButton_4.setStyleSheet("background-color: #4ebf6d;\n"
"border-radius: 7px;\n"
"padding: 4px;\n"
"color: white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(420, 50, 71, 31))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(40, 130, 301, 20))
        self.label_19.setObjectName("label_19")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 90, 291, 29))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(40, 92, 61, 20))
        self.label_20.setObjectName("label_20")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 90, 87, 29))
        self.pushButton_5.setStyleSheet("background-color: #a8a894;\n"
"border-radius: 7px;\n"
"padding: 4px;\n"
"color: white;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(90, 70, 381, 29))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(200, 40, 191, 37))
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 280, 121, 31))
        self.pushButton_3.setStyleSheet("background-color: #c4c245;\n"
"border-radius: 7px;\n"
"padding: 4px;\n"
"color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 120, 471, 138))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_7.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_7.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_7.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_7.addWidget(self.label_27)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_8.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_8.addWidget(self.lineEdit_13)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_8.addWidget(self.lineEdit_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_8.addWidget(self.lineEdit_15)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(self.tab_5)
        self.line.setGeometry(QtCore.QRect(-3, 100, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 280, 121, 31))
        self.pushButton_6.setStyleSheet("background-color: #c4c245;\n"
"border-radius: 7px;\n"
"padding: 4px;\n"
"color: white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIAPE"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "Senha"))
        self.pushButton.setText(_translate("MainWindow", "Atualizar"))
        self.label_6.setText(_translate("MainWindow", "Exercicíos Cadastrados: "))
        self.label_7.setText(_translate("MainWindow", "Times Cadastrados: "))
        self.label_4.setText(_translate("MainWindow", "Dados Pessoais"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Perfil"))
        self.label_8.setText(_translate("MainWindow", "Progresso"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pontuação"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Submissões Corretas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Progresso dos Times"))
        self.pushButton_2.setText(_translate("MainWindow", "Cadastrar Time"))
        self.label_11.setText(_translate("MainWindow", "Nome do Time"))
        self.label_12.setText(_translate("MainWindow", "Componente 1"))
        self.label_21.setText(_translate("MainWindow", "Componente 2"))
        self.label_22.setText(_translate("MainWindow", "Componente 3"))
        self.label_23.setText(_translate("MainWindow", "Componente 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cadastrar Time"))
        self.label_14.setText(_translate("MainWindow", "Visibilidade da questão:"))
        self.label_15.setText(_translate("MainWindow", "Nome da questão"))
        self.checkBox.setText(_translate("MainWindow", "Visible"))
        self.label_16.setText(_translate("MainWindow", "Descrição"))
        self.label_17.setText(_translate("MainWindow", "ID da questão"))
        self.pushButton_4.setText(_translate("MainWindow", "Cadastrar Questão"))
        self.label_18.setText(_translate("MainWindow", "ID"))
        self.label_19.setText(_translate("MainWindow", "Time limite para execução em millisegundos:"))
        self.label_20.setText(_translate("MainWindow", "Arquivo"))
        self.pushButton_5.setText(_translate("MainWindow", "Importar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Cadastrar Questão"))
        self.label_13.setText(_translate("MainWindow", "Digite o nome da equipe"))
        self.pushButton_3.setText(_translate("MainWindow", "Pesquisar"))
        self.label_24.setText(_translate("MainWindow", "Componente 1"))
        self.label_25.setText(_translate("MainWindow", "Componente 2"))
        self.label_26.setText(_translate("MainWindow", "Componente 3"))
        self.label_27.setText(_translate("MainWindow", "Componente 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Alterar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Editar Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

