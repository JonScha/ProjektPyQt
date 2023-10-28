from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from Menus import BaseMenu
from baseClasses import DataSetFrame
from Windows.specificClasses.sql import LoginWindow, InputWindow
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import MainWindow
    from Windows.baseClasses import DataFrameTableView



class SQLMenu():

    def __init__(self, main_window: "MainWindow"):   
        self.main_menu = BaseMenu(main_window, "SQL")
        self.main_window = main_window
        self.main_frame = main_window.data_frame
        self.data_viewer = main_window.data_viewer
        self.data_conn = main_window.database_conn

        self.main_menu.add_action_to_sub_menu("connect",main_window.show_login_window)
        self.main_menu.add_action_to_sub_menu("sql query",main_window.show_sql_input_window)
    