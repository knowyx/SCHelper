#!/usr/bin/env python
#!/usr/bin/env python3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication([])
window = uic.loadUi("main.ui")

window.show()
app.exec_()


