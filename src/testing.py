import sys
from PySide6 import QtWidgets
from baseClasses import DataSetFrame
from Windows.specificClasses.sql.InputWindow import SQLInputWindow
from Windows.baseClasses import BaseFunctionWindow
from Menus import BaseMenu
import pandas as pd
from main import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QWidget()
    
    def show_data(sql_query):
        print(f"Executing SQL Query: {sql_query}")
    
    input_window = SQLInputWindow(main_window)
    
    
    input_window.show()
    sys.exit(app.exec())

# if __name__ == '__main__':
#     main()

import sys
import unittest
from PySide6.QtWidgets import QApplication
from Windows.specificClasses.sql import LoginWindow
from baseClasses.connectionDatabase import DatabaseConnector  # Annahme: DatabaseConnector ist in connectionDatabase verfügbar

app = QApplication([])
class TestLoginWindow(unittest.TestCase):
    
    def setUp(self):
        self.main_window = LoginWindow(None, DatabaseConnector())
        self.main_window.show()

    def tearDown(self):
        self.main_window.close()

    def test_ip_address_entry(self):
        ip_address_entry = self.main_window.ip_address_entry
        ip_address_entry.setText("127.0.0.1")
        self.assertEqual(ip_address_entry.text(), "127.0.0.1")

    def test_user_name_entry(self):
        user_name_entry = self.main_window.user_name_entry
        user_name_entry.setText("username")
        self.assertEqual(user_name_entry.text(), "username")

    def test_password_entry(self):
        password_entry = self.main_window.password_entry
        password_entry.setText("password")
        self.assertEqual(password_entry.text(), "password")

    def test_database_entry(self):
        database_entry = self.main_window.database_entry
        database_entry.setText("mydb")
        self.assertEqual(database_entry.text(), "mydb")

class TestbaseFunctionWindow(unittest.TestCase):

    def setUp(self):
        self.main_window = BaseFunctionWindow(None, DatabaseConnector())
        self.main_window.show()


    def test_anything(self):
        self.main_window.add_button("exit", sys.exit)
        self.main_window.add_boolean_dropdown("boolean_drop")
        self.main_window.add_entry("entry_param")

class testBaseColumnWindow(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

if __name__ == '__main__':
    
    def test_func(x, a, b):

        if a:
            return 10, 20
        elif b:
            return 200,65
        else:
            return 5,20


    df = DataSetFrame()#
    data = pd.DataFrame(["a","b", "c"])
    df.set_main_frame(data)

    main_window = MainWindow()
    menus = BaseMenu(main_window)
   
    file_menu = menus.add_main_menu("File")
    menus.add_action_to_sub_menu("Hallo!" , lambda : print(df.get_numpy_array()))

    main_window.show()
 
    

    sys.exit(app.exec())