#!/usr/bin/env python
#!/usr/bin/env python3
from PyQt5 import QtWidgets
import sys
from ui.mainUI import Ui_mainWindow


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

       
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()

    
if __name__ == "__main__":
    main()