import sys
from PySide6 import QtWidgets
from baseClasses import DataSetFrame
from Windows.specificClasses.sql.InputWindow import SQLInputWindow
from Windows.baseClasses import BaseFunctionWindow

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

if __name__ == '__main__':
    #unittest.main()
    # main_window = QtWidgets.QTabWidget()
    # login_window = BaseFunctionWindow(main_window, DatabaseConnector())
    # login_window.show()


    def test_func(x, a, b):

        if a:
            return 10, 20
        elif b:
            return 200,65
        else:
            return 5,20


    df = DataSetFrame()
    main_window = BaseFunctionWindow(None, df)
    main_window.add_boolean_dropdown("a")
    main_window.add_boolean_dropdown("b")
    
    main_window.add_function_button()
    main_window.set_function(test_func)
    main_window.set_result_names(["1", "2"])
    main_window.show()
    print(main_window.get_parameters())
  

    sys.exit(app.exec())