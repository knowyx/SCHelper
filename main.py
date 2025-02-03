#!/usr/bin/env python
#!/usr/bin/env python3
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
import sys
from mainUI import Ui_MainWindow
from PyQt5.QtGui import QFont, QFontDatabase
from ui2 import timetable

window = None
timetableW = None

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def hide(self):
        self.close()


class timetableWindow(QtWidgets.QWidget):
    def __init__(self):
        super(timetableWindow, self).__init__()
        self.ui = timetable()
        self.ui.setupUi(self)
   
def runSecWindow(info):
   global timetableW
   if info == 'Расписание':
       timetableW = timetableWindow()
       # window.hide()
       timetableW.show()

       

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    # window.getUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()