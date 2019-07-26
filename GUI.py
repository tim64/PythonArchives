# -*- coding: utf-8 -*-
# ���������� GUI �� PyGt4

# ������ ����
"""
import sys
from PyQt4 import QtGui #QtGui �������� ������ ��� ������ � �����������

app = QtGui.QApplication(sys.argv) #������ ������ ����������. 

widget = QtGui.QWidget() #QWidget -������� ����� ��� ���� ��������. ��� ����
widget.resize(250, 150) #������ ����
widget.setWindowTitle('simple') #���������
widget.show() #����������

sys.exit(app.exec_()) #�������� ���� ���������
"""

# ������ ���� � �������
# ���������� ��� �����.
"""

import sys
from PyQt4 import QtGui


class Icon(QtGui.QWidget): #����� Icon. ��������� ������ �������� QtGui.QWidget
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        #��������� ������ �� ������������ �� QtGui.QWidget
        self.setGeometry(300, 300, 250, 150) #�������������� ���� � ��� �������
        self.setWindowTitle('Icon')          #��������� ����
        self.setWindowIcon(QtGui.QIcon('icons/web.png')) #����� � ������


app = QtGui.QApplication(sys.argv) #������ ������ ����������. 
icon = Icon() #����������� ���������� icon ����� icon
icon.show()   #�������� ����� ������
sys.exit(app.exec_()) #��������� ����������
"""

#���������� � ����������� ����������
"""
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Tooltip(QtGui.QWidget): #����� Tooltip. ��������� ������ �������� QtGui.QWidget
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150) #���������� ������ ������
        self.setWindowTitle('Tooltip')

        self.setToolTip('<b>QWidget</b>') #���� ���������
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10)) #������������� �����


app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
app.exec_()
"""

#���������� � ������� "�������"
"""
import sys
from PyQt4 import QtGui, QtCore


class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')

        quit = QtGui.QPushButton('Close', self) #�������� ������� quit
        quit.setGeometry(10, 10, 60, 35)        #������������� ��� ������������� � ������

        self.connect(quit, QtCore.SIGNAL('clicked()'), #������� ������� � pyQT ���������� ����� � �������
            QtGui.qApp, QtCore.SLOT('quit()'))         #��� ������� �� ������ ���������� ������ clicked
                                                       #����� QtCore.QObject.connect() �������� �� ����� ����� ������� � ���������
                                                       #����� �� ��������� ����� clicked � ������ ���������� (qApp) � ��� �������� quit


app = QtGui.QApplication(sys.argv)
qb = QuitButton()   #������ "������ ������" �� ������ QuitButton
qb.show()           #����� ������
sys.exit(app.exec_())
"""

# ����� �� ���������� � ��������������
"""
import sys
from PyQt4 import QtGui


class MessageBox(QtGui.QWidget): #������ ����� MessageBox ��� ��� ������
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('message box')


    def closeEvent(self, event): #������ ���������� �������  "��������"
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No) #������ Yes � No ����� ����������� ��������� ������.

        if reply == QtGui.QMessageBox.Yes: #�������� ������
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
"""

# ������ ���������
"""
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('statusbar')

        self.statusBar().showMessage('Ready') #��� �������� ������ ��������� �������� ����� statusBar() ������ QApplication


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
"""

# ������� ����
"""
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('menubar')

        #�������� �������� EXIT
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self) #������ exit
        exit.setShortcut('Ctrl+Q')  #������. � ������ ������ �������
        exit.setStatusTip('Exit application') #���������
        #����� ��������
        
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()')) 
        
        # ���� Set �� ������� ���, �� �������� �������� �� ����������
        set = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Set', self) #������ Set
        set.setShortcut('Ctrl+S')  #������. � ������ ������ �������
        set.setStatusTip('Set application') #���������



        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File') #������ ������ ����
        file.addAction(exit)            #��������� ��������. exit. ��� �� ��������� � ������ MainWindow
        set = menubar.addMenu('&Set')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
"""

#������ ������������
"""
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('toolbar')
        
        #�������� �������� EXIT
        self.exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        #����� ��������
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        # ^ ��������� ����� � ���� ����������

        self.toolbar = self.addToolBar('Exit') #��������� ������
        self.toolbar.addAction(self.exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
"""

