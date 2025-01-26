from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication([])

# Загружаем файл .ui
window = uic.loadUi("main.ui")

window.show()
app.exec_()
