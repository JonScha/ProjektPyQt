from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from Menus import BaseMenu
from baseClasses import DataSetFrame
from typing import TYPE_CHECKING
#from chattest import DataFrameTable
if TYPE_CHECKING:
    from main import MainWindow

class FileMenu(BaseMenu):

    def __init__(self, main_window: "MainWindow"):
        super().__init__(main_window, "File")
        self.main_window = main_window
        self.main_frame = self.main_window.data_frame
        self.data_viewer = self.main_window.data_viewer
        #self.menu : QMenu = self.add_sub_menu("import")

        self.add_sub_menu("import")

        self.add_action_to_main_menu("hey", lambda : print("hello world!"))
