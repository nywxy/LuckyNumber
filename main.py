# from dataoption import dbase

# db = dbase()

# db.dbOptionWithSql("select * from TermTable where term>2019000")
# print(db.cursor.fetchall())

from ui.jxluckymain import *
import sys
from PyQt5 import QtCore,QtGui,QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())