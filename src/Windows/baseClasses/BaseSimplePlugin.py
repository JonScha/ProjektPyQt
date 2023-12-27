from typing import TYPE_CHECKING
from Plugins.baseClasses import BasePlugin
if TYPE_CHECKING:
    from main import MainWindow
    from baseClasses import DataSetFrame


class BaseSimplePlugin(BasePlugin):


    def __init__(self, main_window : "MainWindow"):
        super().__init__(main_window)
        pass

 
    def initialize(self):
        self.data_viewer.add_simple_plugin(self)

    def set_name(self, name : str):
        self.name = name