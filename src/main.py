import sys
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout
from Menus.specificMenus import FileMenu, SQLMenu, DataScienceMenu
from Windows.specificClasses.sql import LoginWindow, SQLInputWindow
from Windows.specificClasses.data import DataFrameTable
from baseClasses import DatabaseConnector
from seaborn import heatmap
import pandas as pd
from baseClasses import DataSetFrame

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.width = 800
        self.height = 650
        self.setWindowTitle("Ihr Hauptfenster")

        self.grid_layout = QGridLayout()
        self.database_conn = DatabaseConnector()
        
        data = [0,1,2,3]
        df = pd.DataFrame(data)
        self.data_frame = DataSetFrame()
        self.data_frame.set_main_frame(df)
        
        # To-Do
        self.data_viewer = DataFrameTable(self)
        self.file_menu = FileMenu(self)
        self.setCentralWidget(self.data_viewer)
        self.layout().setContentsMargins(0,0,0,0)


        self.sql_menu = SQLMenu(self)
        self.data_science_menu = DataScienceMenu(self)
        
        
        self.setGeometry(20, 30, self.width, self.height)
        self.__center()
        self.login_window = None
        self.input_window = None
        

    def __center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_login_window(self):
        self.login_window = LoginWindow(self, self.database_conn)
        self.login_window.show()

    def show_sql_input_window(self):
        self.input_window = SQLInputWindow(self)
        self.input_window.show()
            
    def show_coeffs(self):
       heatmap(self.data_frame.calc_coeff_matrix())
       plt.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main_Win = MainWindow()
    Main_Win.show()
    sys.exit(app.exec())

