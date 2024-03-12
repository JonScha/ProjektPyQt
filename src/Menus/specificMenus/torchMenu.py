from Menus import BaseMenu
from typing import TYPE_CHECKING
from baseClasses import torchModuleHandler

if TYPE_CHECKING:
    from main import MainWindow

class TorchMenu(BaseMenu):


    def __init__(self, main_window: "MainWindow"):
        super().__init__(main_window, "pyTorch")
        self.main_window = main_window
        self.main_frame = main_window.data_frame
        self.data_viewer = main_window.data_viewer
        self.data_conn = main_window.database_conn

        self.fit_window = main_window.torch_fit_window

        moudleHandler = torchModuleHandler(self.main_window,self.main_frame)

        self.add_action_to_main_menu("print", lambda : print("Hello world!"))
        self.add_action_to_main_menu("fit", self.fit_window.show)
        self.add_action_to_main_menu("load", lambda : moudleHandler.load_model())
        self.add_action_to_main_menu("save", lambda : moudleHandler.save_model())