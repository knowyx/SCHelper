#!/usr/bin/env python
#!/usr/bin/env python3
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
import sys
from ui.mainUI import Ui_mainWindow
from PyQt5.QtGui import QFont, QFontDatabase
from ui.timetableUI import Ui_timetable


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


class timetableWindow(QtWidgets.QWidget):
    def __init__(self):
        super(timetableWindow, self).__init__()
        self.ui = Ui_timetable()
        self.ui.setupUi(self)
   

def runSecWindow(info):
   global timetableW
   if info == 'Расписание':
       timetableW = timetableWindow()
       timetableW.show()

       
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()