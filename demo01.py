#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
脚本大集合
Author:van
'''
import sys, os
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt


class mywidget(QWidget):
    def __init__(self):
        super(mywidget, self).__init__()
        self.init()

    def init(self):
        btn = QPushButton("1.打开夜神模拟器", self)
        btn.resize(120, 20)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(250,250,250,50%);font-weight:bold")
        btn.clicked.connect(opensimulator)
        btn.clicked.connect(self.tips0)
        btn = QPushButton("2.弹出一个提示框", self)
        btn.resize(120, 20)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(250,250,250,50%);font-weight:bold")
        btn.clicked.connect(self.tips)
        btn.move(0, 21)
        btn = QPushButton("3.检测当前的网速", self)
        btn.resize(120, 20)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(250,250,250,50%);font-weight:bold")
        btn.move(0, 42)
        btn = QPushButton("4.打开公司的主页", self)
        btn.resize(120, 20)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(250,250,250,50%);font-weight:bold")
        btn.move(0, 63)
        btn.clicked.connect(openurl)
        btn = QPushButton("5. adb的自用教程", self)
        btn.resize(120, 20)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(250,250,250,50%);font-weight:bold")
        btn.move(0, 84)
        btn.clicked.connect(self.jump_widget1)

        btn = QPushButton("退出", self)
        btn.resize(40, 40)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(205,197,191,50%);font-weight:bold")
        btn.move(320, 0)
        btn.clicked.connect(QApplication.instance().quit)
        btn = QPushButton("任务", self)
        btn.setStyleSheet("color:rgba(0,191,250,100%) ;background-color:rgba(0,238,118,50%);font-weight:bold")
        btn.resize(40, 40)
        btn.move(360, 0)
        btn.clicked.connect(openrc)
        btn = QPushButton("0.0不知道会发生什么", self)
        btn.setStyleSheet("color:black ;background-color:rgba(0,238,118,50%);font-weight:bold")
        btn.resize(150, 40)
        btn.move(250, 234)
        self.setWindowTitle("( ゜- ゜)つロ")
        self.setWindowIcon(QIcon(r'C:\Users\xiewenhua\Desktop\自用脚本\脚本大集合\1.jpg'))
        self.resize(400, 274)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
        qp = QPalette()
        qp.setBrush(self.backgroundRole(), QBrush(QPixmap(r'C:\Users\xiewenhua\Desktop\自用脚本\脚本大集合\1.jpg')))
        self.setPalette(qp)

    def tips(self):
        button = QMessageBox()
        button.information(self, '提示信息', self.tr("你是真的皮"))

    def tips0(self):
        button = QMessageBox()
        button.information(self, '提示信息', self.tr("夜神模拟器已打开"))

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示框', '确认关闭？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def jump_widget1(self):
        self.zz = widget1()


# 打开
def opensimulator():
    name_simulator = r"E:\xwh\simulator\nox_simulator\Nox\bin\Nox.exe"
    os.startfile(name_simulator)


# 打开日程文档
def openrc():
    object = r"C:\Users\xiewenhua\Desktop\我的日程规划.docx"
    os.startfile(object)


# 打开网页
def openurl():
    webbrowser.open("https://pt.ztgame.com/")


def tips():
    qm = QMessageBox()
    qm.question('你是一直哈士奇', QMessageBox.Yes)
    qm.setWindowTitle("提示信息")
    qm.show()


# adb界面
class widget1(QWidget):
    def __init__(self):
        super(widget1, self).__init__()
        self.init()

    def init(self):
        btn0 = QPushButton(self)
        btn0.setText("adb devices")
        btn0.clicked.connect(self.jump_widget11)
        self.resize(500, 500)
        self.setWindowTitle("adb各种命令的分析")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

    def jump_widget11(self):
        self.cc = widget11()


class widget11(QWidget):
    def __init__(self):
        super(widget11, self).__init__()
        self.init()

    def init(self):
        label = QLabel(self)
        label.setText("adb devices")
        label0 = QLabel(self)
        label0.move(0, label.height())
        label0.setText("In response, return serial number and state ")
        label1 = QLabel(self)
        label1.move(0, 2 * label0.height())
        label1.setText("作为回应，返回序列号和状态")
        self.resize(500, 500)
        self.setWindowTitle("adb device命令的解析")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = mywidget()
    sys.exit(app.exec_())