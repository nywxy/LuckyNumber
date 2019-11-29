import sys
from jxluckywindow import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = JxLucky()
    sys.exit(app.exec_())