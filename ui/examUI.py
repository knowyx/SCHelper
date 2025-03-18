# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from resources.jsonWorker import read
from random import randrange
FILE = "resources/exercises.json"
data = read(FILE)
BOXSTYLESHEETS = """
            QWidget {
                background-color:rgb(255, 166, 103);
                padding: 3;
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
                font-size: 13px;
                color: black;
            }
            QScrollBar:vertical {
                border 1px;
                width: 13px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #888;
                min-height: 20px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #555;
            }
            QScrollBar::handle:vertical:pressed {
                background: #333;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }      
        """


class Ui_exam(object):
    def setupUi(self, exam):
        exam.setObjectName("exam")
        exam.resize(915, 499)
        exam.setMinimumSize(QtCore.QSize(640, 480))
        exam.setWindowIcon(QtGui.QIcon('icon.ico'))
        exam.setStyleSheet("""
            background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0             rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));
        """)
        self.gridLayout = QtWidgets.QGridLayout(exam)
        self.gridLayout.setObjectName("gridLayout")
        self.condBox = QtWidgets.QGroupBox(exam)
        self.condBox.setStyleSheet(BOXSTYLESHEETS)
        self.condBox.setTitle("")
        self.condBox.setObjectName("condBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.condBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.condition = QtWidgets.QLabel(self.condBox)
        self.condition.setWordWrap(True) 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condition.sizePolicy().hasHeightForWidth())
        self.condition.setSizePolicy(sizePolicy)
        self.condition.setStyleSheet("font-size: 15px;")
        self.condition.setObjectName("condition")
        self.verticalLayout_3.addWidget(self.condition)
        self.gridLayout.addWidget(self.condBox, 2, 0, 1, 1)
        self.title = QtWidgets.QLabel(exam)
        self.title.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: white;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 2)
        self.answerBox = QtWidgets.QGroupBox(exam)
        self.answerBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.answerBox.setStyleSheet(BOXSTYLESHEETS)
        self.answerBox.setTitle("")
        self.answerBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.answerBox.setObjectName("answerBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.answerBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(self.answerBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMaximumSize(QtCore.QSize(300, 30))
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.status = QtWidgets.QLabel(self.answerBox)
        self.status.setWordWrap(True) 
        self.status.setMaximumSize(QtCore.QSize(300, 60))
        self.status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.giveAns = QtWidgets.QLineEdit(self.answerBox)
        self.giveAns.setMaximumSize(QtCore.QSize(300, 16777215))
        self.giveAns.setObjectName("giveAns")
        self.verticalLayout.addWidget(self.giveAns)
        self.checkButton = QtWidgets.QPushButton(self.answerBox)
        self.checkButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.checkButton.setObjectName("checkButton")
        self.verticalLayout.addWidget(self.checkButton)
        self.nextButton = QtWidgets.QPushButton(self.answerBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout.addWidget(self.nextButton)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.answerBox, 2, 1, 1, 1)
        self.retranslateUi(exam)
        QtCore.QMetaObject.connectSlotsByName(exam)
        self.checkButton.clicked.connect(lambda: self.check())
        self.nextButton.clicked.connect(lambda: self.update())
        

    def retranslateUi(self, exam):
        _translate = QtCore.QCoreApplication.translate
        exam.setWindowTitle(_translate("exam", "SCHelper — Подготовка к экзаменам"))
        self.condition.setText(_translate("exam", "Нажмите \"Следующая задача\" для генерации задачи"))
        self.title.setText(_translate("exam", "Подготовка к экзаменам"))
        self.header.setText(_translate("exam", "Ваш ответ: (в СИ, без едениц измерения)"))
        self.status.setText(_translate("exam", "Не дан"))
        self.checkButton.setText(_translate("exam", "Проверить ответ"))
        self.nextButton.setText(_translate("exam", "Следующая задача"))

    def update(self):
        exercise = data[randrange(len(data))]
        self.condition.setText(exercise['condition'])
        self.status.setText('Не дан')
        self.ans = exercise['answer']

    def isCorrect(self, num):
        isDig = False
        dotIn = False

        for x in num:
            if x.isdigit():
                isDig = True
            elif x == '.':
                if dotIn:
                    return False
                dotIn = True
            else:
                return False

        return isDig

    def check(self):
        if self.isCorrect(self.giveAns.text()):
            if float(self.giveAns.text()) == self.ans:
                self.status.setText("✅ Верно")
            else:
                self.status.setText(f"❎ Неверно или не дан ответ (правиильный ответ: {self.ans})")
        else:
            self.status.setText("❎ Ответ не дан или он должен быть числом (дробные числа вводятся через точку)")
