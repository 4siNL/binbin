import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = sqlite3.connect('coffee.sqlite')
        cur = db.cursor()
        coffee = cur.execute('''SELECT * FROM coffee''').fetchall()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Кофе',
                                                    'название сорта',
                                                    'степень обжарки',
                                                    'молотый/в зернах',
                                                    'описание вкуса', 'цена',
                                                    'объем упаковки'])
        self.tableWidget.setRowCount(0)
        for i, j in enumerate(coffee):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(j[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(j[1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(j[2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(j[3])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(j[4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(j[5])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(j[6])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(j[7])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())