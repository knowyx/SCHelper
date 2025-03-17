# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
TOPBUTTONSSTYLE ="""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: white;
                margin-left: 70px;
                margin-right: 70px
            }
            QPushButton:hover { 
                background-color:rgb(244, 81, 0);
            }
        """


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(915, 499)
        about.setMinimumSize(QtCore.QSize(640, 480))
        about.setWindowIcon(QtGui.QIcon('icon.ico'))
        about.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0             rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutHeader = QtWidgets.QLabel(about)
        self.aboutHeader.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aboutHeader.setFont(font)
        self.aboutHeader.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: white;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.aboutHeader.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aboutHeader.setObjectName("aboutHeader")
        self.verticalLayout.addWidget(self.aboutHeader)
        self.infoBox = QtWidgets.QGroupBox(about)
        self.infoBox.setStyleSheet("background-color: none; border: none;")
        self.infoBox.setTitle("")
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
                font-size: 13px;
                color: black;
            }
        """)
        self.projectInfo.setWordWrap(True)
        self.projectInfo.setObjectName("projectInfo")
        self.verticalLayout_2.addWidget(self.projectInfo)
        self.verticalLayout.addWidget(self.infoBox)
        self.gitButton = QtWidgets.QPushButton(about)
        self.gitButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gitButton.setFont(font)
        self.gitButton.setStyleSheet(TOPBUTTONSSTYLE)
        self.gitButton.setObjectName("gitButton")
        self.verticalLayout.addWidget(self.gitButton)
        self.lyceumWebButton = QtWidgets.QPushButton(about)
        self.lyceumWebButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lyceumWebButton.setFont(font)
        self.lyceumWebButton.setStyleSheet(TOPBUTTONSSTYLE)
        self.lyceumWebButton.setObjectName("lyceumWebButton")
        self.verticalLayout.addWidget(self.lyceumWebButton)
        self.contactsButton = QtWidgets.QGroupBox(about)
        self.contactsButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.contactsButton.setStyleSheet("background-color: none; border: none;")
        self.contactsButton.setTitle("")
        self.contactsButton.setObjectName("contactsButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.contactsButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.telegramButton = QtWidgets.QPushButton(self.contactsButton)
        self.telegramButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.telegramButton.setFont(font)
        self.telegramButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: white;
                margin-left: 60px;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }      
        """)
        self.telegramButton.setObjectName("telegramButton")
        self.horizontalLayout_2.addWidget(self.telegramButton)
        self.mailtoButton = QtWidgets.QPushButton(self.contactsButton)
        self.mailtoButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mailtoButton.setFont(font)
        self.mailtoButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: white;
                margin-right: 60px;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }      
        """)
        self.mailtoButton.setObjectName("mailtoButton")
        self.horizontalLayout_2.addWidget(self.mailtoButton)
        self.verticalLayout.addWidget(self.contactsButton)
        self.gitButton.clicked.connect(lambda: webbrowser.open('https://github.com/knowyx/SCHelper'))
        self.lyceumWebButton.clicked.connect(lambda: webbrowser.open('http://www.kirov.spb.ru/sc/393/index.php'))
        self.telegramButton.clicked.connect(lambda: webbrowser.open('https://t.me/knowyx'))
        self.mailtoButton.clicked.connect(lambda: webbrowser.open('mailto:knowyx@gmail.com'))
        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "SCHelper — Справка"))
        self.aboutHeader.setText(_translate("about", "Справка"))
        self.projectInfo.setText(_translate(
        "about",
        "Программа для ЭВМ \"'SCHelper\" версии 1.0 создана Конжиным Никитой, "
        "учеником 9А класса Лицея №393 Кировского Района города Санкт-Петербурга, "
        "для проекта по программированию. Вся требуемая документация предоставлена "
        "преподавателю в письме. Репозиторий доступен для свободного распространения "
        "в рамках лицензии GNU GPL V3 и скачивания на странице GitHub.\n"
        "Логотип сгеренерирован неиросетью ChatGPT\n"
        "Иконка \"Удалить\" взята с сайта freeicons.io"
        ))
        self.gitButton.setText(_translate("about", "GitHub"))
        self.lyceumWebButton.setText(_translate("about", "Сайт Лицея"))
        self.telegramButton.setText(_translate("about", "Автор в телеграм"))
        self.mailtoButton.setText(_translate("about", "Почта автора"))
