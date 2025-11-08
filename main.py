#!/usr/bin/env python
#!/usr/bin/env python3
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFontDatabase
import sys
from ui.mainUI import Ui_mainWindow

class mainWindow(QtWidgets.QWidget):
    def __init__(self, font):
        super(mainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self, font)

       
def main():
    app = QtWidgets.QApplication(sys.argv)
    font = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont("resources/font.ttf"))[0]
    window = mainWindow(font)
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()