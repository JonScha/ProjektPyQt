import pandas as pd
import sys
from typing import TYPE_CHECKING
#from baseClasses.connectionDatabase import DatabaseConnector
from PySide6 import QtWidgets # Annahme: DataPreviewWindow ist eine separate Klasse

if TYPE_CHECKING:
    from main import MainWindow
class SQLInputWindow(QtWidgets.QWidget):
    def __init__(self, main_window : "MainWindow"):
        super().__init__()
        self.setWindowTitle("Neues Fenster")
        self.setGeometry(100, 100, 400, 500)
        self.main_window = main_window
        self.db_conn = main_window.database_conn
        self.main_frame = main_window.data_frame
        self.dv = main_window.data_viewer
        self._create_button()
        self._create_text_input()

        layout = QtWidgets.QVBoxLayout()
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
        new_frame = self.db_conn.postgresql_to_dataframe(self.sql_query_string, self.main_frame.get_column_names())
        self.main_frame.set_main_frame(new_frame)
        self.dv.update()

    def _create_text_input(self):
        self.sql_text = QtWidgets.QTextEdit("Your SQL Query here", self)

    def get_sql_query(self):
        return self.sql_query_string



