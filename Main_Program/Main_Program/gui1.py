
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(390, 290)
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 271))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 351, 241))
        self.textBrowser.setMaximumSize(QtCore.QSize(450, 550))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Описание"))
        self.groupBox.setTitle(_translate("MainWindow", "Об авторах и программе"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:22pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400;\">Данный инстолятор живет и функционирует благодаря великолепной работе программиста Shi Warai. Второй же &quot;программист&quot;, Vegelos, задизайнил это великолепие и написал этот текст.  Данная программа предназначена для экономии вашего времени и безграничного модинга своего любимого Minecraft\'а.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400;\">Желаем побыстрее накопить на лицензию этой великой игры!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400;\">Кстати, данная версия обладает возможностью обновления!</span></p></body></html>"))

import resurs_rc
