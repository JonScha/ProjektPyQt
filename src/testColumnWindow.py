import sys
from PySide6 import QtWidgets
from baseClasses import DataSetFrame
from Windows.specificClasses.sql.InputWindow import SQLInputWindow
from Windows.baseClasses import BaseColumnWindow
from Menus import BaseMenu
import pandas as pd
import unittest
from main import MainWindow



class Test(unittest.TestCase):


        
  

    def test_s(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_win = MainWindow()
        self.main_win.show()
        self.window = BaseColumnWindow(self.main_win)
        self.window.add_entry("Hey", "es geht!")
        self.window.add_ok_button()
        self.main_win.data_viewer.add_context_action_window("example", self.window)
        

        self.app.exec()

        

if __name__ == "__main__":
    unittest.main()