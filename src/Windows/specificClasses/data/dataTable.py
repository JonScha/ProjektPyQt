import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMenu, QWidget
from PySide6.QtGui import QColor, QBrush, QAction, QMouseEvent
from PySide6.QtCore import QPoint
from typing import TYPE_CHECKING, Callable
import pandas as pd

if TYPE_CHECKING:
    from main import MainWindow

class DataFrameTable(QTableWidget):
    """
        A tabular representation of primitive data from a DataSetFrame

        Methods
        -------
        set_cell_background_color : row, col, color
            colors a cell in a  (row,col) with a specified color
        set_column_background_color : col, color
            colors a whole column
        update : 
            refreshes the data view ( i.e. when the DataSetFrame changed)
        __set_width_columns : 
            sets the width of all columns to 200
        



    """
    def __init__(self, main_window : "MainWindow"):
        super().__init__()
        self.main_window = main_window
        self.main_data_set_frame = main_window.data_frame
        self.main_frame : pd.DataFrame = main_window.data_frame.get_main_frame()
        self.setRowCount(self.main_frame.shape[0])
        self.setColumnCount(self.main_frame.shape[1])
        self.__set_width_columns()
        self.current_column = 1
        self.context_menu = QMenu(self)
        self.name_action_list : list = []
        self.menu_check = False
        self.add_context_action("hello", [ lambda col : self.set_column_background_color(col, "red")])

        # Sets first init dataFrame
        for row in range(self.main_frame.shape[0]):
            for col in range(self.main_frame.shape[1]):
                item = QTableWidgetItem(str(self.main_frame.iat[row, col]))
                self.setItem(row, col, item)

    def set_cell_background_color(self, row, col, color):
        item = self.item(row, col)
        if item is not None:
            brush = QBrush(QColor(color))
            item.setBackground(brush)

    def set_column_background_color(self, col, color):
        for row in range(self.main_frame.shape[0]):
            item = self.item(row, col)
            brush = QBrush(QColor(color))
            item.setBackground(brush)

    def __set_width_columns(self):
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


    def add_context_action(self, name : str, functions : list[Callable]):
            self.name_action_list.append(functions)
            act = QAction(name, self)
            self.context_menu.addAction(act)

    def add_context_action_window(self, name : str,  window : QWidget):
            self.name_action_list.append([lambda col : window.show()])
            act = QAction(name, self)
            self.context_menu.addAction(act)


    # overwritten-fuction from QTableWidget
    def contextMenuEvent(self, event : QMouseEvent) -> None:
        coordinates : QPoint = event.pos()
        x, y = coordinates.toTuple()
        self.current_column = self.columnAt(x)

        if not self.menu_check:
            for i, action in enumerate(self.context_menu.actions()):
                for func in self.name_action_list[i]:
                    action.triggered.connect(lambda : func(self.current_column))
            self.menu_check = True
        
        self.context_menu.exec(self.mapToGlobal(event.pos()))
        self.current_column = self.columnAt(x)

      



            

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    table = DataFrameTable(window)
    table.set_cell_background_color(1,1, "#FF0000")
    window.setCentralWidget(table)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()