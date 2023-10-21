from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction
from typing import Callable

class BaseMenu:
    def __init__(self, main_window : QMainWindow):
        self.main_window : QMainWindow = main_window
        
        self.menubar = self.main_window.menuBar()
        self.main_window.setMenuBar(self.menubar)

        self.menu = None

    def add_main_menu(self, menu_title : str):

        self.menu = self.menubar.addMenu(menu_title)    
    
    def add_sub_menu(self, menu_title : str, menu : QMenu) -> QMenu:

        menu = self.menu.addMenu(menu_title) 
        return menu     
    
    def add_action_to_sub_menu(self, name : str,  function : Callable):

        act = QAction(name, self.main_window)
        act.triggered.connect(function)
        self.menu.addAction(act)