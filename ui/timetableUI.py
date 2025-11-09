# -*- coding: utf-8 -*-
# импорт библиотек
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

# константы с путем к файлу, стилем и названиями столбцов таблицы
FILE = "resources/db.sqlite"
LABELS = ['№', 'Название урока', 'Время начала',
          'Время окончания', 'Место проведения', 'Ф.И.О Преподавателя']
LABELSENG = {'№': 'lessonNum', 'Название урока': 'lessonName', 'Время начала': 'lessonStarts',
             'Время окончания': 'lessonEnds', 'Место проведения': 'place', 'Ф.И.О Преподавателя': 'teacher'}
BUTTONSTYLESHEET = """
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: black;
                height: 37px;
            }
            QPushButton:hover {
                background-color:rgb(244, 81, 0);
            }
"""


class Ui_timetable(QtWidgets.QWidget):
    # класс окна расписания
    def setupUi(self, timetable, mainFont):
        # верстка окна распиания
        timetable.setObjectName("timetable")
        timetable.resize(1000, 600)
        timetable.setMinimumSize(QtCore.QSize(800, 600))
        timetable.setWindowIcon(QtGui.QIcon('icon.ico'))
        timetable.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,"
                                " stop:0 rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));")
        self.font = QtGui.QFont(mainFont, 10)
        self.bigFont = QtGui.QFont(mainFont, 14)
        self.verticalLayout = QtWidgets.QVBoxLayout(timetable)
        self.verticalLayout.setObjectName("verticalLayout")
        # работа со шрифтом, размерами и фоновым цветом окна
        self.timetableTitle = QtWidgets.QLabel(self)
        self.timetableTitle.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: black;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.timetableTitle.setObjectName("timetableTitle")
        self.verticalLayout.addWidget(self.timetableTitle)
        # название окна
        self.dayChoose = QtWidgets.QComboBox(self)
        self.dayChoose.setStyleSheet("""
            QComboBox, 
            QComboBox::drop-down, 
            QAbstractItemView{
                background-color:rgb(255, 166, 103);
                border: 0;
                margin: 0;
                border-radius: 3;
                color: black;
                padding: 3;
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
                
            }
            QComboBox:hover, 
            QComboBox::drop-down:hover, 
            QComboBox::drop-down:hover{
                background-color: rgb(244, 81, 0);
            }
            QComboBox::down-arrow {
                image: url(resources/plus.svg);
                width: 12px;
                height: 12px;
            }
        """)
        self.dayChoose.setObjectName("dayChoose")
        self.dayChoose.addItem("")
        self.dayChoose.addItem("")
        self.dayChoose.addItem("")
        self.dayChoose.addItem("")
        self.dayChoose.addItem("")
        self.dayChoose.addItem("")
        self.dayChoose.addItem("")
        self.verticalLayout.addWidget(self.dayChoose)
        # добавление пустых элементов и работа с выпадающим списком выбора дня
        self.timetableView = QtWidgets.QTableWidget(self)
        self.timetableView.setStyleSheet("""
            QTableWidget,
            QHeaderView::section,
            QTableCornerButton::section, QWidget{
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
                background-color:rgb(255, 166, 103);
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
        self.timetableView.setObjectName("timetableView")
        self.verticalLayout.addWidget(self.timetableView)
        # таблица просмотра расписания
        self.newLineButton = QtWidgets.QPushButton(self)
        self.newLineButton.setStyleSheet(BUTTONSTYLESHEET)
        self.newLineButton.setObjectName("newLineButton")
        self.verticalLayout.addWidget(self.newLineButton)
        # кнопка создания пустой строки
        self.deleteLayout = QtWidgets.QHBoxLayout()
        self.deleteLayout.setObjectName("deleteLayout")
        # создание лейаута для кнопки и индекса удаления строки
        self.deleteIndex = QtWidgets.QSpinBox(self)
        self.deleteIndex.setValue(1)
        self.deleteIndex.setMinimum(1)
        self.deleteIndex.setStyleSheet("""
            QSpinBox,
            QSpinBox::down-button,
            QSpinBox::up-button {
                background-color:rgb(255, 166, 103);
                border-radius: 3;
                color: black;
                border-style: solid;
                border-width: 1.5px;
                border-color: rgb(255, 133, 62);
            }
            QSpinBox {
                padding-right: 20px; 
                height: 30px;
            }
            QSpinBox::up-button {
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 15px;
                height: 15px;
            }
            QSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                width: 15px;
                height: 15px;
            }
            QSpinBox::up-arrow {
                image: url(resources/plus.svg);
                width: 15px;
                height: 15px;
            }
            QSpinBox::down-arrow {
                image: url(resources/minus.svg);
                width: 15px;
                height: 15px;
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background-color: rgb(244, 81, 0);
            }
        """)
        self.deleteIndex.setObjectName("deleteIndex")
        self.deleteLayout.addWidget(self.deleteIndex)
        # поле для ввода индекса удаления строки
        self.deleteButton = QtWidgets.QPushButton(self)
        self.deleteButton.setStyleSheet(BUTTONSTYLESHEET)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteLayout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(lambda: self.deleteLine(self.deleteIndex.value()))
        self.verticalLayout.addLayout(self.deleteLayout)
        # кнопка удаления строки
        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setStyleSheet(BUTTONSTYLESHEET)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        # кнопка сохранения изменений
        self.retranslateUi(timetable)
        QtCore.QMetaObject.connectSlotsByName(timetable)
        self.con = sqlite3.connect(FILE)
        self.removeEmpty()
        self.modified = {}
        self.dayChoose.currentTextChanged.connect(self.update)
        self.timetableView.itemChanged.connect(self.boxChanged)
        self.saveButton.clicked.connect(self.saver)
        self.newLineButton.clicked.connect(self.newLine)
        self.timetableTitle.setFont(self.bigFont)
        self.saveButton.setFont(self.bigFont)
        self.deleteButton.setFont(self.bigFont)
        self.newLineButton.setFont(self.bigFont)
        self.dayChoose.setFont(self.font)
        self.update()
        # вызов функции установки текста на объекты, создание подключения к БД,
        # установка шрифтов и вызов загрузки данных из БД

    def removeEmpty(self):
        # функция удаления пустых строк при загрузке окна
        cur = self.con.cursor()
        cur.execute("DELETE FROM timetable WHERE lessonNum = '' "
                    "AND lessonName = '' AND lessonStarts = '' "
                    "AND lessonEnds = '' AND place = '' AND teacher = ''").fetchall()
        self.con.commit()
        self.update()

    def update(self):
        # функция загрузки данных из БД и установки их в таблицу
        cur = self.con.cursor()
        currentDay = self.dayChoose.currentIndex()
        result = cur.execute(f"SELECT lessonNum, lessonName, lessonStarts, lessonEnds, place, teacher FROM"
                             f" timetable WHERE weekDay = {currentDay}").fetchall()
        self.timetableView.setRowCount(len(result))
        self.deleteIndex.setMaximum(len(result))
        if len(result) != 0:
            self.timetableView.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.timetableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        self.modified = {}
        # расстановка данных и отчистка буфера обновлений
        self.timetableView.setHorizontalHeaderLabels(LABELS)
        self.timetableView.setColumnWidth(0, 20)
        self.timetableView.setColumnWidth(1, 145)
        self.timetableView.setColumnWidth(2, 145)
        self.timetableView.setColumnWidth(3, 145)
        self.timetableView.setColumnWidth(4, 145)
        self.timetableView.setColumnWidth(5, 145)
        self.timetableView.setFont(self.font)
        # установка ширины, названия колонок и шрифта таблицы

    def boxChanged(self, item):
        # функция записи координат и нового текста измененного объекта
        self.modified[(item.column(), item.row())] = item.text()

    def printError(self, errorText):
        # функция печати ошибки формата данных
        errorBox = QtWidgets.QMessageBox()
        errorBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        errorBox.setWindowIcon(QtGui.QIcon('icon.ico'))
        errorBox.setWindowTitle("Ошибка формата данных")
        errorBox.setText(errorText)
        errorBox.setFont(self.font)
        errorBox.exec()

    def checker(self, type, data):
        # функция проверки формата данных
        if type == "lessonNum":
            values = []
            columnIndex = 0
            for row in range(self.timetableView.rowCount()):
                item = self.timetableView.item(row, columnIndex)
                if item is not None:
                    values.append(item.text())
            indexes = {}
            for i in values:
                if i == '':
                    continue
                if i not in indexes.keys():
                    indexes[i] = 1
                else:
                    indexes[i] += 1
            if max(list(indexes.values())) > 1:
                errorText = (f"В расписании не может существовать 2 урока, с одинаковым номером ({data})."
                             f" Данные не были записаны в базу, вы можете ввести их заново")
                self.printError(errorText)
                return False
        elif type == "lessonStarts" or type == "lessonEnds":
            errorText = (f"Время должно быть в формате \"HH:MM\". "
                         f"Вы ввели: \"{data}\". Данные не были записаны в базу, вы можете ввести их заново")
            parts = data.split(":")
            if len(parts) != 2:
                self.printError(errorText)
                return False
            hh, mm = parts
            if not (hh.isdigit() and mm.isdigit()):
                self.printError(errorText)
                return False
            hh, mm = int(hh), int(mm)
            if 0 <= hh <= 23 and 0 <= mm <= 59:
                pass
            else:
                errorText = (f"Часы должны быть в интервале 0 <= HH <= 23, а минуты - 0 <= MM <= 59 "
                             f"Вы ввели: \"{data}\". Данные не были записаны в базу, вы можете ввести их заново")
                self.printError(errorText)
                return False
        return True

    def saver(self):
        # функция записи успешно проверенных данных в бд
        if self.modified:
            cur = self.con.cursor()
            for key, value in self.modified.items():
                row = LABELSENG[LABELS[key[0]]]
                col = key[1]
                if self.checker(row, value):
                    que = f"""
                            UPDATE 
                                timetable
                            SET 
                                {row} = "{value}"
                            WHERE 
                                id = (
                                    SELECT id
                                    FROM timetable
                                    WHERE weekday = {self.dayChoose.currentIndex()}
                                    ORDER BY id
                                    LIMIT 1 OFFSET {col}
                                )
                            """
                    cur.execute(que).fetchall()
                    self.con.commit()
            self.update()

    def newLine(self):
        # функция создания новой пустой строки
        cur = self.con.cursor()
        cur.execute("INSERT INTO timetable (lessonNum, weekDay, "
                    "lessonName, lessonStarts, lessonEnds,"
                    f" place, teacher) VALUES ('', {self.dayChoose.currentIndex()}, '', '', '', '', '')").fetchall()
        self.con.commit()
        self.update()

    def deleteLine(self, num):
        # функция удаления нужной строки
        cur = self.con.cursor()
        cur.execute(f"""
            DELETE FROM timetable
            WHERE id = (
                SELECT id
                FROM timetable
                WHERE weekday = {self.dayChoose.currentIndex()}
                ORDER BY id
                LIMIT 1 OFFSET {num - 1}
            )
        """).fetchall()
        self.con.commit()
        self.update()

    def retranslateUi(self, timetable):
        # функция установки текста на объекты
        _translate = QtCore.QCoreApplication.translate
        timetable.setWindowTitle(_translate("timetable", "SCHelper — Расписание"))
        self.timetableTitle.setText(_translate("timetable", "Расписание"))
        self.dayChoose.setItemText(0, _translate("timetable", "Понедельник"))
        self.dayChoose.setItemText(1, _translate("timetable", "Вторник"))
        self.dayChoose.setItemText(2, _translate("timetable", "Среда"))
        self.dayChoose.setItemText(3, _translate("timetable", "Четверг"))
        self.dayChoose.setItemText(4, _translate("timetable", "Пятница"))
        self.dayChoose.setItemText(5, _translate("timetable", "Суббота"))
        self.dayChoose.setItemText(6, _translate("timetable", "Воскресенье"))
        self.newLineButton.setText(_translate("timetable", "Новая строка"))
        self.deleteButton.setText(_translate("timetable", "Удалить строку"))
        self.saveButton.setText(_translate("timetable", "Сохранить изменения"))
