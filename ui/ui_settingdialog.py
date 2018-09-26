# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingdialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(255, 145)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settingsDialog.sizePolicy().hasHeightForWidth())
        settingsDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(settingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(settingsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.infoSourceComboBox = QtWidgets.QComboBox(settingsDialog)
        self.infoSourceComboBox.setObjectName("infoSourceComboBox")
        self.gridLayout.addWidget(self.infoSourceComboBox, 0, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(settingsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(settingsDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.modelLineEdit = QtWidgets.QLineEdit(settingsDialog)
        self.modelLineEdit.setObjectName("modelLineEdit")
        self.gridLayout.addWidget(self.modelLineEdit, 3, 2, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(settingsDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.ankiControlcomboBox = QtWidgets.QComboBox(settingsDialog)
        self.ankiControlcomboBox.setObjectName("ankiControlcomboBox")
        self.gridLayout.addWidget(self.ankiControlcomboBox, 1, 2, 1, 2)
        self.deckLineEdit = QtWidgets.QLineEdit(settingsDialog)
        self.deckLineEdit.setObjectName("deckLineEdit")
        self.gridLayout.addWidget(self.deckLineEdit, 2, 2, 1, 2)
        self.label.setBuddy(self.infoSourceComboBox)
        self.label_2.setBuddy(self.ankiControlcomboBox)

        self.retranslateUi(settingsDialog)
        self.buttonBox.accepted.connect(settingsDialog.accept)
        self.buttonBox.rejected.connect(settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Dialog"))
        self.label.setText(_translate("settingsDialog", "查词源"))
        self.label_3.setText(_translate("settingsDialog", "deck"))
        self.label_4.setText(_translate("settingsDialog", "model"))
        self.label_2.setText(_translate("settingsDialog", "Anki交互"))

