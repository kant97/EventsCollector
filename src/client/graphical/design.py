# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trello-GC.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 649)
        MainWindow.setMaximumSize(QtCore.QSize(827, 649))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Synchronize = QtWidgets.QWidget()
        self.Synchronize.setObjectName("Synchronize")
        self.widget = QtWidgets.QWidget(self.Synchronize)
        self.widget.setGeometry(QtCore.QRect(10, 20, 781, 521))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.AddButton = QtWidgets.QPushButton(self.widget)
        self.AddButton.setObjectName("AddButton")
        self.verticalLayout_11.addWidget(self.AddButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.HandRadio = QtWidgets.QRadioButton(self.widget)
        self.HandRadio.setObjectName("HandRadio")
        self.verticalLayout_3.addWidget(self.HandRadio)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.SyncButton = QtWidgets.QPushButton(self.widget)
        self.SyncButton.setObjectName("SyncButton")
        self.verticalLayout_3.addWidget(self.SyncButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AutioRadio = QtWidgets.QRadioButton(self.widget)
        self.AutioRadio.setObjectName("AutioRadio")
        self.verticalLayout_5.addWidget(self.AutioRadio)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.fstTime = QtWidgets.QRadioButton(self.widget)
        self.fstTime.setObjectName("fstTime")
        self.verticalLayout_4.addWidget(self.fstTime)
        self.sndTime = QtWidgets.QRadioButton(self.widget)
        self.sndTime.setObjectName("sndTime")
        self.verticalLayout_4.addWidget(self.sndTime)
        self.trdTime = QtWidgets.QRadioButton(self.widget)
        self.trdTime.setObjectName("trdTime")
        self.verticalLayout_4.addWidget(self.trdTime)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frtTime = QtWidgets.QRadioButton(self.widget)
        self.frtTime.setMaximumSize(QtCore.QSize(17, 16777215))
        self.frtTime.setText("")
        self.frtTime.setObjectName("frtTime")
        self.horizontalLayout_2.addWidget(self.frtTime)
        self.Timer = QtWidgets.QTimeEdit(self.widget)
        self.Timer.setObjectName("Timer")
        self.horizontalLayout_2.addWidget(self.Timer)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.Synchronize, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.widget1 = QtWidgets.QWidget(self.Settings)
        self.widget1.setGeometry(QtCore.QRect(50, 17, 731, 551))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_8.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_8.addWidget(self.checkBox_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_9.addWidget(self.lineEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.SettingsButton = QtWidgets.QPushButton(self.widget1)
        self.SettingsButton.setObjectName("SettingsButton")
        self.horizontalLayout_5.addWidget(self.SettingsButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.Settings, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Events Synchronizer"))
        self.AddButton.setText(_translate("MainWindow", "Добавить запись"))
        self.HandRadio.setText(_translate("MainWindow", "Ручная синхронизация"))
        self.SyncButton.setText(_translate("MainWindow", "Синхронизировать"))
        self.AutioRadio.setText(_translate("MainWindow", "Автономная работа"))
        self.label_2.setText(_translate("MainWindow", "Обновлять каждые:"))
        self.fstTime.setText(_translate("MainWindow", "5 секунд"))
        self.sndTime.setText(_translate("MainWindow", "30 секунд"))
        self.trdTime.setText(_translate("MainWindow", "5 минут"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Synchronize), _translate("MainWindow", "Синхронизация"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.SettingsButton.setText(_translate("MainWindow", "Save Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Настройки"))

