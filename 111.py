#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
pyqt的接触
'''
import sys
import time
import os
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('1.打开夜神模拟器', self)
        btn.resize(150, 50)
        btn.move(10, 10)
        btn.clicked.connect(sta_simulator)

        btn = QPushButton('2.打开外网游戏', self)
        btn.resize(150, 50)
        btn.move(10, 70)
        btn.clicked.connect(sta_simulator)

        self.setGeometry(300, 250, 300, 300)
        self.setWindowIcon(QIcon(r'C:\Users\van\Desktop\自用脚本\cc脚本\1'))
        self.setWindowTitle('终极脚本集合')
        self.show()

    def on_click(self):
        print("PyQt5 button click")

def sta_simulator():
    name_simulator = r"E:\van\simulator\nox_simulator\Nox\bin\Nox.exe"
    os.startfile(name_simulator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exm = Example()
    sys.exit(app.exec_())
