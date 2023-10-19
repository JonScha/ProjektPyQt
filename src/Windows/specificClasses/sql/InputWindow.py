import pandas as pd
import sys
#from baseClasses.connectionDatabase import DatabaseConnector
from PySide6 import QtWidgets # Annahme: DataPreviewWindow ist eine separate Klasse

class SQLInputWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Neues Fenster")
        self.setGeometry(100, 100, 400, 500)
        self.main_window = main_window

        self._create_button()
        self._create_text_input()

        layout = QtWidgets.QVBoxLayout()
        #layout = QtWidgets.QGridLayout()
        layout.addWidget(self.sql_text)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.sql_query_string = ""

    def _create_button(self):
        self.button = QtWidgets.QPushButton("Connect", self)
        self.button.clicked.connect(self._button_function)

    def _button_function(self):
        self.sql_query_string = self.sql_text.toPlainText()
        self.close()

    def _create_text_input(self):
        self.sql_text = QtWidgets.QTextEdit("Your SQL Query here", self)

    def get_sql_query(self):
        return self.sql_query_string



