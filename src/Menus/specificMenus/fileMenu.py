from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from Menus import BaseMenu
from baseClasses import DataSetFrame
from typing import TYPE_CHECKING
#from chattest import DataFrameTable
if TYPE_CHECKING:
    from main import MainWindow
    from Windows.baseClasses import DataFrameTableView

class FileMenu():

    def __init__(self, main_window: "MainWindow"):

        self.main_menu = BaseMenu(main_window, "File")
        self.main_window = main_window
        self.main_frame = self.main_window.data_frame
        self.data_viewer = self.main_window.data_viewer
        # self.menu : QMenu = self.add_sub_menu("import")

        self.sub1 = self.main_menu.add_sub_menu("Sub1")

        self.__create_import()
        
        
    def __create_import(self):
        act = QAction("import file", self.main_window)
        act.triggered.connect(lambda :self.main_frame.import_file("I:/ProjektPyQt/src/TestDateien/data.csv"))
        act.triggered.connect(self.__update_table)
        act.triggered.connect(lambda : print(self.main_frame.get_numpy_array()))
        self.sub1.addAction(act)

    def __update_table(self):

        self.data_viewer.update()
        print("Hallo")

