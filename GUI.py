# -*- coding: utf-8 -*-
# Разработка GUI на PyGt4

# ПУСТОЕ ОКНО
"""
import sys
from PyQt4 import QtGui #QtGui основной модуль для работы с интерфейсом

app = QtGui.QApplication(sys.argv) #Создаём объект приложение. 

widget = QtGui.QWidget() #QWidget -главный класс для всех виджетов. Это окно
widget.resize(250, 150) #Размер окна
widget.setWindowTitle('simple') #Заголовок
widget.show() #Показываем

sys.exit(app.exec_()) #Основной цикл программы
"""

# ПУСТОЕ ОКНО С ИКОНКОЙ
# Используем ООП стиль.
"""

import sys
from PyQt4 import QtGui


class Icon(QtGui.QWidget): #Класс Icon. Родителем класса является QtGui.QWidget
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        #Следующие методы мы унаследовали от QtGui.QWidget
        self.setGeometry(300, 300, 250, 150) #Местоположение окна и его размеры
        self.setWindowTitle('Icon')          #Заголовок окна
        self.setWindowIcon(QtGui.QIcon('icons/web.png')) #Пусть к иконке


app = QtGui.QApplication(sys.argv) #Создаём объект приложение. 
icon = Icon() #Присваеваем переменной icon класс icon
icon.show()   #Вызываем метод показа
sys.exit(app.exec_()) #Запускаем приложение
"""

#ПРИЛОЖЕНИЕ С КОНТЕКСТНОЙ ПОДСКАЗКОЙ
"""
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Tooltip(QtGui.QWidget): #Класс Tooltip. Родителем класса является QtGui.QWidget
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150) #Аналогично классу иконки
        self.setWindowTitle('Tooltip')

        self.setToolTip('<b>QWidget</b>') #Сама подсказка
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10)) #Устанавливаем шрифт


app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
app.exec_()
"""

#ПРИЛОЖЕНИЕ С КНОПКОЙ "ЗАКРЫТЬ"
"""
import sys
from PyQt4 import QtGui, QtCore


class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')

        quit = QtGui.QPushButton('Close', self) #Создание объекта quit
        quit.setGeometry(10, 10, 60, 35)        #Устанавливаем его метоположение и размер

        self.connect(quit, QtCore.SIGNAL('clicked()'), #Система событий в pyQT использует слоты и сигналы
            QtGui.qApp, QtCore.SLOT('quit()'))         #При нажатии на кнопку посылается сигнал clicked
                                                       #Метод QtCore.QObject.connect() отвечает за связь между слотами и сигналами
                                                       #Здесь мы связываем синал clicked с слотом приложения (qApp) и его функцией quit


app = QtGui.QApplication(sys.argv)
qb = QuitButton()   #Объект "Кнопка выхода" из класса QuitButton
qb.show()           #Метод показа
sys.exit(app.exec_())
"""

# ВЫХОД ИЗ ПРИЛОЖЕНИЯ С ПОДТВЕРЖДЕНИЕМ
"""
import sys
from PyQt4 import QtGui


class MessageBox(QtGui.QWidget): #Создаём класс MessageBox все как раньше
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('message box')


    def closeEvent(self, event): #Создаём обработчик события  "Закрытия"
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No) #Вместо Yes и No можно прописывать различные кнопки.

        if reply == QtGui.QMessageBox.Yes: #Проверка ответа
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
"""

# ПАНЕЛЬ СОСТОЯНИЯ
"""
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('statusbar')

        self.statusBar().showMessage('Ready') #Для создания панели состояния вызываем метод statusBar() класса QApplication


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
"""

# ГЛАВНОЕ МЕНЮ
"""
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('menubar')

        #Создание действия EXIT
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self) #Объект exit
        exit.setShortcut('Ctrl+Q')  #Иконка. В данном случае надпись
        exit.setStatusTip('Exit application') #Подсказка
        #Конец создания
        
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()')) 
        
        # Меню Set ты добавил сам, но действие добавить не получилось
        set = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Set', self) #Объект Set
        set.setShortcut('Ctrl+S')  #Иконка. В данном случае надпись
        set.setStatusTip('Set application') #Подсказка



        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File') #Создаём пункты меню
        file.addAction(exit)            #Добавляем действие. exit. Его мы прописали в классе MainWindow
        set = menubar.addMenu('&Set')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
"""

#ПАНЕЛЬ ИНСТРУМЕНТОВ
"""
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('toolbar')
        
        #Создание действия EXIT
        self.exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        #Конец создания
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        # ^ Соеденяем синал и слот приложения

        self.toolbar = self.addToolBar('Exit') #Добавляем тулбар
        self.toolbar.addAction(self.exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
"""

