import mainwindow
from infosource import InfoSource, InfoSourceShanbay
from ankicontrol import AbstractAnkiControl, AnkiControlLocal

import sys

from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal


class WordInfoThread(QThread):
    getWord = pyqtSignal(dict)

    def __init__(self, infoSource: InfoSource, parent=None):
        super(WordInfoThread, self).__init__()
        self.sentence = ''
        self.word = ''
        self.infoSource = infoSource

    def run(self):
        word_info = self.get_word_meaning(self.sentence, self.word)
        self.getWord.emit(word_info)

    def get_word_meaning(self, sentence: str, word: str):
        return self.infoSource.get_word_info(sentence, word)


class MainWindow(QWidget):
    def __init__(self, clip):
        super().__init__()
        self.ui = mainwindow.Ui_Form()
        self.ui.setupUi(self)
        self.clipboard = clip
        self.clipboard.dataChanged.connect(self.clipboard_changed)

        self.wordInfoThread = WordInfoThread(infoSource=InfoSourceShanbay())
        self.wordInfoThread.getWord.connect(self.has_get_word_info)

        self.ankicontrol = AnkiControlLocal(deck_name="paper::paperWords", model_name="Facebook")

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
        self.ui.sentence_textEdit.setPlainText(self.clipboard.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app.clipboard())
    mainWindow.show()
    sys.exit(app.exec_())
