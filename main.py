# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '이차방정식_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from fractions import Fraction as frac
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import random
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 841)
        MainWindow.setSizeIncrement(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("로고.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0, angle:0, stop:0 rgba(0, 0, 0, 200), stop:0.492683 rgba(219, 235, 255, 255));")
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.x2 = QtWidgets.QLabel(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(240, 150, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x2.setFont(font)
        self.x2.setAlignment(QtCore.Qt.AlignCenter)
        self.x2.setIndent(2)
        self.x2.setObjectName("x2")
        self.x = QtWidgets.QLabel(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(360, 150, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x.setFont(font)
        self.x.setAlignment(QtCore.Qt.AlignCenter)
        self.x.setObjectName("x")
        self.frac_1 = QtWidgets.QFrame(self.centralwidget)
        self.frac_1.setGeometry(QtCore.QRect(180, 170, 61, 2))
        self.frac_1.setStyleSheet("background-color:\"black\"")
        self.frac_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.frac_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frac_1.setObjectName("frac_1")
        self.frac_2 = QtWidgets.QFrame(self.centralwidget)
        self.frac_2.setGeometry(QtCore.QRect(310, 170, 61, 2))
        self.frac_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frac_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frac_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frac_2.setObjectName("frac_2")
        self.frac_3 = QtWidgets.QFrame(self.centralwidget)
        self.frac_3.setGeometry(QtCore.QRect(430, 170, 61, 2))
        self.frac_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frac_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frac_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frac_3.setObjectName("frac_3")
        self.a_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.a_1.setGeometry(QtCore.QRect(180, 110, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.a_1.setFont(font)
        self.a_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a_1.setObjectName("a_1")
        self.a_1.setAlignment(QtCore.Qt.AlignCenter)              
        self.a_1.textChanged.connect(self.on_text_changed)
        self.b_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.b_1.setGeometry(QtCore.QRect(310, 110, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.b_1.setFont(font)
        self.b_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.b_1.setObjectName("b_1")
        self.b_1.setAlignment(QtCore.Qt.AlignCenter)              
        self.b_1.textChanged.connect(self.on_text_changed)
        self.c_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.c_1.setGeometry(QtCore.QRect(430, 110, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.c_1.setFont(font)
        self.c_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_1.setObjectName("c_1")
        self.c_1.setAlignment(QtCore.Qt.AlignCenter)              
        self.c_1.textChanged.connect(self.on_text_changed)
        self.b_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.b_2.setGeometry(QtCore.QRect(310, 180, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.b_2.setFont(font)
        self.b_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.b_2.setObjectName("b_2")
        self.b_2.setAlignment(QtCore.Qt.AlignCenter)              
        self.b_2.textChanged.connect(self.on_text_changed)
        self.exp = QtWidgets.QLabel(self.centralwidget)
        self.exp.setGeometry(QtCore.QRect(290, 510, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.exp.setFont(font)
        self.exp.setAlignment(QtCore.Qt.AlignCenter)
        self.exp.setObjectName("exp")
        self.c_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.c_2.setGeometry(QtCore.QRect(430, 180, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.c_2.setFont(font)
        self.c_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_2.setObjectName("c_2")
        self.c_2.setAlignment(QtCore.Qt.AlignCenter)              
        self.c_2.textChanged.connect(self.on_text_changed)
        self.gwalho = QtWidgets.QLabel(self.centralwidget)
        self.gwalho.setGeometry(QtCore.QRect(500, 510, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.gwalho.setFont(font)
        self.gwalho.setAlignment(QtCore.Qt.AlignCenter)
        self.gwalho.setObjectName("gwalho")
        self.a_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.a_2.setGeometry(QtCore.QRect(180, 180, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.a_2.setFont(font)
        self.a_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a_2.setObjectName("a_2")
        self.a_2.setAlignment(QtCore.Qt.AlignCenter)              
        self.a_2.textChanged.connect(self.on_text_changed)
        self.plus_1 = QtWidgets.QLabel(self.centralwidget)
        self.plus_1.setGeometry(QtCore.QRect(275, 160, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.plus_1.setFont(font)
        self.plus_1.setAlignment(QtCore.Qt.AlignCenter)
        self.plus_1.setObjectName("plus_1")
        self.plus_2 = QtWidgets.QLabel(self.centralwidget)
        self.plus_2.setGeometry(QtCore.QRect(390, 160, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.plus_2.setFont(font)
        self.plus_2.setAlignment(QtCore.Qt.AlignCenter)
        self.plus_2.setObjectName("plus_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(520, 550, 60, 2))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(600, 550, 60, 2))
        self.line_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.arrow = QtWidgets.QPushButton(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(450, 300, 151, 101))
        self.arrow.setAutoFillBackground(False)
        self.arrow.setStyleSheet("border:enable;")
        self.arrow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("화살표.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrow.setIcon(icon1)
        self.arrow.setIconSize(QtCore.QSize(150, 150))
        self.arrow.setObjectName("arrow")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 240, 371, 371))
        self.widget.setObjectName("widget")
        self.ilban = QtWidgets.QPushButton(self.centralwidget)
        self.ilban.setGeometry(QtCore.QRect(50, 660, 291, 101))
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.ilban.setFont(font)
        self.ilban.setStyleSheet("background-color: rgb(100, 200, 200);\n"
"color: rgb(255, 255, 0);\n"
"")
        self.ilban.setObjectName("ilban")
        self.ilban_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ilban_2.setGeometry(QtCore.QRect(390, 660, 291, 101))
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.ilban_2.setFont(font)
        self.ilban_2.setStyleSheet("background-color: rgb(100, 200, 200);\n"
"color: rgb(255, 255, 0);\n"
"")
        self.ilban_2.setObjectName("ilban_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(522, 500, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(522, 560, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(601, 560, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(600, 500, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        #self.widget.raise_()
        self.x2.raise_()
        self.x.raise_()
        self.frac_1.raise_()
        self.frac_2.raise_()
        self.frac_3.raise_()
        self.a_1.raise_()
        self.b_1.raise_()
        self.c_1.raise_()
        self.b_2.raise_()
        self.c_2.raise_()
        self.gwalho.raise_()
        self.exp.raise_()
        self.a_2.raise_()
        self.plus_1.raise_()
        self.plus_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.arrow.raise_()
        self.ilban.raise_()
        self.ilban_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        self.arrow.clicked.connect(self.pyojun_f)
        self.ilban.clicked.connect(self.dograph_f)
        self.ilban_2.clicked.connect(self.dojum_f)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.a_1, self.b_1)
        MainWindow.setTabOrder(self.b_1, self.c_1)
        MainWindow.setTabOrder(self.c_1, self.a_2)
        MainWindow.setTabOrder(self.b_2, self.c_2)
        self.vbox = QtWidgets.QVBoxLayout(self.widget)

    def dojum_f(self):

        self.window= QtWidgets.QMainWindow()
        self.ui= Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def pyojun_f(self):
        self.a1=int(self.a_1.text())
        self.a2=int(self.a_2.text())
        self.b1=int(self.b_1.text())
        self.b2=int(self.b_2.text())
        self.c1=int(self.c_1.text())
        self.c2=int(self.c_2.text())

        self.a=frac(self.a1/self.a2)
        self.b=frac(self.b1/self.b2)
        self.c=frac(self.c1/self.c2)
        self.poi_1=frac((self.b/(self.a*2)*-1))
        self.poi_2=frac(self.a*self.poi_1**2+self.poi_1*self.b+self.c)
        self.label_5.setText(str(self.poi_1.numerator))
        self.label_6.setText(str(self.poi_1.denominator))
        self.label_8.setText(str(self.poi_2.numerator))
        self.label_7.setText(str(self.poi_2.denominator))
    def on_text_changed(self, text):
        width = self.a_1.fontMetrics().width(text)
        self.a_1.setMinimumWidth(width)
        width = self.a_2.fontMetrics().width(text)
        self.a_2.setMinimumWidth(width)
        width = self.b_1.fontMetrics().width(text)
        self.b_1.setMinimumWidth(width)
        width = self.b_2.fontMetrics().width(text)
        self.b_2.setMinimumWidth(width)
        width = self.c_1.fontMetrics().width(text)
        self.c_1.setMinimumWidth(width)
        width = self.c_2.fontMetrics().width(text)
        self.c_2.setMinimumWidth(width)

    def dograph_f(self):
        
        self.widget.raise_()
        a=(int(self.a_1.text())/int(self.a_2.text()))
        b=(int(self.b_1.text())/int(self.b_2.text()))
        c=(int(self.c_1.text())/int(self.c_2.text()))

        self.vbox.takeAt(0)
        self.poi1=(b/(a*2)*-1)
        self.poi2=a*self.poi1**2+self.poi1*b+c

        dynamic_canvas = FigureCanvas(Figure(figsize=(4, 3),facecolor='#dbebff'))
        self.vbox.addWidget(dynamic_canvas)

        self.dynamic_ax = dynamic_canvas.figure.subplots()
        self.dynamic_ax.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
        #self.dynamic_ax.set_facecolor("#dbebff")
        self.dynamic_ax.clear()
        arr1=np.array([])
        arr2=np.array([])
        x=0+self.poi1
        p=1
        o=0
        r=600
        y=self.poi2
        self.dynamic_ax.text(x+1, y-15, "point({}, {})".format(x, y), fontsize=10)
        self.dynamic_ax.scatter(x, y, c='black')
        self.dynamic_ax.set_title('Secondary Function')
        for i in range(r):
            y=a*x**2+b*x+c+self.poi2
            arr1=np.append(arr1,np.array([x]))
            arr2=np.append(arr2,np.array([y]))
            x+=p
            if y>400:
                o+=1
                p=-1
            if o>3:
                break

        self.dynamic_ax.plot(arr1,arr2, color='deeppink')
        self.dynamic_ax.figure.canvas.draw()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "이차함수의 일반형"))
        self.x2.setText(_translate("MainWindow", "x²"))
        self.x.setText(_translate("MainWindow", "x"))
        self.a_1.setText(_translate("MainWindow", "a"))
        self.b_1.setText(_translate("MainWindow", "b"))
        self.c_1.setText(_translate("MainWindow", "c"))
        self.b_2.setText(_translate("MainWindow", "1"))
        self.c_2.setText(_translate("MainWindow", "1"))
        self.gwalho.setText(_translate("MainWindow", "(        ,        )"))
        self.exp.setText(_translate("MainWindow", "꼭짓점의 좌표:"))
        self.a_2.setText(_translate("MainWindow", "1"))
        self.plus_1.setText(_translate("MainWindow", "+"))
        self.plus_2.setText(_translate("MainWindow", "+"))
        self.ilban.setText(_translate("MainWindow", "그래프 그리기"))
        self.ilban_2.setText(_translate("MainWindow", "두 점의 좌표로 구하기"))
        self.label_5.setText(_translate("MainWindow", "x"))
        self.label_6.setText(_translate("MainWindow", "1"))
        self.label_7.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "y"))
        self.action.setText(_translate("MainWindow", "아아아"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+C"))








"""
aaaaaaaaaaaaaaaaaaaaaaaaaaa
"""





class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 846)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("로고.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0, angle:0, stop:0 rgba(0, 0, 0, 200), stop:0.492683 rgba(219, 235, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ilban = QtWidgets.QPushButton(self.centralwidget)
        self.ilban.setGeometry(QtCore.QRect(50, 660, 291, 101))
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.ilban.setFont(font)
        self.ilban.setStyleSheet("background-color: rgb(100, 200, 200);\n"
"color: rgb(255, 255, 0);\n"
"")
        self.ilban.setObjectName("ilban")
        self.twojum = QtWidgets.QPushButton(self.centralwidget)
        self.twojum.setGeometry(QtCore.QRect(390, 660, 291, 101))
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.twojum.setFont(font)
        self.twojum.setStyleSheet("background-color: rgb(100, 200, 200);\n"
"color: rgb(255, 255, 0);\n"
"")
        self.twojum.setObjectName("twojum")
        self.arrow = QtWidgets.QPushButton(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(400, 260, 151, 101))
        self.arrow.setAutoFillBackground(False)
        self.arrow.setStyleSheet("border:enable;")
        self.arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("화살표.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrow.setIcon(icon)
        self.arrow.setIconSize(QtCore.QSize(150, 150))
        self.arrow.setObjectName("arrow")
        self.exp_1 = QtWidgets.QLabel(self.centralwidget)
        self.exp_1.setGeometry(QtCore.QRect(80, 130, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.exp_1.setFont(font)
        self.exp_1.setObjectName("exp_1")
        self.gwalho_1 = QtWidgets.QLabel(self.centralwidget)
        self.gwalho_1.setGeometry(QtCore.QRect(260, 130, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gwalho_1.setFont(font)
        self.gwalho_1.setObjectName("gwalho_1")
        self.x1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.x1_2.setGeometry(QtCore.QRect(280, 181, 48, 50))
        self.x1_2.setAlignment(QtCore.Qt.AlignCenter)              
        self.x1_2.textChanged.connect(self.on_text_changed)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x1_2.setFont(font)
        self.x1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x1_2.setObjectName("x1_2")
        self.x1_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.x1_1.setGeometry(QtCore.QRect(280, 120, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x1_1.setFont(font)
        self.x1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x1_1.setObjectName("x1_1")
        self.x1_1.setAlignment(QtCore.Qt.AlignCenter)              
        self.x1_1.textChanged.connect(self.on_text_changed)
        self.y1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.y1_2.setGeometry(QtCore.QRect(360, 180, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.y1_2.setFont(font)
        self.y1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y1_2.setObjectName("y1_2")
        self.y1_2.setAlignment(QtCore.Qt.AlignCenter)              
        self.y1_2.textChanged.connect(self.on_text_changed)
        
        self.y1_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.y1_1.setGeometry(QtCore.QRect(360, 120, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.y1_1.setFont(font)
        self.y1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y1_1.setObjectName("y1_1")
        self.y1_1.setAlignment(QtCore.Qt.AlignCenter)              
        self.y1_1.textChanged.connect(self.on_text_changed)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(274, 175, 60, 2))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(354, 174, 60, 2))
        self.line_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frac_3 = QtWidgets.QFrame(self.centralwidget)
        self.frac_3.setGeometry(QtCore.QRect(635, 490, 61, 2))
        self.frac_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frac_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frac_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frac_3.setObjectName("frac_3")
        self.x = QtWidgets.QLabel(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(565, 470, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x.setFont(font)
        self.x.setAlignment(QtCore.Qt.AlignCenter)
        self.x.setObjectName("x")
        self.frac_1 = QtWidgets.QFrame(self.centralwidget)
        self.frac_1.setGeometry(QtCore.QRect(385, 490, 61, 2))
        self.frac_1.setStyleSheet("background-color:\"black\"")
        self.frac_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.frac_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frac_1.setObjectName("frac_1")
        self.x2 = QtWidgets.QLabel(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(445, 470, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x2.setFont(font)
        self.x2.setAlignment(QtCore.Qt.AlignCenter)
        self.x2.setIndent(2)
        self.x2.setObjectName("x2")
        self.plus_2 = QtWidgets.QLabel(self.centralwidget)
        self.plus_2.setGeometry(QtCore.QRect(595, 480, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.plus_2.setFont(font)
        self.plus_2.setAlignment(QtCore.Qt.AlignCenter)
        self.plus_2.setObjectName("plus_2")
        self.frac_2 = QtWidgets.QFrame(self.centralwidget)
        self.frac_2.setGeometry(QtCore.QRect(515, 490, 61, 2))
        self.frac_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frac_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frac_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frac_2.setObjectName("frac_2")
        self.plus_1 = QtWidgets.QLabel(self.centralwidget)
        self.plus_1.setGeometry(QtCore.QRect(480, 480, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.plus_1.setFont(font)
        self.plus_1.setAlignment(QtCore.Qt.AlignCenter)
        self.plus_1.setObjectName("plus_1")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 240, 371, 371))
        self.widget.setObjectName("widget")
        self.a_1 = QtWidgets.QLabel(self.centralwidget)
        self.a_1.setGeometry(QtCore.QRect(390, 440, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.a_1.setFont(font)
        self.a_1.setAlignment(QtCore.Qt.AlignCenter)
        self.a_1.setObjectName("a_1")
        self.a_2 = QtWidgets.QLabel(self.centralwidget)
        self.a_2.setGeometry(QtCore.QRect(390, 500, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.a_2.setFont(font)
        self.a_2.setAlignment(QtCore.Qt.AlignCenter)
        self.a_2.setObjectName("a_2")
        self.b_2 = QtWidgets.QLabel(self.centralwidget)
        self.b_2.setGeometry(QtCore.QRect(520, 500, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.b_2.setFont(font)
        self.b_2.setAlignment(QtCore.Qt.AlignCenter)
        self.b_2.setObjectName("b_2")
        self.b_1 = QtWidgets.QLabel(self.centralwidget)
        self.b_1.setGeometry(QtCore.QRect(520, 440, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.b_1.setFont(font)
        self.b_1.setAlignment(QtCore.Qt.AlignCenter)
        self.b_1.setObjectName("b_1")
        self.c_2 = QtWidgets.QLabel(self.centralwidget)
        self.c_2.setGeometry(QtCore.QRect(640, 500, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.c_2.setFont(font)
        self.c_2.setAlignment(QtCore.Qt.AlignCenter)
        self.c_2.setObjectName("c_2")
        self.c_1 = QtWidgets.QLabel(self.centralwidget)
        self.c_1.setGeometry(QtCore.QRect(640, 440, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.c_1.setFont(font)
        self.c_1.setAlignment(QtCore.Qt.AlignCenter)
        self.c_1.setObjectName("c_1")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(540, 173, 60, 2))
        self.line_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.y2_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.y2_2.setGeometry(QtCore.QRect(546, 179, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.y2_2.setFont(font)
        self.y2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y2_2.setObjectName("y2_2")
        self.y2_2.setAlignment(QtCore.Qt.AlignCenter)              
        self.y2_2.textChanged.connect(self.on_text_changed)
        
        self.y2_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.y2_1.setGeometry(QtCore.QRect(546, 119, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.y2_1.setAlignment(QtCore.Qt.AlignCenter)              
        self.y2_1.textChanged.connect(self.on_text_changed)
        self.y2_1.setFont(font)
        self.y2_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y2_1.setObjectName("y2_1")

        self.x1_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.x1_3.setGeometry(QtCore.QRect(466, 119, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x1_3.setFont(font)
        self.x1_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x1_3.setObjectName("x1_3")
        self.x1_3.setAlignment(QtCore.Qt.AlignCenter)              
        self.x1_3.textChanged.connect(self.on_text_changed)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(460, 174, 60, 2))
        self.line_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.x1_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.x1_4.setGeometry(QtCore.QRect(466, 180, 48, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.x1_4.setFont(font)
        self.x1_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x1_4.setObjectName("x1_4")
        self.x1_4.setAlignment(QtCore.Qt.AlignCenter)              
        self.x1_4.textChanged.connect(self.on_text_changed)
        self.gwalho_2 = QtWidgets.QLabel(self.centralwidget)
        self.gwalho_2.setGeometry(QtCore.QRect(446, 129, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.gwalho_2.setFont(font)
        self.gwalho_2.setObjectName("gwalho_2")
        self.gwalho_2.raise_()
        self.widget.raise_()
        self.ilban.raise_()
        self.twojum.raise_()
        self.arrow.raise_()
        self.exp_1.raise_()
        self.gwalho_1.raise_()
        self.x1_2.raise_()
        self.x1_1.raise_()
        self.y1_2.raise_()
        self.y1_1.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.frac_3.raise_()
        self.x.raise_()
        self.frac_1.raise_()
        self.x2.raise_()
        self.plus_2.raise_()
        self.frac_2.raise_()
        self.plus_1.raise_()
        self.a_1.raise_()
        self.a_2.raise_()
        self.b_2.raise_()
        self.b_1.raise_()
        self.c_2.raise_()
        self.c_1.raise_()
        self.line_3.raise_()
        self.y2_2.raise_()
        self.y2_1.raise_()
        self.x1_3.raise_()
        self.line_4.raise_()
        self.x1_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ilban.clicked.connect(self.dograph_f)
        self.twojum.clicked.connect(self.dojum_f)
        self.arrow.clicked.connect(self.work_f)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.x1_1, self.y1_1)
        MainWindow.setTabOrder(self.y1_1, self.x1_3)
        MainWindow.setTabOrder(self.x1_3, self.y2_1)
        MainWindow.setTabOrder(self.y2_1, self.x1_2)
        MainWindow.setTabOrder(self.x1_2, self.y1_2)
        MainWindow.setTabOrder(self.y1_2, self.x1_4)
        self.vbox = QtWidgets.QVBoxLayout(self.widget)
    def dojum_f(self):
        self.window= QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def  dograph_f(self):
        self.widget.raise_()
        g1=int(self.x1_1.text())/int((self.x1_2.text()))
        g2=int(self.x1_3.text())/int((self.x1_4.text()))
        g3=int(self.y1_1.text())/int((self.y1_2.text()))
        g4=int(self.y2_1.text())/int((self.y2_2.text()))

        y=frac(-1*g3+g4)
        a=frac(y/g1**2/g3**2)
        b=frac(-1*2*a*g1)
        c=frac(-1*a*g1**2-b*g1-g3)
        
        self.vbox.takeAt(0)
        self.p1=(b/(a*2)*-1)
        self.p2=a*self.p1**2+self.p1*b+c

        dynamic_canvas = FigureCanvas(Figure(figsize=(4, 3),facecolor='#dbebff'))
        self.vbox.addWidget(dynamic_canvas)

        self.dynamic_bx = dynamic_canvas.figure.subplots()
        self.dynamic_bx.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')
        #self.dynamic_bx.set_facecolor("#dbebff")
        self.dynamic_bx.clear()
        #self.dynamic_bx.plt.xlabel('x값')
        #self.dynamic_bx.plt.ylabel('y값')
        arr1=np.array([])
        arr2=np.array([])
        p=0.1
        o=0
        x=self.p1+0
        y=self.p2
        self.dynamic_bx.text(x+1, y-15, "point({}, {})".format(x, y), fontsize=10)
        self.dynamic_bx.scatter(x, y, c='black')
        self.dynamic_bx.set_title('Secondary Function')
        while 1:
            y=a*x**2+b*x+c+self.p2
            arr1=np.append(arr1,np.array([x]))
            arr2=np.append(arr2,np.array([y]))
            x+=p
            if y>400:
                o+=1
                p=-0.1
            elif y<-400:
                o+=1
                p=0.1
            if x>400:
                o+=1
                p=-0.1
            elif x<-400:
                o+=1
                p=0.1
            if o>3:
                break

        self.dynamic_bx.plot(arr1,arr2, color='deeppink')
        self.dynamic_bx.figure.canvas.draw()
    def work_f(self):
        self.x1=int(self.x1_1.text())
        self.x2=int(self.x1_2.text())
        self.x3=int(self.x1_3.text())
        self.x4=int(self.x1_4.text())
        self.y1=int(self.y1_1.text())
        self.y2=int(self.y1_2.text())
        self.y3=int(self.y2_1.text())
        self.y4=int(self.y2_2.text())

        self.y=frac(-1*self.y1/self.y2+self.y3/self.y4)
        self.a=frac(self.y/(self.x1/self.x2)**2/(self.y1/self.y2)**2)
        self.b=frac(-1*2*self.a*self.x1/self.x2)
        self.c=frac(-1*self.a*(self.x1/self.x2)**2-self.b*(self.x1/self.x2)-(self.y1/self.y2))
        self.a_1.setText(str(self.a.numerator))
        self.a_2.setText(str(self.a.denominator))
        self.b_1.setText(str(self.b.numerator))
        self.b_2.setText(str(self.b.denominator))
        
        self.c_1.setText(str(self.c.numerator))
        self.c_2.setText(str(self.c.denominator))

    def on_text_changed(self, text):
        width = self.x1_1.fontMetrics().width(text)
        self.x1_1.setMinimumWidth(width)
        width = self.x1_2.fontMetrics().width(text)
        self.x1_2.setMinimumWidth(width)
        width = self.x1_3.fontMetrics().width(text)
        self.x1_3.setMinimumWidth(width)
        width = self.x1_4.fontMetrics().width(text)
        self.x1_4.setMinimumWidth(width)
        width = self.y1_1.fontMetrics().width(text)
        self.y1_1.setMinimumWidth(width)
        width = self.y1_2.fontMetrics().width(text)
        self.y1_2.setMinimumWidth(width)
        width = self.y2_1.fontMetrics().width(text)
        self.y2_1.setMinimumWidth(width)
        width = self.y2_2.fontMetrics().width(text)
        self.y2_2.setMinimumWidth(width)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "이차함수의 두 점의 좌표"))
        self.ilban.setText(_translate("MainWindow", "그래프 그리기"))
        self.twojum.setText(_translate("MainWindow", "일반형으로 구하기"))
        self.exp_1.setText(_translate("MainWindow", "두 점의 좌표:"))
        self.gwalho_1.setText(_translate("MainWindow", "(            ,            )"))
        self.x1_2.setText(_translate("MainWindow", "1"))
        self.x1_1.setText(_translate("MainWindow", "x"))
        self.y1_2.setText(_translate("MainWindow", "1"))
        self.y1_1.setText(_translate("MainWindow", "y"))
        self.x.setText(_translate("MainWindow", "x"))
        self.x2.setText(_translate("MainWindow", "x²"))
        self.plus_2.setText(_translate("MainWindow", "+"))
        self.plus_1.setText(_translate("MainWindow", "+"))
        self.a_1.setText(_translate("MainWindow", "a"))
        self.a_2.setText(_translate("MainWindow", "1"))
        self.b_2.setText(_translate("MainWindow", "1"))
        self.b_1.setText(_translate("MainWindow", "b"))
        self.c_2.setText(_translate("MainWindow", "1"))
        self.c_1.setText(_translate("MainWindow", "c"))
        self.y2_2.setText(_translate("MainWindow", "1"))
        self.y2_1.setText(_translate("MainWindow", "y"))
        self.x1_3.setText(_translate("MainWindow", "x"))
        self.x1_4.setText(_translate("MainWindow", "1"))
        self.gwalho_2.setText(_translate("MainWindow", "(            ,            )"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
