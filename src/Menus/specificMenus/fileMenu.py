from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from Menus import BaseMenu
from baseClasses import DataSetFrame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MainWindow

class FileMenu():

    def __init__(self, main_window: "MainWindow"):

        self.main_menu = BaseMenu(main_window, "File")
        self.main_window = main_window
        # self.menu : QMenu = self.add_sub_menu("import")

        self.sub1 = self.main_menu.add_sub_menu("Sub1")
        self.main_menu.add_action_to_sub_menu("import", lambda : print("Hello there!"))

        #self.main_menu.add("Hello")
        # act = QAction("funktion 1", main_window)
        # act.triggered.connect(main_window.show_login_window)
        # self.sub1.addAction(act)

        self.__create_import()
        
        
    def __create_import(self):
        act = QAction("import file", self.main_window)
        df = DataSetFrame()
        act.triggered.connect(lambda : df.import_file("I:/ProjektPyQt/src/TestDateien/data.csv"))
        self.sub1.addAction(act)
