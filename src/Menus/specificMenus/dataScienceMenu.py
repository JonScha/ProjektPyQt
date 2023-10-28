from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from Menus import BaseMenu
from baseClasses import DataSetFrame
from Windows.specificClasses.sql import LoginWindow, InputWindow
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import MainWindow

class DataScienceMenu():

    
    def __init__(self, main_window: "MainWindow"):   
        self.main_menu = BaseMenu(main_window, "DataScience")
        self.main_window = main_window
        self.main_frame = main_window.data_frame
        self.data_viewer = main_window.data_viewer
        self.data_conn = main_window.database_conn

        self.main_menu.add_action_to_sub_menu("show coeff matrix",main_window.show_coeffs)