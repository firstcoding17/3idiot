import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import pandas as pd
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import time
import calendar
import pandas as pd
import os

class Data(QMainWindow):

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
        self.initUI('CSV/test.csv')


    #너비 1200 넓이 800
    def initUI(self,File):
        self.df = pd.read_csv(File)
        self.df_row_count = len(self.df)+1
        self.df_column_count = len(self.df.columns)
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        Filemenu = menubar.addMenu('&File')
        Graph = menubar.addMenu('Graph')
        Tool = menubar.addMenu('&Tool')
        Help = menubar.addMenu("&Help")

        self.tablewidget=QTableWidget(self)
        self.tablewidget.setRowCount(self.df_row_count)
        self.tablewidget.resize(1200,800)
        self.tablewidget.setColumnCount(self.df_column_count)


        self.df_list =list(self.df)

        self.insert_data()













        self.statusBar()

        self.showtime()
        self.setWindowTitle('세얼간이')
        self.move(0, 300)
        self.resize(1200, 800)
        self.show()

    def insert_data(self):


        for i in range(0, self.df_row_count):
            if i == 0:
                for j in range(0, self.df_column_count):
                    self.tablewidget.setItem(i, j, QTableWidgetItem(self.df_list[j]))
            else:
                for j in range(0, self.df_column_count):
                    self.tablewidget.setItem(i, j, QTableWidgetItem(str(self.df[self.df_list[j]][i-1])))

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
   ex = Data()
   sys.exit(app.exec_())