# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(653, 252)
        MainWindow.setMaximumSize(QtCore.QSize(855, 480))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 140, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(93, 255, 120);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 200, 141, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 89, 92);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setEnabled(False)
        self.webEngineView.setGeometry(QtCore.QRect(-420, -90, 721, 411))
        self.webEngineView.setUrl(QtCore.QUrl("qrc:/data/trangles.jpg"))
        self.webEngineView.setObjectName("webEngineView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 220, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 20, 321, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.webEngineView.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.textBrowser.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minecraft ModInstaller"))
        self.pushButton.setText(_translate("MainWindow", "Запуск установщика"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход из установщика"))
        self.pushButton_3.setText(_translate("MainWindow", "О разработчиках"))

from PyQt5 import QtWebEngineWidgets
import resurs_rc
