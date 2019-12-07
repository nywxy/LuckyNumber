import sys
from jxluckywindow import *
from PyQt5.QtWidgets import QApplication

from MyMongo import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = myDb()
    mainWnd = JxLucky()
    sys.exit(app.exec_())
