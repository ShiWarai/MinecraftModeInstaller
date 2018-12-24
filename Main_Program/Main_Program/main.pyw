# -*- coding: utf-8 -*-

import sys,os,shutil,time,zipfile, connection,subprocess,threading  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
import gui as design
import gui1 as design1


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def addText(self,text):
        self.textEdit.setText(QtCore.QCoreApplication.translate("MainWindow",str(self.textEdit.toPlainText())+text+"\n"))
    def __init__(self,file):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.file=file; self.path=None; self.clicked_=False 
        if self.last(2)==1 and self.path!=None:
            self.addText("Последняя папка:\n"+self.path)
        self.label.hide()
        self.pushButton.clicked.connect(self.copy)
        self.pushButton_2.clicked.connect(self.select_folder)
        self.pushButton_3.clicked.connect(self.about)
        self.pushButton_4.clicked.connect(self.start_update)
    def installer(self,way,name):
        new=zipfile.ZipFile(name,'r')
        new.extractall(way)
        new.close();
        os.remove(name)
        old=os.path.basename(sys.argv[0])
        file=open(way+'update.bat','w')
        file.write('ren '+way+'updated.exe '+old+'\nerase /Q '+way+'update.bat'); file.close();
    def start_update(self):
        self.label.show()
        new=connection.UpdateFromDropbox('bhMu3WRecMAAAAAAAAAAKcV5rJjH2MsowFAXFGyKQ7BhsvW24nWQP4zwy85lAoqa','app',self.installer)
        way=new.download(); 
        try:
            os.remove(way+'old.exe')
        except:
            pass
        QtWidgets.QMessageBox.about(self,'Обновление','Требуется перезагрузка!')
        os.rename(sys.argv[0],way+'old.exe')
        subprocess.Popen([way+'update.bat'])
        self.close()
    def copy(self):
        if self.clicked_==True:
            path=self.path
        else:
            path=os.environ["APPDATA"]+"\.minecraft"
        if os.path.exists(path)==True:
            self.addText("> Папка Minecraft найдена")
        else:
            QtWidgets.QMessageBox.about(self,"Ошибка!","Minecraft не найден!")
            self.close()
        if os.path.exists(path+"\mods")==True:
            shutil.copy(self.file,path+"\mods")
            self.addText("> Модификация установлена")
            QtWidgets.QMessageBox.about(self,"Готово","Модификация установлена")
            self.path=path
            self.textEdit.hide()
            self.textEdit.show()
            self.last(1)
            time.sleep(1)
            self.close()
        else:
            QtWidgets.QMessageBox.about(self,"Ошибка","Папка mods не найдена!")
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
    if len(sys.argv)>1:
        main(sys.argv[1])  # то запускаем функцию main()
    else:
        main(r'C:\test.jar')