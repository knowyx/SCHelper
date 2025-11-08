# -*- coding: utf-8 -*-
#костанты и импорты
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from resources.csvWorker import read
from random import randrange
FILE = "resources/exercises.csv"
data = read(FILE)
BOXSTYLESHEETS = """
            QWidget {
                background-color:rgb(255, 166, 103);
                padding: 3;
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
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
    def setupUi(self, exam, mainFont):
        exam.setObjectName("exam")
        exam.resize(1000, 600)
        exam.setMinimumSize(QtCore.QSize(800, 600))
        exam.setWindowIcon(QtGui.QIcon('icon.ico'))
        exam.setStyleSheet("""
            background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0
                         rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));
        """)
        font = QFont(mainFont, 14)
        font.setBold(True)
        #/\ работа с окошком, шрифтом
        self.mainGrid = QtWidgets.QGridLayout(exam)
        self.mainGrid.setObjectName("mainGrid")
        self.condBox = QtWidgets.QGroupBox(exam)
        self.condBox.setStyleSheet(BOXSTYLESHEETS)
        self.condBox.setTitle("")
        self.condBox.setObjectName("condBox")
        self.condLayout = QtWidgets.QVBoxLayout(self.condBox)
        self.condLayout.setObjectName("condLayout")
        self.condition = QtWidgets.QLabel(self.condBox)
        self.condition.setWordWrap(True)
        self.condition.setObjectName("condition")
        self.condLayout.addWidget(self.condition)
        self.mainGrid.addWidget(self.condBox, 2, 0, 1, 1)
        #/\работа с главной сеткой и условием
        self.title = QtWidgets.QLabel(exam)
        self.title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.title.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: black;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.title.setObjectName("title")
        self.mainGrid.addWidget(self.title, 1, 0, 1, 2)
        #/\работа с верхне подписью
        self.answerBox = QtWidgets.QGroupBox(exam)
        self.answerBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.answerBox.setStyleSheet(BOXSTYLESHEETS)
        self.answerBox.setTitle("")
        self.answerBox.setAlignment(Qt.AlignmentFlag.AlignLeading
                                    |Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.answerBox.setObjectName("answerBox")
        self.ansLayout = QtWidgets.QVBoxLayout(self.answerBox)
        self.ansLayout.setObjectName("ansLayout")
        #/\лейаут для правой части программы (место для ввода ответа)
        self.header = QtWidgets.QLabel(self.answerBox)
        self.header.setObjectName("header")
        self.ansLayout.addWidget(self.header)
        #/\подсказка для воода ответа
        self.status = QtWidgets.QLabel(self.answerBox)
        self.header.setWordWrap(True)
        self.status.setAlignment(Qt.AlignmentFlag.AlignLeading
                                 |Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.status.setObjectName("status")
        self.status.setWordWrap(True)
        self.ansLayout.addWidget(self.status)
        #/\статус ответа
        self.giveAns = QtWidgets.QLineEdit(self.answerBox)
        self.giveAns.setMaximumSize(QtCore.QSize(400, 16777215))
        self.giveAns.setObjectName("giveAns")
        self.ansLayout.addWidget(self.giveAns)
        #/\ответ, данный пользователем
        self.checkButton = QtWidgets.QPushButton(self.answerBox)
        self.checkButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.checkButton.setObjectName("checkButton")
        self.ansLayout.addWidget(self.checkButton)
        #/\кнопка проверки ответа
        self.nextButton = QtWidgets.QPushButton(self.answerBox)
        self.nextButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.nextButton.setObjectName("nextButton")
        self.ansLayout.addWidget(self.nextButton)
        #/\кнопка следующей задачи
        self.mainGrid.addWidget(self.answerBox, 2, 1, 1, 1)
        self.retranslateUi(exam)
        QtCore.QMetaObject.connectSlotsByName(exam)
        self.checkButton.clicked.connect(lambda: self.check())
        self.nextButton.clicked.connect(lambda: self.update())
        self.condition.setFont(font)
        self.title.setFont(font)
        self.header.setFont(font)
        self.status.setFont(font)
        self.checkButton.setFont(font)
        self.nextButton.setFont(font)
        #/\работа с сеткой, тексом на объектах и шрифтами
        

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
        #подстановка новой задачи
        exercise = data[randrange(len(data))]
        self.condition.setText(exercise['condition'])
        self.status.setText('Не дан')
        self.ans = float(exercise['answer'])

    def isCorrect(self, num):
        #проаверка на то, является ли число цифрой
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
        #сверка ответа
        try:
            if self.isCorrect(self.giveAns.text()):
                if float(self.giveAns.text()) == self.ans:
                    self.status.setText("✅ Верно")
                else:
                    self.status.setText(f"❎ Неверно или не дан ответ (правиильный ответ: {self.ans})")
            else:
                self.status.setText("❎ Ответ не дан или он должен быть числом (дробные числа вводятся через точку)")
        except ValueError:
            self.status.setText("❎ Ответ не дан или он должен быть числом (дробные числа вводятся через точку)")
        except AttributeError:
            self.status.setText("❎ Вы еще не получили задачу")
