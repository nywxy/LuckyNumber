import sys
from ui.jxluckymain import *
from PyQt5.QtWidgets import QMainWindow

class JxLucky :
    def __init__(self):
        self.mainWnd = QMainWindow()
        self.mainUI = Ui_MainWindow()
        self.mainUI.setupUi(self.mainWnd)
        self.mainWnd.show()









