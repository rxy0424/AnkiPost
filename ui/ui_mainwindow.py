# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.word_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.word_lineEdit.setObjectName("word_lineEdit")
        self.horizontalLayout_2.addWidget(self.word_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.sentence_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.sentence_textEdit.setObjectName("sentence_textEdit")
        self.horizontalLayout.addWidget(self.sentence_textEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.textBrowser_meaning = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_meaning.setObjectName("textBrowser_meaning")
        self.verticalLayout_2.addWidget(self.textBrowser_meaning)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 23))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.aboutMenu = QtWidgets.QMenu(self.menubar)
        self.aboutMenu.setObjectName("aboutMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.settingAction = QtWidgets.QAction(MainWindow)
        self.settingAction.setObjectName("settingAction")
        self.aboutQtAction = QtWidgets.QAction(MainWindow)
        self.aboutQtAction.setObjectName("aboutQtAction")
        self.fileMenu.addAction(self.settingAction)
        self.aboutMenu.addAction(self.aboutQtAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.aboutMenu.menuAction())
        self.label.setBuddy(self.word_lineEdit)
        self.label_2.setBuddy(self.sentence_textEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "单词"))
        self.label_2.setText(_translate("MainWindow", "句子"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.fileMenu.setTitle(_translate("MainWindow", "文件"))
        self.aboutMenu.setTitle(_translate("MainWindow", "关于"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.settingAction.setText(_translate("MainWindow", "设置"))
        self.aboutQtAction.setText(_translate("MainWindow", "关于Qt"))
