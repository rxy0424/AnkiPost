import mainwindow

import sys

from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

import requests


class WordInfoFromInternet(QThread):
    getWord = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(WordInfoFromInternet, self).__init__()
        self.sentence = ''
        self.word = ''

    def run(self):
        word_info = self.get_word_meaning(self.sentence, self.word)
        self.getWord.emit(word_info)
        #self.getWord.emit("abc")

    def get_word_meaning(self, sentence, word):
        word_info = {}
        dict_usr = 'https://api.shanbay.com/bdc/search/?word='+word
        try:
            r = requests.get(dict_usr, timeout=5)
        except:
            return word_info


        r_json = r.json()
        if r_json['status_code'] == 1:
            print("no word find")
            #self.ui.textBrowser_meaning.setText("no word find")
        else:
            word_info['content'] = r_json['data']['content']
            word_info['definition'] = r_json['data']['definition'].replace("\n", "<br>")
            word_info['pronunciation'] = r_json['data']['pronunciation']
            word_info['sentence'] = sentence.replace("\n", " ").replace(word, "<b>" + word + "</b>").replace("- ", "")
            #self.ui.textBrowser_meaning.setText(r_json['data']['definition'])
        return word_info


class MainWindow(QWidget):
    def __init__(self, clip):
        super().__init__()
        self.ui = mainwindow.Ui_Form()
        self.ui.setupUi(self)
        self.clipboard = clip
        self.clipboard.dataChanged.connect(self.clipboard_changed)

        self.wordInfoFromInternet = WordInfoFromInternet()
        self.wordInfoFromInternet.getWord.connect(self.has_get_word_info)

    def add_deck(self, word_info):
        m_data = {
            'action': 'addNote', 'params': {
                'note': {
                    'fields': {
                        'expression': word_info['content'],
                        'glossary': word_info['definition'],
                        'sentence': word_info['sentence'],
                        'reading': word_info['pronunciation']
                    },
                    'tags': {},
                    'deckName': 'paper::paperWords',
                    'modelName': 'Facebook'
                }
            }
        }
        r = requests.post('http://127.0.0.1:8765', json=m_data)
        r.status_code

    @pyqtSlot()
    def on_pushButton_clicked(self):
        word = self.ui.word_lineEdit.text()
        sentence = self.ui.sentence_textEdit.toPlainText()
        if word != '' and sentence != '':
            self.begin_get_word_info(sentence, word)

    def begin_get_word_info(self, sentence, word):
        self.ui.sentence_textEdit.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui.word_lineEdit.setDisabled(True)
        self.wordInfoFromInternet.sentence = sentence
        self.wordInfoFromInternet.word = word
        self.wordInfoFromInternet.start()

    @pyqtSlot(dict)
    def has_get_word_info(self, word_info):
        if len(word_info) > 0:
            self.add_deck(word_info)
            self.ui.textBrowser_meaning.setText(word_info['definition'])
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
