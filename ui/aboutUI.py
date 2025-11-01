# -*- coding: utf-8 -*-
#импорт и константы
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import webbrowser
TOPBUTTONSSTYLE ="""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: black;
                margin-left: 70px;
                margin-right: 70px;
            }
            QPushButton:hover { 
                background-color:rgb(244, 81, 0);
            }
        """
FILE = "resources/aboutText.txt"
VERFILE = "resources/ver"


def getText(file, verfile):
    text = ''
    with open(file) as f:
        line = f.readline()
        while line:
            text += line
            line = f.readline()
    with open(verfile) as f:
        ver = f.readline()
    return text.format(ver=ver)


class Ui_about(object):
    def setupUi(self, about, mainFont):
        about.setObjectName("about")
        about.resize(1000, 500)
        about.setMinimumSize(QtCore.QSize(800, 600))
        about.setWindowIcon(QtGui.QIcon('icon.ico'))
        about.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0"
                            "             rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QFont(mainFont, 12)
        paragrathFont = QFont(mainFont, 10)
        font.setBold(True)
        paragrathFont.setBold(True)
        #/\работа с окном
        self.verticalLayout = QtWidgets.QVBoxLayout(about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutHeader = QtWidgets.QLabel(about)
        self.aboutHeader.setMaximumSize(QtCore.QSize(16777215, 30))
        self.aboutHeader.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: black;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.aboutHeader.setAlignment(Qt.AlignmentFlag.AlignLeading|
                                      Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.aboutHeader.setObjectName("aboutHeader")
        self.verticalLayout.addWidget(self.aboutHeader)
        #/\хедер виджита
        self.infoBox = QtWidgets.QGroupBox(about)
        self.infoBox.setStyleSheet("background-color: none; border: none;")
        self.infoBox.setObjectName("infoBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.infoBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.projectInfo = QtWidgets.QLabel(self.infoBox)
        self.projectInfo.setStyleSheet("""
            QWidget {
                background-color:rgb(255, 166, 103);
                padding: 3;
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
                color: black;
            }
        """)
        self.projectInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.projectInfo.setWordWrap(True)
        self.projectInfo.setObjectName("projectInfo")
        self.verticalLayout_2.addWidget(self.projectInfo)
        self.verticalLayout.addWidget(self.infoBox)
        #/\блок основной информации
        self.gitButton = QtWidgets.QPushButton(about)
        self.gitButton.setMinimumSize(QtCore.QSize(0, 50))
        self.gitButton.setStyleSheet(TOPBUTTONSSTYLE)
        self.gitButton.setObjectName("gitButton")
        self.verticalLayout.addWidget(self.gitButton)
        #/\кнопка ссылки на гит
        self.lyceumWebButton = QtWidgets.QPushButton(about)
        self.lyceumWebButton.setMinimumSize(QtCore.QSize(0, 50))
        self.lyceumWebButton.setStyleSheet(TOPBUTTONSSTYLE)
        self.lyceumWebButton.setObjectName("lyceumWebButton")
        self.verticalLayout.addWidget(self.lyceumWebButton)
        #/\ссылка на сайт лицея
        self.contactButtons = QtWidgets.QGroupBox(about)
        self.contactButtons.setMaximumSize(QtCore.QSize(16777215, 70))
        self.contactButtons.setStyleSheet("background-color: none; border: none;")
        self.contactButtons.setObjectName("contactsButton")
        self.contactsLayout = QtWidgets.QHBoxLayout(self.contactButtons)
        self.contactsLayout.setObjectName("contactsLayout")
        #/\лейаут для кнопок контактов
        self.telegramButton = QtWidgets.QPushButton(self.contactButtons)
        self.telegramButton.setMinimumSize(QtCore.QSize(0, 50))
        self.telegramButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: black;
                margin-left: 60px;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }      
        """)
        self.telegramButton.setObjectName("telegramButton")
        self.contactsLayout.addWidget(self.telegramButton)
        #/\кнопка связи в телеграм
        self.mailtoButton = QtWidgets.QPushButton(self.contactButtons)
        self.mailtoButton.setMinimumSize(QtCore.QSize(0, 50))
        self.mailtoButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: black;
                margin-right: 60px;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }      
        """)
        self.mailtoButton.setObjectName("mailtoButton")
        #/\кнопка связи по почте
        self.contactsLayout.addWidget(self.mailtoButton)
        self.verticalLayout.addWidget(self.contactButtons)
        #/\работа с лейаутами
        self.gitButton.clicked.connect(lambda: webbrowser.open('https://github.com/knowyx/SCHelper'))
        self.lyceumWebButton.clicked.connect(lambda: webbrowser.open('http://www.kirov.spb.ru/sc/393/index.php'))
        self.telegramButton.clicked.connect(lambda: webbrowser.open('https://t.me/knowyx'))
        self.mailtoButton.clicked.connect(lambda: webbrowser.open('mailto:knowyx@gmail.com'))
        #/\назначение ссылок на кнопки
        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)
        self.aboutHeader.setFont(font)
        self.projectInfo.setFont(paragrathFont)
        self.gitButton.setFont(font)
        self.lyceumWebButton.setFont(font)
        self.telegramButton.setFont(font)
        self.mailtoButton.setFont(font)
        #/\установка шрифтов и текста на элементы

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "SCHelper — Справка"))
        self.aboutHeader.setText(_translate("about", "Справка"))
        self.projectInfo.setText(_translate("about", getText(FILE, VERFILE)))
        self.gitButton.setText(_translate("about", "GitHub"))
        self.lyceumWebButton.setText(_translate("about", "Сайт Лицея"))
        self.telegramButton.setText(_translate("about", "Автор в телеграм"))
        self.mailtoButton.setText(_translate("about", "Почта автора"))
