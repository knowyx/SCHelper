# -*- coding: utf-8 -*-
# импорт библиотек и функций
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGroupBox, QMessageBox
from resources.dbWorker import read, delete, writer
from datetime import datetime

# константа, путь к файлу БД
FILE = "resources/db.sqlite"


class Ui_crontab(object):
    # класс окна планировщика задач
    def saver(self, name, givedData, taskContainer, taskLayout):
        # сохранение в БД новой записи
        try:
            dateSt, timeStr = givedData.split(' ')
            day, month, year = map(int, dateSt.split('.'))
            hour, minute, second = map(int, timeStr.split(':'))
            timestamp = datetime(year, month, day, hour, minute, second).timestamp()
            writer(FILE, "cron", ("name", "date"), (name, timestamp))
            self.update(taskContainer, taskLayout)
        except ValueError:
            # вызов ошибки формата данных
            errorBox = QMessageBox()
            errorBox.setIcon(QMessageBox.Icon.Critical)
            errorBox.setWindowIcon(QtGui.QIcon('icon.ico'))
            errorBox.setWindowTitle("Ошибка формата данных")
            errorBox.setText(f"Дата и время должны быть в формате \"DD.MM.YYYY HH:MM:SS\". "
                             f"Вы ввели: \"{givedData}\". Данные не были записаны в базу, вы можете ввести их заново")
            errorBox.setFont(self.font)
            errorBox.exec()

    def setupUi(self, crontab, mainFont):
        # верстка окна планировщика задач
        crontab.setObjectName("crontab")
        crontab.resize(1000, 600)
        crontab.setMinimumSize(QtCore.QSize(800, 600))
        crontab.setWindowIcon(QtGui.QIcon('icon.ico'))
        crontab.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0"
            "             rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));")
        # работа с размерами и фоновым цветом окна
        self.font = QtGui.QFont(mainFont, 10)
        self.bigFont = QtGui.QFont(mainFont, 14)
        self.gridLayout = QtWidgets.QGridLayout(crontab)
        self.gridLayout.setObjectName("gridLayout")
        self.taskName = QtWidgets.QLineEdit(crontab)
        self.taskName.setStyleSheet("""
            background-color:rgb(255, 166, 103);
            border: 0;
            margin: 0;
            border-radius: 3;
            color: black;
            padding: 3;
            border-style: solid;
            border-width: 1.5px;
            border-color: rgb(255, 133, 62);
        """)
        self.taskName.setObjectName("taskName")
        self.gridLayout.addWidget(self.taskName, 7, 0, 1, 1)
        # поле ввода назвыания новой задачи
        self.footerButtons = QtWidgets.QHBoxLayout()
        self.footerButtons.setObjectName("footerButtons")
        self.saveButton = QtWidgets.QPushButton(crontab)
        self.saveButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: black;
                padding-top: 2px;
                padding-bottom: 2px;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }
        """)
        self.saveButton.setObjectName("saveButton")
        self.footerButtons.addWidget(self.saveButton)
        self.gridLayout.addLayout(self.footerButtons, 9, 0, 1, 1)
        # кнопка сохранения задачи и лейаут нижних кнопок
        self.taskCreationInfoBox = QtWidgets.QHBoxLayout()
        self.taskCreationInfoBox.setObjectName("taskCreationInfoBox")
        self.newTaskLabel = QtWidgets.QLabel(crontab)
        self.newTaskLabel.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: black;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.newTaskLabel.setObjectName("newTaskLabel")
        self.taskCreationInfoBox.addWidget(self.newTaskLabel)
        # лейбл, обозначающий зону создания задачи
        self.taskDate = QtWidgets.QLineEdit(crontab)
        self.taskDate.setStyleSheet("""
            background-color:rgb(255, 166, 103);
            border: 0;
            margin: 0;
            border-radius: 3;
            color: black;
            padding: 3;
            border-style: solid;
            border-width: 1.5px;
            border-color: rgb(255, 133, 62);
        """)
        self.taskDate.setObjectName("taskDate")
        self.taskCreationInfoBox.addWidget(self.taskDate)
        self.gridLayout.addLayout(self.taskCreationInfoBox, 2, 0, 1, 1)
        # поле ввода даты новой задачи
        taskScroll = QtWidgets.QScrollArea(crontab)
        taskScroll.setWidgetResizable(True)
        taskContainer = QtWidgets.QWidget()
        taskLayout = QtWidgets.QVBoxLayout(taskContainer)
        taskScroll.setWidget(taskContainer)
        self.gridLayout.addWidget(taskScroll, 1, 0, 1, 1)
        taskContainer.setStyleSheet("""
            background-color:rgb(255, 166, 103);
            padding: 3;
        """)
        taskScroll.setStyleSheet("""
            QScrollArea {
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
            }
            QScrollBar:vertical {
                border: none;
                background: #FFA066;
                width: 12px;
                margin: 0;
                border-radius: 6px;
            }
    
            QScrollBar::handle:vertical {
                background: #FF8C42;
                min-height: 20px;
                border-radius: 6px;
                border: 2px solid #D66A2A;
            }
    
            QScrollBar::handle:vertical:hover {
                background: #FF7A2F;
            }
    
            QScrollBar::add-line:vertical, 
            QScrollBar::sub-line:vertical {
                background: #FFA066;
                height: 6px;
                subcontrol-origin: margin;
                subcontrol-position: top;
            }
    
            QScrollBar::add-page:vertical, 
            QScrollBar::sub-page:vertical {
                background: #FFA066;
            }
    
            QScrollBar:horizontal {
                border: none;
                background: #FFA066;
                height: 12px;
                margin: 0;
                border-radius: 6px;
            }
    
            QScrollBar::handle:horizontal {
                background: #FF8C42;
                min-width: 20px;
                border-radius: 6px;
                border: 1px solid #D66A2A;
            }
    
            QScrollBar::handle:horizontal:hover {
                background: #FF7A2F;
            }
    
            QScrollBar::add-line:horizontal, 
            QScrollBar::sub-line:horizontal {
                background: #FFA066;
                width: 6px;
                subcontrol-origin: margin;
                subcontrol-position: left;
            }
    
            QScrollBar::add-page:horizontal, 
            QScrollBar::sub-page:horizontal {
                background: #FFA066;
            }
        """)
        taskScroll.verticalScrollBar().setStyleSheet(taskScroll.styleSheet())
        taskScroll.horizontalScrollBar().setStyleSheet(taskScroll.styleSheet())
        # виджет и зона прокрутки пула задач
        self.cronLabel = QtWidgets.QLabel(crontab)
        self.cronLabel.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: black;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.cronLabel.setObjectName("cronLabel")
        self.gridLayout.addWidget(self.cronLabel, 0, 0, 1, 1)
        # лейбл названия окна
        self.saveButton.clicked.connect(lambda: self.saver(self.taskName.text(), self.taskDate.text(),
                                                           taskContainer, taskLayout))
        self.retranslateUi(crontab)
        QtCore.QMetaObject.connectSlotsByName(crontab)
        self.update(taskContainer, taskLayout)
        self.cronLabel.setFont(self.bigFont)
        self.newTaskLabel.setFont(self.bigFont)
        self.taskName.setFont(self.font)
        self.taskDate.setFont(self.font)
        self.saveButton.setFont(self.bigFont)
        # подключение шрифтов и функции, задающий текст элементам

    def retranslateUi(self, crontab):
        # функция, задающая текст элементам
        _translate = QtCore.QCoreApplication.translate
        crontab.setWindowTitle(_translate("crontab", "SCHelper — Планировщик задач"))
        self.taskName.setPlaceholderText(_translate("crontab", "Название"))
        self.saveButton.setText(_translate("crontab", "Сохранить"))
        self.newTaskLabel.setText(_translate("crontab", "Создать новую задачу"))
        self.taskDate.setPlaceholderText(_translate("crontab", "Дата и время в"
                                                               " формате \"DD.MM.YYYY HH:MM:SS\""))
        self.cronLabel.setText(_translate("crontab", "Планировщик задач"))

    def delAndUpdate(self, num, taskContainer, taskLayout):
        # функция, которая удаляет элмент, после этого идет обновление пула задач
        delete(FILE, "cron", num)
        for task in taskContainer.findChildren(QGroupBox):
            task.deleteLater()
        self.update(taskContainer, taskLayout)

    def update(self, taskContainer, taskLayout):
        # обновление пула задач
        tasksDATA = read(FILE, "cron", "*")
        tasksDATA.sort(key=lambda x: x[1])
        tasksDATA.sort(key=lambda x: x[2])
        for task in taskContainer.findChildren(QGroupBox):
            task.deleteLater()
        # удаление старых задач и сортировка новых
        for num, name, date in tasksDATA:
            # создание отдельного элемента для каждой задачи
            setattr(self, f"task{num}", QtWidgets.QGroupBox(taskContainer))
            getattr(self, f"task{num}").setStyleSheet("""
                    background-color:rgb(255, 166, 103);
                    padding: 3;
                    border-style: solid;
                    border-width: 1.5px;
                    border-color: rgb(255, 133, 62);
                    color: black;
            """)
            getattr(self, f"task{num}").setMaximumSize(16777215, 100)
            taskLayout.addWidget(getattr(self, f"task{num}"))
            setattr(self, f"gridLayoutTask{num}", QtWidgets.QGridLayout(getattr(self, f"task{num}")))
            getattr(self, f"gridLayoutTask{num}").setObjectName(f"gridLayout{num}")
            setattr(self, f"taskDeleteButton{num}", QtWidgets.QPushButton(getattr(self, f"task{num}")))
            getattr(self, f"taskDeleteButton{num}").setMaximumSize(QtCore.QSize(70, 72))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/DELETE_ICON.svg"))
            getattr(self, f"taskDeleteButton{num}").setIcon(icon)
            getattr(self, f"taskDeleteButton{num}").setIconSize(QtCore.QSize(70, 70))
            (getattr(self, f"taskDeleteButton{num}").clicked.connect
             (lambda _, n=num: self.delAndUpdate(n, taskContainer, taskLayout)))
            getattr(self, f"gridLayoutTask{num}").addWidget(getattr(self, f"taskDeleteButton{num}"), 1, 2, 2, 1)
            taskName = QtWidgets.QLabel(getattr(self, f"task{num}"))
            taskName.setText(name)
            getattr(self, f"gridLayoutTask{num}").addWidget(taskName, 1, 0, 1, 1)
            taskDate = QtWidgets.QLabel(getattr(self, f"task{num}"))
            dateConverted = datetime.fromtimestamp(date)
            printDate = (f"{dateConverted.day}.{dateConverted.month}.{dateConverted.year} "
                         f"{dateConverted.hour}:{dateConverted.minute}:{dateConverted.second}")
            taskDate.setText(printDate)
            getattr(self, f"gridLayoutTask{num}").addWidget(taskDate, 2, 0, 1, 1)
            taskDate.setFont(self.font)
            taskName.setFont(self.font)
