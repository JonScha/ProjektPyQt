from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from Menus import BaseMenu
from baseClasses import DataSetFrame
from typing import TYPE_CHECKING
#from chattest import DataFrameTable
if TYPE_CHECKING:
    from main import MainWindow

class FileMenu():

    def __init__(self, main_window: "MainWindow"):

        self.main_menu = BaseMenu(main_window, "File")
        self.main_window = main_window
        self.main_frame = self.main_window.data_frame
        self.data_viewer = self.main_window.data_viewer
        #self.menu : QMenu = self.add_sub_menu("import")

        self.sub1 = self.main_menu.add_sub_menu("import")

        self.__create_import()
        
        self.main_menu.add_action_to_sub_menu("hello", print)
    def __create_import(self):
        act = QAction("import file", self.main_window)
        act.triggered.connect(self.main_frame.import_file)
        act.triggered.connect(self.__update_table)
        self.sub1.addAction(act)
        #self.main_menu.add_action_to_sub_menu("import file", act)

    def __update_table(self):
        self.data_viewer.update()
        self.data_viewer.set_width_columns()

