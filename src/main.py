import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QMenu, QMenuBar, QWidgetAction, QTableView
from PySide6.QtGui import QAction
from Menus import BaseMenu, FileMenu
from Windows.specificClasses.sql import LoginWindow
from Windows.baseClasses import DataFrameTableView
from baseClasses import DatabaseConnector
# from Menus.specificMenus import FileMenu
# from DataBaseWindows.LoginWindow import Login_Window
# from DataSetWindows.DataMarkWindow import DataMarkWindow
# from CustomGUIWidgets import customTreeView, DataTable, SQLMenu, FileMenu, DSMenu
from baseClasses import DataSetFrame
# from dataScienceWindows.specificClasses.WindowClasses import normTestWindow, tTestWindow, chiQuadratTestWindow, coeffMatrix

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.width = 800
        self.height = 650
        self.setWindowTitle("Ihr Hauptfenster")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.database_conn = DatabaseConnector()
        

        self.data_frame = DataSetFrame()
        
        # To-Do
        self.data_viewer = DataFrameTableView(self.data_frame)
        #self.data_viewer = QTableView(self)
        self.file_menu = FileMenu(self)
        self.setCentralWidget(self.data_viewer)
        
        self.setGeometry(20, 30, self.width, self.height)
        self.__center()
        #
        self.login_window = None
        

    def __center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_login_window(self):
        self.login_window = LoginWindow(self, self.database_conn)
        self.login_window.show()

    def show_chi_quadrat_test(self):
        #win = chiQuadratTestWindow(self, self.main_data_set)
        pass
        
    def show_coeffs(self):
       # win = coeffMatrix(self, self.main_data_set)
       pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main_Win = MainWindow()
    Main_Win.show()
    sys.exit(app.exec())

