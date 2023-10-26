import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from baseClasses import DataSetFrame

class DataFrameViewer(QWidget):
    def __init__(self, data_frame : "DataSetFrame"):
        super().__init__()
        self.data : pd.DataFrame = data_frame.get_main_frame()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.model = QStandardItemModel(self)
        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)

        for row in range(self.data.shape[0]):
            items = [QStandardItem(str(self.data.iat[row, col])) for col in range(self.data.shape[1])]
            self.model.appendRow(items)

        self.layout.addWidget(self.tableView)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pandas DataFrame Viewer")
        self.setGeometry(100, 100, 800, 600)

        data = pd.DataFrame({'A': [1, 2, 3, 4],
                             'B': [5, 6, 7, 8]})
        
        data_viewer = DataFrameViewer(data)
        self.setCentralWidget(data_viewer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
