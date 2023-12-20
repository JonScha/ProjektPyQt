from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import MainWindow
    from baseClasses import DataSetFrame


class BaseSimplePlugin():


    def __init__(self, main_window : "MainWindow"):
        self.main_window = main_window
        self.main_data_set : DataSetFrame = main_window.data_frame
        self.data_viewer = self.main_window.data_viewer
        self.plugin_name = "Jürgen!"


    def function(self, col):
        raise NotImplementedError("function not implemented!")
    

    def initialize(self):
        self.data_viewer.add_context_action(self.plugin_name, [lambda col : self.function(col)])

    def set_name(self, name : str):
        self.plugin_name = name