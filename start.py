import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtGui import QIcon
#참고용입니다

class MyApp(QMainWindow):
    name = ''
    type = ''
    amount = ''

    def __init__(self):
        super().__init__()
        self.initUI()

    #너비 1200 넓이 800
    def initUI(self):

        self.btn_name = QPushButton('이름', self)
        self.btn_name.move(0,35)
        self.btn_name.clicked.connect(self.showname)

        self.le = QLineEdit(self)
        self.le.move(0,0)

        self.btn_type = QPushButton('성향', self)
        self.btn_type.move(100,35)
        self.btn_type.clicked.connect(self.showType)

        self.ty = QLineEdit(self)
        self.ty.move(100,0)

        self.btn_Amount = QPushButton('계좌', self)
        self.btn_Amount.move(200, 35)
        self.btn_Amount.clicked.connect(self.showAM)

        self.AM = QLineEdit(self)
        self.AM.move(200, 0)

        self.btn_useradd = QPushButton('유저 추가',self)
        self.btn_useradd.move(400,35)


        self.btn_serch_name = QPushButton('이름',self)
        self.btn_serch_name.move(0,235)
        self.btn_serch_name.clicked.connect(self.showS_N)

        self.S_N = QLineEdit(self)
        self.S_N.move(0,200)

        self.btn_serch_Date = QPushButton('검색 날짜',self)
        self.btn_serch_Date.move(100,235)
        self.btn_serch_Date.clicked.connect(self.serch_Date)

        self.S_D = QLineEdit(self)
        self.S_D.move(100,200)






        self.btn_serch = QPushButton('검색', self)
        self.btn_serch.move(400, 250)

        self.setWindowTitle('ESG 투자성향')
        self.move(0, 0)
        self.resize(500, 300)
        self.show()



    def showname(self):
        text, ok = QInputDialog.getText(self,'input', '이름 입력')
        if ok:
            self.le.setText(str(text))
    def showType(self):
        text, ok = QInputDialog.getText(self, 'input', '투자성향 입력')
        if ok:
            self.ty.setText(str(text))

    def showAM(self):
        text, ok = QInputDialog.getInt(self, 'input', '투자금 입력')
        if ok:
            self.AM.setText(str(text))

    def showS_N(self):
        text, ok = QInputDialog.getText(self, 'input', '검색할 이름 입력')
        if ok:
            self.S_N.setText(str(text))
    def serch_Date(self):
        text, ok = QInputDialog.getText(self, 'input', '검색할 이름 입력')
        if ok:
            self.S_D.setText(str(text))


















if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
