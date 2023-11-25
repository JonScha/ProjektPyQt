from typing import List
from PySide6 import QtWidgets
from typing import TYPE_CHECKING
from baseClasses.connectionDatabase import DatabaseConnector

if TYPE_CHECKING:
    from main import MainWindow

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, main_window: "MainWindow"):
        super().__init__()
        self.main_window = main_window
        self.main_data_base_connector = main_window.database_conn

        self.ip_address = ""
        self.user_name = ""
        self.password = ""
        self.database = ""

        self.debug_flag = False

        self.__create_ui()

    def __create_ui(self):
        self.setWindowTitle("Login Window")
        self.setGeometry(100, 100, 400, 300)

        self.ip_address_entry = QtWidgets.QLineEdit(self)
        self.ip_address_entry.setPlaceholderText("IP Address")

        self.user_name_entry = QtWidgets.QLineEdit(self)
        self.user_name_entry.setPlaceholderText("User Name")

        self.password_entry = QtWidgets.QLineEdit(self)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)

        self.database_entry = QtWidgets.QLineEdit(self)
        self.database_entry.setPlaceholderText("Database Name")

        self.button = QtWidgets.QPushButton("Connect", self)
        self.button.clicked.connect(self.__button_function)

        layout = QtWidgets.QVBoxLayout()
        
        layout.addWidget(self.ip_address_entry)
        layout.addWidget(self.user_name_entry)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.database_entry)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def __button_function(self):
        self.ip_address : QtWidgets.QLineEdit = self.ip_address_entry.text()
        self.user_name = self.user_name_entry.text()
        self.password = self.password_entry.text()
        self.database = self.database_entry.text()

        self.__login_to_database()

        self.close()

    def get_root(self):
        return self

    def __get_login_data(self):
        return self.ip_address,self.database ,self.user_name, self.password

    def __login_to_database(self):
        ip, db_name, user_name, password = self.__get_login_data()

        if any(value != "" for value in [ip, db_name, user_name, password]):
            try:
                self.main_data_base_connector.connect(ip, db_name, user_name, password)
                print("Connection successful!!!!!")
            except BaseException as e:
                print("Fehler!!!!!")

                print(str(e))