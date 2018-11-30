# -*- coding: utf-8 -*-

import sys,os,shutil,time  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
import gui as design
import gui1 as design1

def translate(text):
    return QtCore.QCoreApplication.translate("MainWindow",text)

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self,file):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.file=file; self.path=None; self.clicked_=False 
        if self.last(2)==1 and self.path!=None:
            self.addText("Последняя папка:\n"+self.path)
        self.pushButton.clicked.connect(self.copy)
        self.pushButton_2.clicked.connect(self.select_folder)
        self.pushButton_3.clicked.connect(self.about)
    def addText(self,text):
        self.textBrowser.setText(str(self.textBrowser.toPlainText())+text)
    def copy(self):
        if self.clicked_==True:
            path=self.path
        else:
            path=os.environ["APPDATA"]+"\.minecraft"
        if os.path.exists(path)==True:
            self.addText("> Папка Minecraft найдена\n")
        else:
            QtWidgets.QMessageBox.about(self,"Ошибка!","Minecraft не найден!")
            self.close()
        if os.path.exists(path+"\mods")==True:
            shutil.copy(self.file,path+"\mods")
            self.addText("> Модификация установлена\n")
            self.path=path
            self.last(1)
            time.sleep(1)
            self.close()
        else:
            self.addText("> Папка mods не найдена!\n")
    def select_folder(self):
        self.path=""
        if os.environ["APPDATA"]+"\.minecraft"==True:
            self.path=QtWidgets.QFileDialog.getExistingDirectory(self,"Выберите папку сборки",os.environ["APPDATA"]+"\.minecraft")
        else:
            self.path=QtWidgets.QFileDialog.getExistingDirectory(self,"Выберите папку сборки",os.environ["USERPROFILE"])
        self.path=str(self.path)
        if self.path!="":
            self.clicked_=True
    def about(self):
        about=About(self)
        about.show()
    def last(self,in_out):
        if os.path.exists(os.environ["PROGRAMDATA"]+r"\MinecraftInstaller")==False:
            os.mkdir(os.environ["PROGRAMDATA"]+r"\MinecraftInstaller")
        if in_out==1:
            file=open(os.environ["PROGRAMDATA"]+r"\MinecraftInstaller\last.dat",'w')
            file.write(self.path)
            file.close()
        else:
            try:
                file=open(os.environ["PROGRAMDATA"]+r"\MinecraftInstaller\last.dat",'r')
                self.path=file.read()
                file.close()
                if self.path=="":
                    self.path=None
                return 1
            except:
                self.path=None
                return 0
class About(QtWidgets.QMainWindow, design1.Ui_MainWindow):
    def __init__(self,parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
def main(file):
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp(file)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main(r"C:\Users\Shi Warai\Downloads\123.jar")  # то запускаем функцию main()