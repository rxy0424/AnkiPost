from ui import ui_settingdialog

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings


class SettingDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent=parent)
        self.ui = ui_settingdialog.Ui_settingsDialog()
        self.ui.setupUi(self)

        self.config = QSettings("config.ini", QSettings.IniFormat)

    def set_config(self, source_list: iter, control_list: iter):
        self.ui.infoSourceComboBox.addItems(source_list)
        self.ui.ankiControlcomboBox.addItems(control_list)
        self.update_config()

    def update_config(self):
        self.ui.infoSourceComboBox.setCurrentText(self.config.value("source_name"))
        self.ui.ankiControlcomboBox.setCurrentText(self.config.value("control_name"))
        self.ui.deckLineEdit.setText(self.config.value("deck_name"))
        self.ui.modelLineEdit.setText(self.config.value("model_name"))

