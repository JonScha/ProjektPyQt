from Windows.baseClasses import BaseFunctionWindow
from abc import abstractmethod, ABC, ABCMeta
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy, QGridLayout, QLabel
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from typing import TYPE_CHECKING
import pandas as pd
import inspect

if TYPE_CHECKING:
    from main import MainWindow
    from baseClasses import DataSetFrame


class BaseColumnWindow(QtWidgets.QWidget):

 
    def __init__(self, main_window : "MainWindow",has_2_datasets=False, width=700, height=550):
        self.main_window = main_window
        self.main_data_set : DataSetFrame = main_window.data_frame
        self.main_data_set_frame : pd.DataFrame = self.main_data_set.get_main_frame()
        self.data_viewer = self.main_window.data_viewer
        self.has_2_datasets = has_2_datasets
        self.width = width
        self.height = height
        self.function = None
        self.result = None
        self.result_names = None
        self.num_rows = 3
        self.num_columns = 4
        self.row = 0
        self.column = 0
        self.parameter_names = []
        self.widget_list : list[QtWidgets.QLineEdit | QtWidgets.QComboBox] = []
        self.non_callable_widget_list = []
        self.parameters = {}

       
        self.setWindowTitle("Base Function Window")
        self.setGeometry(100, 100, width, height)

        layout = QGridLayout(self)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)
        
        self.__center()
        self.setLayout(layout)
        self.setMaximumSize(self.width, self.height)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        

if __name__ == "__main__":
    test = BaseColumnWindow()
    test.func(1)