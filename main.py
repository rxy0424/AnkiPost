from infosource.infosource import InfoSource
from ankicontrol.ankicontrol import AbstractAnkiControl
import infosource.infosource
import ankicontrol.ankicontrol

from ui import ui_mainwindow
from settingdialog import SettingDialog

from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSettings

import sys
import inspect
import time


class WordInfoThread(QThread):
    getWord = pyqtSignal(dict)

    def __init__(self, info_source: InfoSource, parent=None):
        super(WordInfoThread, self).__init__()
        self.sentence = ''
        self.word = ''
        self.infoSource = info_source

    def run(self):
        word_info = self.get_word_meaning(self.sentence, self.word)
        self.getWord.emit(word_info)

    def get_word_meaning(self, sentence: str, word: str):
        return self.infoSource.get_word_info(sentence, word)


class MainWindow(QMainWindow):
    def __init__(self, clip):
        super().__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.clipboard = clip
        self.clipboard.dataChanged.connect(self.clipboard_changed)

        self.controls = {control.name: control
                         for (name, control) in inspect.getmembers(ankicontrol.ankicontrol)
                         if inspect.isclass(control) and control.name != "Abstract"}
        self.sources = {source.name: source
                        for (name, source) in inspect.getmembers(infosource.infosource)
                        if inspect.isclass(source) and source.name != "Abstract"}

        self.config = QSettings("config.ini", QSettings.IniFormat)

        if not self.config.contains("control_name"):
            self.config.setValue("control_name", "Local")
        if not self.config.contains("deck_name"):
            self.config.setValue("deck_name", "paper::paperWords")
        if not self.config.contains("model_name"):
            self.config.setValue("model_name", "Facebook")
        if not self.config.contains("source_name"):
            self.config.setValue("source_name", "Shanbay")

        control_name = self.config.value("control_name", "Local")
        deck_name = self.config.value("deck_name", "paper::paperWords")
        model_name = self.config.value("model_name", "Facebook")
        source_name = self.config.value("source_name", "Shanbay")
        self.updateStatusBar()

        self.ankicontrol = self.controls[control_name](deck_name=deck_name, model_name=model_name)

        self.wordInfoThread = WordInfoThread(info_source=self.sources[source_name]())
        self.wordInfoThread.getWord.connect(self.has_get_word_info)

        self.settingDialog = SettingDialog(self)
        self.settingDialog.set_config(self.sources.keys(), self.controls.keys())

        self.ui.settingAction.triggered.connect(self.setting_windows_handle)
        self.ui.aboutQtAction.triggered.connect(QApplication.aboutQt)


    @pyqtSlot()
    def setting_windows_handle(self):
        if self.settingDialog.exec():
            self.settingUpdateCheck("deck_name", self.settingDialog.ui.deckLineEdit.text())
            self.settingUpdateCheck("model_name", self.settingDialog.ui.modelLineEdit.text())
            self.settingUpdateCheck("source_name", self.settingDialog.ui.infoSourceComboBox.currentText())
            self.settingUpdateCheck("control_name", self.settingDialog.ui.ankiControlcomboBox.currentText())

            control_name = self.config.value("control_name")
            deck_name = self.config.value("deck_name")
            model_name = self.config.value("model_name")
            source_name = self.config.value("source_name")
            self.ankicontrol = self.controls[control_name](deck_name=deck_name, model_name=model_name)
            self.wordInfoThread.info_source=self.sources[source_name]()
            self.updateStatusBar()
        else:
            return

    def settingUpdateCheck(self, setting_name: str, dialog_value: str):
        if self.config.value(setting_name) != dialog_value:
            self.config.setValue(setting_name, dialog_value)

    def updateStatusBar(self):
        control_name = self.config.value("control_name")
        deck_name = self.config.value("deck_name")
        model_name = self.config.value("model_name")
        source_name = self.config.value("source_name")
        self.ui.statusbar.showMessage("Ctrl:{}\tSource:{}\ndeck:{}\tmodel:{}".format(control_name, source_name, deck_name, model_name))


    def add_deck(self, word_info: dict):
        self.ankicontrol.add_deck(word_info)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        word = self.ui.word_lineEdit.text()
        sentence = self.ui.sentence_textEdit.toPlainText()
        if word != '' and sentence != '':
            self.begin_get_word_info(sentence, word)

    def begin_get_word_info(self, sentence: str, word: str):
        self.ui.sentence_textEdit.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui.word_lineEdit.setDisabled(True)
        self.wordInfoThread.sentence = sentence
        self.wordInfoThread.word = word
        self.wordInfoThread.start()

    @pyqtSlot(dict)
    def has_get_word_info(self, word_info: dict):
        if len(word_info) > 0:
            self.add_deck(word_info)
            self.ui.textBrowser_meaning.setText(word_info['glossary'])
        else:
            self.ui.textBrowser_meaning.setText("no word")
        self.ui.sentence_textEdit.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.word_lineEdit.setEnabled(True)

    @pyqtSlot()
    def on_sentence_textEdit_textChanged(self):
        self.ui.word_lineEdit.setText('')
        self.ui.textBrowser_meaning.setText("")

    @pyqtSlot()
    def on_sentence_textEdit_selectionChanged(self):
        word = self.ui.sentence_textEdit.textCursor().selectedText()
        if word != "" :
            print(word)
            self.ui.word_lineEdit.setText(word)
            self.ui.textBrowser_meaning.setText("")

    @pyqtSlot()
    def clipboard_changed(self):
        time.sleep(1)
        self.ui.sentence_textEdit.setPlainText(self.clipboard.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app.clipboard())
    mainWindow.show()
    sys.exit(app.exec_())
