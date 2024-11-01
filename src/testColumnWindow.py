import sys
from PySide6 import QtWidgets
from baseClasses import DataSetFrame
from Windows.specificClasses.sql.InputWindow import SQLInputWindow
from Windows.baseClasses import BaseColumnWindow
from Menus import BaseMenu
import pandas as pd
import unittest
from main import MainWindow
from _internal.Plugins.pluginManager import PluginManager



class testWindow(BaseColumnWindow):

    def __init__(self, main_window: MainWindow, width=700, height=550):
        super().__init__(main_window, width, height)

        self.add_entry("Hey", "es geht!")
        self.function = self.func
        self.add_ok_button()
        

    def func(self,col, Hey):

        print("Funktion ausgelöst!!!")
        print(Hey)

    
    

class Test(unittest.TestCase):

    def test_s(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_win = MainWindow()
        self.main_win.show()

        handler = PluginManager("Plugins", self.main_win)
        handler.import_plugins()
        print(handler.plugins)
        self.app.exec()

        

if __name__ == "__main__":
    unittest.main()