# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from resources.jsonWorker import read, writeAdd, elementDeletion
FILE = 'resources/tasks.json'
tasksDATA = read(FILE)


def blockCreation(parent, index, taskData):
        
    taskGroup = QtWidgets.QGroupBox(parent)
    taskGroup.setStyleSheet("""
        background-color:rgb(255, 166, 103);
        padding: 3;
        border-style: solid;
        border-width: 1.5px;
        border-color: rgb(255, 133, 62);
        font-size: 13px;
        color: black;
    """)
    taskGroup.setMaximumSize(QtCore.QSize(16777215, 100))
    taskGroup.setTitle("")
    taskGroup.setObjectName(f"task{index}")
    gridLayout = QtWidgets.QGridLayout(taskGroup)
    gridLayout.setObjectName(f"gridLayout{index}")
    taskDelete = QtWidgets.QPushButton(taskGroup)
    taskDelete.setMaximumSize(QtCore.QSize(70, 72))
    font = QtGui.QFont()
    taskDelete.setFont(font)
    taskDelete.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("resources/DELETE_ICON.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    taskDelete.setIcon(icon)
    taskDelete.setIconSize(QtCore.QSize(70, 70))
    taskDelete.setObjectName(f"taskDelete{index}")
    taskDelete.clicked.connect(lambda: Ui_crontab.delete(taskGroup, index))
    gridLayout.addWidget(taskDelete, 1, 2, 2, 1)
    taskName = QtWidgets.QLabel(taskGroup)
    taskName.setObjectName(f"taskName{index}")
    taskName.setText(taskData['name'])
    gridLayout.addWidget(taskName, 1, 0, 1, 1)
    taskDate = QtWidgets.QLabel(taskGroup)
    taskDate.setObjectName(f"taskDate{index}")
    taskDate.setText(taskData['date'])
    gridLayout.addWidget(taskDate, 2, 0, 1, 1)
    return taskGroup, taskDelete


class Ui_crontab(object):
    def setupUi(self, crontab):
        crontab.setObjectName("crontab")
        crontab.resize(915, 499)
        crontab.setMinimumSize(QtCore.QSize(640, 480))
        crontab.setWindowIcon(QtGui.QIcon('icon.ico'))
        crontab.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0             rgba(255, 117, 83, 255), stop:1 rgba(255, 255, 255, 255));")
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
            font-size: 13px;
        """)
        self.taskName.setObjectName("taskName")
        self.gridLayout.addWidget(self.taskName, 7, 0, 1, 1)
        self.footerButtons = QtWidgets.QHBoxLayout()
        self.footerButtons.setObjectName("footerButtons")
        self.saveButton = QtWidgets.QPushButton(crontab)
        self.saveButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 133, 62);
                border: 0;
                margin: 0;
                border-radius: 5;
                color: white;
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
        self.taskCreationInfoBox = QtWidgets.QHBoxLayout()
        self.taskCreationInfoBox.setObjectName("taskCreationInfoBox")
        self.newTaskLabel = QtWidgets.QLabel(crontab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newTaskLabel.setFont(font)
        self.newTaskLabel.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: white;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.newTaskLabel.setObjectName("newTaskLabel")
        self.taskCreationInfoBox.addWidget(self.newTaskLabel)
        self.taskDate = QtWidgets.QLineEdit(crontab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskDate.sizePolicy().hasHeightForWidth())
        self.taskDate.setSizePolicy(sizePolicy)
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
            font-size: 13px;
        """)
        self.taskDate.setObjectName("taskDate")
        self.taskCreationInfoBox.addWidget(self.taskDate)
        self.gridLayout.addLayout(self.taskCreationInfoBox, 2, 0, 1, 1)
        taskScroll = QtWidgets.QScrollArea(crontab)
        taskScroll.setWidgetResizable(True)
        taskContainer = QtWidgets.QWidget()
        taskLayout = QtWidgets.QVBoxLayout(taskContainer)
        taskScroll.setWidget(taskContainer)
        self.gridLayout.addWidget(taskScroll, 1, 0, 1, 1)
        taskContainer.setStyleSheet("""
            background-color:rgb(255, 166, 103);
            padding: 3;
            font-size: 13px;
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
        for i, taskData in enumerate(tasksDATA, start=1):
            taskBlock, deleteButton = blockCreation(taskContainer, i, taskData)
            taskLayout.addWidget(taskBlock)
            deleteButton.clicked.connect(lambda: self.update(taskContainer, taskLayout))
        self.cronLabel = QtWidgets.QLabel(crontab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cronLabel.setFont(font)
        self.cronLabel.setStyleSheet("""
            background-color: rgb(255, 133, 62);
            border: 0;
            margin: 0;
            border-radius: 5;
            color: white;
            padding-left: 5px;
            padding-top: 2px;
            padding-bottom: 2px;
        """)
        self.cronLabel.setObjectName("cronLabel")
        self.gridLayout.addWidget(self.cronLabel, 0, 0, 1, 1)
        self.saveButton.clicked.connect(lambda: writeAdd(FILE, {"name": self.taskName.text(), "date": self.taskDate.text()}))
        self.saveButton.clicked.connect(lambda: self.update(taskContainer, taskLayout))
        self.retranslateUi(crontab)
        QtCore.QMetaObject.connectSlotsByName(crontab)


    def retranslateUi(self, crontab):
        _translate = QtCore.QCoreApplication.translate
        crontab.setWindowTitle(_translate("crontab", "SCHelper — Планировщик задач"))
        self.taskName.setPlaceholderText(_translate("crontab", "Название"))
        self.saveButton.setText(_translate("crontab", "Сохранить"))
        self.newTaskLabel.setText(_translate("crontab", "Создать новую задачу"))
        self.taskDate.setPlaceholderText(_translate("crontab", "Дата"))
        self.cronLabel.setText(_translate("crontab", "Планировщик задач"))


    def update(self, taskContainer, taskLayout):
        tasksDATA = read(FILE)
        while taskLayout.count():
            item = taskLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        for i, taskData in enumerate(tasksDATA, start=1):
            taskBlock, deleteButton = blockCreation(taskContainer, i, taskData)
            taskLayout.addWidget(taskBlock)
            deleteButton.clicked.connect(lambda: self.update(taskContainer, taskLayout))


    def delete(taskGroup, index):
        elementDeletion(FILE, index)
        taskGroup.setParent(None)
        taskGroup.deleteLater()