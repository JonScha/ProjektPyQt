from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from .resultWindow import ResultWindow
import inspect

class BaseFunctionWindow(QtWidgets.QWidget):
    def __init__(self, main_window, main_data_set, has_2_datasets=False, width=800, height=550):
        super().__init__()
        self.main_window = main_window
        self.main_data_set = main_data_set
        self.has_2_datasets = has_2_datasets
        self.width = width
        self.height = height
        self.function = None
        self.result = None
        self.result_names = None
        self.num_rows = 3
        self.num_columns = 3
        self.row = 0
        self.column = 0
        self.parameter_names = []
        self.widget_list = []
        self.non_callable_widget_list = []
        self.parameters = {}

        self.setWindowTitle("Base Function Window")
        self.setGeometry(100, 100, width, height)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addStretch(1)

    def add_entry(self, parameter_name, tooltip_text=None):
        self.parameter_names.append(parameter_name)

        entry = QtWidgets.QLineEdit(self)
        entry.setPlaceholderText(parameter_name)
        self.layout().addWidget(entry)
        if tooltip_text is not None:
            entry.setToolTip(tooltip_text)

        self.widget_list.append(entry)

    def add_dropdown(self, parameter_name, values, tooltip_text=None):
        self.parameter_names.append(parameter_name)

        dropdown = QtWidgets.QComboBox(self)
        dropdown.addItems(values)
        self.layout().addWidget(dropdown)
        if tooltip_text is not None:
            dropdown.setToolTip(tooltip_text)

        self.widget_list.append(dropdown)

    def add_boolean_dropdown(self, parameter_name, tooltip_text=None):
        self.parameter_names.append(parameter_name)

        dropdown = QtWidgets.QComboBox(self)
        dropdown.addItems(["True", "False"])
        self.layout().addWidget(dropdown)
        if tooltip_text is not None:
            dropdown.setToolTip(tooltip_text)

        self.widget_list.append(dropdown)

    def _set_parameters(self):
        for name, widget in zip(self.parameter_names, self.widget_list):
            tmp : QtWidgets.QComboBox = widget.currentText()
            if tmp.isdigit():
                self.parameters[name] = int(tmp)
            elif tmp == "False":
                self.parameters[name] = False
            elif tmp == "True":
                self.parameters[name] = True
            elif not tmp:
                self.parameters[name] = None
            else:
                self.parameters[name] = tmp

    def get_parameters(self):
        return self.parameters

    def get_root(self):
        return self

    def _add_button(self):
        button = QtWidgets.QPushButton("OK", self)
        button.clicked.connect(self._button_fun)
        self.layout().addWidget(button)

    def add_button(self, text, button_function, tooltip_text=None):
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

        x, y = self.main_data_set.get_raw_data_split()
        params = self.get_parameters()

        args = inspect.getfullargspec(self.function).args
        erstes_argument = args[0]
        zweites_argument = args[1]

        params[erstes_argument] = x

        if self.has_2_datasets:
            params[zweites_argument] = y
            self.result = self.function(**params)
        else:
            self.result = self.function(**params)

        self.show_result_window()

    def show_result_window(self):
        win = ResultWindow(self, results=self.result, results_names=self.result_names)

    def set_result_names(self, names):
        self.result_names = names

    def set_function(self, function):
        self.function = function
