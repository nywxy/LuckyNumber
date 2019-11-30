import sys
from jxluckywindow import *
from PyQt5.QtWidgets import QApplication

from dataoption import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = dbase()
    print(db.getAllData("termtable")[:10])
    mainWnd = JxLucky()
    sys.exit(app.exec_())
