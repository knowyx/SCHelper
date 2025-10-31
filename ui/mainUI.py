# -*- coding: utf-8 -*-
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from ui.timetableUI import Ui_timetable
from ui.crontabUI import Ui_crontab
from ui.examUI import Ui_exam
from ui.aboutUI import Ui_about
BUTTONSTYLESHEET = """
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: black;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }
        """
NAMEANDCOPYRIGHTSTYLESHEET = """
            background-color: none;
            color: black;
            font-weight: bold;
        """


class timetableWindow(QtWidgets.QWidget):
    def __init__(self):
        super(timetableWindow, self).__init__()
        self.ui = Ui_timetable()
        self.ui.setupUi(self)


class cronWindow(QtWidgets.QWidget):
    def __init__(self):
        super(cronWindow, self).__init__()
        self.ui = Ui_crontab()
        self.ui.setupUi(self)


class examWindow(QtWidgets.QWidget):
    def __init__(self):
        super(examWindow, self).__init__()
        self.ui = Ui_exam()
        self.ui.setupUi(self)


class aboutWindow(QtWidgets.QWidget):
    def __init__(self):
        super(aboutWindow, self).__init__()
        self.ui = Ui_about()
        self.ui.setupUi(self)


class Ui_mainWindow(object):
    def button_clicked(self, info):
        if info == 'Расписание':
            global timetableW
            timetableW = timetableWindow()
            timetableW.show()
        elif info == 'Планировщик задач':
            global crontabW
            crontabW = cronWindow()
            crontabW.show()
        elif info == 'Подготовка к экзаменам':
            global examW
            examW = examWindow()
            examW.show()
        elif info == 'Справка':
            global aboutW
            aboutW = aboutWindow()
            aboutW.show()


    def setupUi(self, mainWindow, mainFont):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(917, 499)
        mainWindow.setMinimumSize(QtCore.QSize(640, 480))
        mainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        font = QtGui.QFont(mainFont, 10)
        bigFont = QtGui.QFont(mainFont, 14)
        mainWindow.setFont(bigFont)
        mainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0             rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(mainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowGrid = QtWidgets.QGridLayout()
        self.windowGrid.setContentsMargins(100, -1, 100, -1)
        self.windowGrid.setObjectName("windowGrid")
        self.logoNameLayout = QtWidgets.QHBoxLayout()
        self.logoNameLayout.setContentsMargins(0, -1, 0, -1)
        self.logoNameLayout.setObjectName("logoNameLayout")
        # /\ работа с окном
        self.logo = QtWidgets.QLabel(mainWindow)
        self.logo.setMaximumSize(QtCore.QSize(100, 100))
        self.logo.setStyleSheet("background-color: none")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resources/LOGO.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logoNameLayout.addWidget(self.logo)
        self.name = QtWidgets.QLabel(mainWindow)
        self.name.setStyleSheet(NAMEANDCOPYRIGHTSTYLESHEET)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name.setObjectName("name")
        self.logoNameLayout.addWidget(self.name)
        self.windowGrid.addLayout(self.logoNameLayout, 2, 0, 1, 1)
        #/\работа с логотипом и названием программы
        self.corntabButt = QtWidgets.QPushButton(mainWindow)
        self.corntabButt.setMinimumSize(QtCore.QSize(150, 50))
        self.corntabButt.setMaximumSize(QtCore.QSize(16777215, 150))
        self.corntabButt.clicked.connect(lambda: self.button_clicked(info = 'Планировщик задач'))
        self.corntabButt.setStyleSheet(BUTTONSTYLESHEET)
        self.corntabButt.setObjectName("corntabButt")
        self.windowGrid.addWidget(self.corntabButt, 5, 0, 1, 1)
        #/\кнопка планировщика
        self.timetableButt = QtWidgets.QPushButton(mainWindow)
        self.timetableButt.setMinimumSize(QtCore.QSize(150, 50))
        self.timetableButt.setMaximumSize(QtCore.QSize(16777215, 150))
        self.timetableButt.clicked.connect(lambda: self.button_clicked(info = 'Расписание'))
        self.timetableButt.setStyleSheet(BUTTONSTYLESHEET)
        self.timetableButt.setObjectName("timetableButt")
        self.windowGrid.addWidget(self.timetableButt, 4, 0, 1, 1)
        #/\кнопка расписания
        self.aboutButt = QtWidgets.QPushButton(mainWindow)
        self.aboutButt.setMinimumSize(QtCore.QSize(150, 50))
        self.aboutButt.setMaximumSize(QtCore.QSize(16777215, 150))
        self.aboutButt.setBaseSize(QtCore.QSize(873, 497))
        self.aboutButt.clicked.connect(lambda: self.button_clicked(info = 'Справка'))
        self.aboutButt.setStyleSheet(BUTTONSTYLESHEET)
        self.aboutButt.setObjectName("aboutButt")
        self.windowGrid.addWidget(self.aboutButt, 7, 0, 1, 1)
        #/\кнопка справки
        self.examButt = QtWidgets.QPushButton(mainWindow)
        self.examButt.setMinimumSize(QtCore.QSize(150, 50))
        self.examButt.setMaximumSize(QtCore.QSize(16777215, 150))
        self.examButt.clicked.connect(lambda: self.button_clicked(info = 'Подготовка к экзаменам'))
        self.examButt.setStyleSheet(BUTTONSTYLESHEET)
        self.examButt.setObjectName("examButt")
        self.windowGrid.addWidget(self.examButt, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.windowGrid)
        #/\кнопка подготовки к экзаменам
        self.copyright = QtWidgets.QLabel(mainWindow)
        self.copyright.setMaximumSize(QtCore.QSize(16777215, 15))
        self.copyright.setStyleSheet(NAMEANDCOPYRIGHTSTYLESHEET)
        self.copyright.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.copyright.setObjectName("copyright")
        self.copyright.setFont(font)
        #/\работа с копирайтом
        self.verticalLayout.addWidget(self.copyright)
        self.retranslateUi(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "SCHelper — Универсальный помощник школьника"))
        self.name.setText(_translate("mainWindow", "Универсальный помощник школьника"))
        self.corntabButt.setText(_translate("mainWindow", "Планировщик задач"))
        self.timetableButt.setText(_translate("mainWindow", "Расписание"))
        self.aboutButt.setText(_translate("mainWindow", "Справка"))
        self.examButt.setText(_translate("mainWindow", "Подготовка к экзаменам"))
        self.copyright.setText(_translate("mainWindow", "SCHelper 2.0 ©Конжин Н.А. 2025"))