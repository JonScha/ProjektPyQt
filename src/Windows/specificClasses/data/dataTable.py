import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMenu
from PySide6.QtGui import QColor, QBrush, QAction, QMouseEvent
from PySide6.QtCore import QPoint
from typing import TYPE_CHECKING, Callable
import pandas as pd

if TYPE_CHECKING:
    from main import MainWindow

class DataFrameTable(QTableWidget):
    def __init__(self, main_window : "MainWindow"):
        super().__init__()
        self.main_window = main_window
        self.main_data_set_frame = main_window.data_frame
        self.main_frame : pd.DataFrame = main_window.data_frame.get_main_frame()
        self.setRowCount(self.main_frame.shape[0])
        self.setColumnCount(self.main_frame.shape[1])
        self.set_width_columns()

        self.name_action_dict_column : dict = {}

        for row in range(self.main_frame.shape[0]):
            for col in range(self.main_frame.shape[1]):
                item = QTableWidgetItem(str(self.main_frame.iat[row, col]))
                self.setItem(row, col, item)

    def setCellBackgroundColor(self, row, col, color):
        item = self.item(row, col)
        if item is not None:
            brush = QBrush(QColor(color))
            item.setBackground(brush)

    def set_column_background_color(self, col, color):

        for row in range(self.main_frame.shape[0]):
            item = self.item(row, col)

            brush = QBrush(QColor(color))
            item.setBackground(brush)

    def set_width_columns(self):

        for col in range(self.main_frame.shape[1]):
            self.setColumnWidth(col, 200)

    def update(self):
        """
            Updates the values in the table (resets the tablr with new values)
        """
        self.main_frame : pd.DataFrame = self.main_window.data_frame.get_main_frame()
        self.setRowCount(self.main_frame.shape[0])
        self.setColumnCount(self.main_frame.shape[1])

        for row in range(self.main_frame.shape[0]):
            for col in range(self.main_frame.shape[1]):
                item = QTableWidgetItem(str(self.main_frame.iat[row, col]))
                self.setItem(row, col, item)


    def __add_context_action(self, context_menu : QMenu, action  : Callable, name : str):
        act = QAction(name, self)
        context_menu.addAction(act)

    # overwritten-fuction fromn QTabelWidget
    def contextMenuEvent(self, event : QMouseEvent) -> None:
        context_menu = QMenu(self)
    
        normalize_action = QAction("normalize column", self)
        context_menu.addAction(normalize_action)
        #add_action("normalize column",self.main_data_set_frame.normalize_column(current_column), self.update())
        coordinates : QPoint = event.pos()
        x, y = coordinates.toTuple()
        context_menu.exec(self.mapToGlobal(event.pos()))
        current_column = self.columnAt(x)

        
        normalize_action.triggered.connect(self.main_data_set_frame.normalize_column(current_column))
        normalize_action.triggered.connect(self.update())

        # if action == normalize_action:
        #     self.main_data_set_frame.normalize_column(current_column)
        #     self.update()
        
    
        



            

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