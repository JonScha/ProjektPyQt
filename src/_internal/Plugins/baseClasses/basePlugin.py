from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MainWindow
    from baseClasses import DataSetFrame


class BasePlugin():
    """
        base class which every Plugin class inheritances
    
    """

    def __init__(self, main_window : "MainWindow") -> None:
        self.data_viewer = main_window.data_viewer
        self.main_window = main_window
        self.main_data_set : "DataSetFrame" = main_window.data_frame
        self.data_viewer = self.main_window.data_viewer
        self.name = "to be replaced!"
        self.__tooltip = None

    def initialize(self):
        raise NotImplementedError("init method not implemented!")


    def function(self):
        raise NotImplementedError("function not implemented!")
   
    def set_tooltip(self, tooltip : str):
        self.__tooltip  = tooltip