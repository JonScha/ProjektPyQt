from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy, QGridLayout, QLabel
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from .resultWindow import ResultWindow
from baseClasses import DataSetFrame
import pandas as pd
from typing import Callable, TYPE_CHECKING
import inspect

if TYPE_CHECKING:
    from main import MainWindow
class BaseFunctionWindow(QtWidgets.QWidget):
    def __init__(self, main_window : "MainWindow",has_2_datasets=False, width=700, height=550):
        super().__init__()
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

        
    @__check_row_columns_wrapper
    def add_dropdown(self, parameter_name, values, tooltip_text=None):
        self.parameter_names.append(parameter_name)

        label = QLabel(self, text= parameter_name)
        dropdown = QtWidgets.QComboBox(self)
        dropdown.addItems(values)
        self.layout().addWidget(label, self.row, self.column)
        self.column += 1
        self.layout().addWidget(dropdown, self.row, self.column)
        if tooltip_text is not None:
            dropdown.setToolTip(tooltip_text)

        self.widget_list.append(dropdown)
        
    @__check_row_columns_wrapper
    def add_boolean_dropdown(self, parameter_name, tooltip_text = None):
        self.add_dropdown(parameter_name, ["True", "False"], tooltip_text)
  
    def _set_parameters(self):
        for name, widget in zip(self.parameter_names, self.widget_list):

            tmp : str = ""
            
            if type(widget) == QtWidgets.QComboBox:
                tmp  = widget.currentText()
            else:
                tmp  = widget.text()
            if tmp.isdigit():
                self.parameters[name] = int(tmp)
            elif tmp == "False":
                self.parameters[name] = False
            elif tmp == "True":
                self.parameters[name] = True
            else:
                self.parameters[name] = tmp

            print(self.parameters)

    def get_parameters(self):
        return self.parameters

    def get_root(self):
        return self

    def add_function_button(self):
        button = QtWidgets.QPushButton("OK", self)
        button.clicked.connect(self._button_fun)
        self.layout().addWidget(button, self.row + 1, 2)

    def add_button(self, text, button_function : Callable, tooltip_text=None):
        button = QtWidgets.QPushButton(text, self)
        button.clicked.connect(button_function)
        self.layout().addWidget(button)
        if tooltip_text is not None:
            button.setToolTip(tooltip_text)

        self.non_callable_widget_list.append(button)
        return button

    def _button_fun(self):
        self._set_parameters()

        if self.function is None:
            raise NotImplementedError("Function not implemented!")

        # x, y = self.main_data_set.get_raw_data_split()
        params : dict = self.get_parameters()

        args = inspect.getfullargspec(self.function).args
        erstes_argument = args[0]
        if len(args) >= 2:
            zweites_argument = args[1]

        # params[erstes_argument] = x

        # if self.has_2_datasets:
        #     params[zweites_argument] = y
        #     self.result = self.function(**params)
        # else:
        #     self.result = self.function(**params)
        self.result = self.function(**params)

        self.show_result_window()

    def show_result_window(self):
        self.win = ResultWindow(self, results=self.result, results_names=self.result_names)
        self.win.show()


    def set_result_names(self, names):
        self.result_names = names

    def set_function(self, function):
        self.function = function
