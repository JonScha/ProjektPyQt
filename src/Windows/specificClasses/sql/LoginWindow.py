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
        self.database_type = ""
        self.port_number = 0

        self.database_dialects = ["mysql", "oracle", "postgresql", "mssql", ]

        self.debug_flag = True

        self.__create_ui()

    def __create_ui(self):
        self.setWindowTitle("Login Window")
        self.setGeometry(100, 100, 400, 300)

        self.ip_address_entry = QtWidgets.QLineEdit(self)
        self.ip_address_entry.setPlaceholderText("IP Address")

        self.port_entry = QtWidgets.QLineEdit(self)
        self.port_entry.setPlaceholderText("port number")

        self.user_name_entry = QtWidgets.QLineEdit(self)
        self.user_name_entry.setPlaceholderText("User Name")

        self.password_entry = QtWidgets.QLineEdit(self)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)

        self.database_entry = QtWidgets.QLineEdit(self)
        self.database_entry.setPlaceholderText("Database Name")

        self.database_type_dropdown = QtWidgets.QComboBox(self)
        self.database_type_dropdown.addItems(self.database_dialects)

        self.button = QtWidgets.QPushButton("Connect", self)
        self.button.clicked.connect(self.__button_function)

        layout = QtWidgets.QVBoxLayout()
        
        layout.addWidget(self.database_type_dropdown)
        layout.addWidget(self.ip_address_entry)
        layout.addWidget(self.port_entry)
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

        self.port_number = int(self.port_entry.text())

        self.database_type = self.database_type_dropdown.currentText()


        self.__login_to_database()

        self.close()

    def get_root(self):
        return self

    def __get_login_data(self):
        return self.database_type, self.port_number, self.ip_address,self.database ,self.user_name, self.password

    def __login_to_database(self):
        db_type, port, ip, db_name, user_name, password = self.__get_login_data()

        if self.debug_flag:
            db_type = "postgresql"
            user_name = "postgres"
            db_name = "postgres"
            password = "hans"
            port = "5432"


        if any(value != "" for value in [ip, db_name, user_name, password]):
            
            if (self.main_data_base_connector.connect(db_type, port, ip, db_name, user_name, password)):

                print("Connection successful!") 
            else:
                print("Connection failed!!!")
                
                
        
            