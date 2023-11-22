from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction
from typing import Callable, TYPE_CHECKING


if TYPE_CHECKING:
    from main import MainWindow

class BaseMenu(QMenu):
    def __init__(self, main_window : "MainWindow", menu_title : str):
        super().__init__(main_window)
        self.main_window : "MainWindow" = main_window
        self.main_window.show_login_window()
        # returns the menuBar from the MainWindow
        self.menubar : QMenuBar = self.main_window.menuBar()
        self.menu : QMenu = self.menubar.addMenu(menu_title)

    def add_sub_menu(self, menu_title : str) -> QMenu:
        # creates new menu on the mainMenu and returns it
        menu = self.menu.addMenu(menu_title) 
        return menu     
    
    def add_action_to_sub_menu(self, name : str,  function : Callable):

        act = QAction(name, self.main_window)
        act.triggered.connect(function)
        self.menu.addAction(act)

    def add_action_to_main_menu(self, name : str, function : Callable):

        act = QAction(name, self.main_window)
        act.triggered.connect(function)
        self.menu.addAction(act)
