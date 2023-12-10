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

 
    def __init__(self, main_window : "MainWindow", width=700, height=550):
        super().__init__()
        self.main_window = main_window
        self.main_data_set : DataSetFrame = main_window.data_frame
        self.main_data_set_frame : pd.DataFrame = self.main_data_set.get_main_frame()
        self.data_viewer = self.main_window.data_viewer
        
        self.width = width
        self.height = height
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


    def __center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def __check_row_columns_wrapper(f):
        def wrapper(*args):
            # arg_self = self 
            arg_self : BaseFunctionWindow = args[0]
            column = arg_self.column
            num_columns = arg_self.num_columns

            if column % num_columns == 0:
                arg_self.row += 1
                arg_self.column = 0

            ret  = f(*args)
            arg_self.column += 1
            
            return ret
        return wrapper

    @__check_row_columns_wrapper
    def add_entry(self, parameter_name, tooltip_text=None):
        self.parameter_names.append(parameter_name)


        label = QLabel(self, text= parameter_name)
        entry = QtWidgets.QLineEdit(self)
        entry.setPlaceholderText(parameter_name)

        self.layout().addWidget(label, self.row, self.column)
        self.column += 1
        self.layout().addWidget(entry,self.row,self.column )

        if tooltip_text is not None:
            entry.setToolTip(tooltip_text)

        self.widget_list.append(entry)

    def function(self):
        raise NotImplementedError("function not implemented!")
    
    def add_action(self):
        self.data_viewer.add_context_action("example", [self.function])
        