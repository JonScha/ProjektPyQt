from main import MainWindow
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QLabel
from PySide6.QtCore import Qt
from . import BaseColumnWindow, ResultWindow





class BaseColumnResultWindow(BaseColumnWindow):


    def __init__(self, main_window: MainWindow, width=700, height=550):
        super().__init__(main_window, width, height)

        
    def show_result_window(self):

        self.win = ResultWindow(self,self.result, self.result_names)
        self.win.show()

    def ok_button_function(self, col, parameters):
        self.result = self.function(col, **parameters)

        self.show_result_window()

    def __set_parameters(self):
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

    def show(self, col):
        """
            shows the window and sets the selected_column to the current selected column
        """
        self.selected_column = col
        print("Columns: ", self.main_data_set.get_column_names())
        
        self.main_button.clicked.connect(lambda : (self.__set_parameters(),
                                                   self.ok_button_function(col, self.parameters)))
        
        super().get_baseClass_show()
        

