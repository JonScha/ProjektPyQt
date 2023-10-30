import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QColor, QBrush
from typing import TYPE_CHECKING
import pandas as pd
#from main import MainWindow

if TYPE_CHECKING:
    from main import MainWindow

class DataFrameTable(QTableWidget):
    def __init__(self, main_window : "MainWindow"):
        super().__init__()
        self.main_window = main_window
        self.main_frame : pd.DataFrame = main_window.data_frame.get_main_frame()
        self.setRowCount(self.main_frame.shape[0])
        self.setColumnCount(self.main_frame.shape[1])

        for row in range(self.main_frame.shape[0]):
            for col in range(self.main_frame.shape[1]):
                item = QTableWidgetItem(str(self.main_frame.iat[row, col]))
                self.setItem(row, col, item)

    def setCellBackgroundColor(self, row, col, color):
        item = self.item(row, col)
        if item is not None:
            brush = QBrush(QColor(color))
            item.setBackground(brush)


    def update(self):

        self.main_frame : pd.DataFrame = self.main_window.data_frame.get_main_frame()
        self.setRowCount(self.main_frame.shape[0])
        self.setColumnCount(self.main_frame.shape[1])

        for row in range(self.main_frame.shape[0]):
            for col in range(self.main_frame.shape[1]):
                item = QTableWidgetItem(str(self.main_frame.iat[row, col]))
                self.setItem(row, col, item)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    table = DataFrameTable(window)
    table.setCellBackgroundColor(1,1, "#FF0000")
    window.setCentralWidget(table)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()