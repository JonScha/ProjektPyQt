from PySide6.QtWidgets import QTableWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QHeaderView, QMenu,QStyledItemDelegate
from PySide6.QtGui import QAction, QColor, QBrush
from PySide6.QtCore import Qt,QAbstractTableModel
from typing import TYPE_CHECKING
import pandas as pd


from baseClasses.dataSetFrame import DataSetFrame

class DataFrameTableView(QTableWidget):
    def __init__(self, main_frame : DataSetFrame):
        super().__init__()
        self.main_set = main_frame
        self.df = main_frame.get_main_frame()
        self.setModel(self.createTableModel(self.main_set))
        self.setSortingEnabled(True)
        self.__stretch_table_view()

        
    def setCellBackgroundColor(self, row, col, color):
        model = self.model()
        index = model.index(row, col)
        item = model.itemData(index)
        if item is not None:
            brush = QBrush(QColor(color))
        
    def createTableModel(self, df):
        model = DataFrameTableModel(df)
        return model
    
    def updateTable(self):
        self.df = self.main_set.get_main_frame()
        self.model().updateData(self.df)
        self.__stretch_table_view()

    def __stretch_table_view(self):

        headers = self.horizontalHeader()
        num_columns = len(self.main_set.get_column_names())
        for i in range(num_columns):
            headers.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        update_action = QAction("Daten aktualisieren", self)
        #update_action.triggered.connect(update_data)
        context_menu.addAction(update_action)
        context_menu.exec(event.globalPos())

        
class DataFrameTableModel(QAbstractTableModel):
    def __init__(self, df : "DataSetFrame"):
        super().__init__()
        self.dataFrame = df.get_main_frame()

    def rowCount(self, parent=None):
        return len(self.dataFrame)

    def columnCount(self, parent=None):
        return len(self.dataFrame.columns)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self.dataFrame.iloc[index.row(), index.column()])
        return None
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.dataFrame.columns[section])
            if orientation == Qt.Vertical:
                return str(self.dataFrame.index[section])
        return None  # Returning Python object directly
    
    def updateData(self, new_df):
        self.beginResetModel()
        self.dataFrame = new_df
        self.endResetModel()
