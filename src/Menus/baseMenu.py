from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction
from typing import Callable, TYPE_CHECKING


if TYPE_CHECKING:
    from main import MainWindow

class BaseMenu:
    def __init__(self, main_window : "MainWindow", menu_title : str):
        self.main_window : "MainWindow" = main_window
        self.main_window.show_login_window()
        self.menubar = self.main_window.menuBar()

        self.main_window.setMenuBar(self.menubar)

        self.menu = self.menubar.addMenu(menu_title)

    def add_main_menu(self, menu_title : str):
        return
        self.menu = self.menubar.addMenu(menu_title)
        pass

    
    def add_sub_menu(self, menu_title : str) -> QMenu:

        menu = self.menu.addMenu(menu_title) 
        return menu     
    
    def add_action_to_sub_menu(self, name : str,  function : Callable):

        act = QAction(name, self.main_window)
        act.triggered.connect(function)
        self.menu.addAction(act)