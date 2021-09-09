import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtGui import QIcon
import pandas as pd
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import time
import calendar
import GUI.Data as Data
import os

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.year = int()
        self.month = int()
        self.day = int()
        self.hour = int()
        self.min = int()
        self.sec = int()
        self.wDay = int()
        self.week = ['월', '화', '수', '목', '금', '토', '일']
        self.workweek = ['월', '화', '수', '목', '금']
        self.Datecountstr = ''
        self.initUI()
        self.initUI()

    #너비 1200 넓이 800
    def initUI(self):


        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        Filemenu = menubar.addMenu('&File')
        Graph = menubar.addMenu('Graph')
        Tool = menubar.addMenu('&Tool')
        Help = menubar.addMenu("&Help")

        self.button_start_work = QPushButton('시작',self)
        self.button_start_work.resize(50,50)
        self.button_start_work.move(80,100)
        self.button_start_work.clicked.connect(self.start())#시작 불러오기

        self.button_start_work = QPushButton('종료', self)
        self.button_start_work.resize(50, 50)
        self.button_start_work.move(180, 100)
        # self.button_start_work.clicked.connect()#시작 불러오기





        self.statusBar()

        self.showtime()
        self.setWindowTitle('세얼간이')
        self.move(500, 300)
        self.resize(300, 300)
        self.show()

    def start(self):
        file_list = os.listdir('CSV')
        items = tuple(file_list)
        item,ok = QInputDialog.getItem(self,'파일 선택', '파일을 선택하세요.',items,0,False)
        if ok:
            app = Data.QApplication(sys.argv)
            ex = Data.Data()
            ex.set_file(item)
            sys.exit(app.exec_())
            Data.Data

    def showtime(self):
        date = QDate.currentDate()
        time = QTime.currentTime()

        # LCD 표시
        self.year = date.year()
        self.month = date.month()
        self.day = date.day()
        self.hour = time.hour()
        self.min = time.minute()
        self.sec = time.second()
        self.wDay = date.dayOfWeek()

        self.Datecountstr = str(self.year) + ' - ' + str(self.month) + ' - ' + str(self.day) + '   ' + str(
            self.hour) + ' : ' + str(self.min) + ' : ' + str(self.sec) + '     ' + str(self.week[self.wDay - 1])
        self.statusBar().showMessage(self.Datecountstr)
        print(self.Datecountstr)

        # 타이머 설정  (1초마다, 콜백함수)
        end_month = calendar.monthrange(self.year, self.month)[1]
        timer = Timer(1, self.showtime)
        timer.start()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
