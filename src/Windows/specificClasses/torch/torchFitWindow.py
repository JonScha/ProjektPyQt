from Windows.baseClasses import BaseFunctionWindow
from typing import TYPE_CHECKING
from baseClasses import torchModuleHandler

if TYPE_CHECKING:
    from main import MainWindow


class torchFitWindow(BaseFunctionWindow):


    def __init__(self, main_window: "MainWindow", has_2_datasets=False, width=700, height=550):
        super().__init__(main_window, has_2_datasets, width, height)


        self.torchHandler = torchModuleHandler(self.main_window, self.main_data_set)


        self.add_entry("epochs")

        self.add_dropdown("loss_function", self.torchHandler.loss_dict.keys())
        self.add_dropdown("optimizer", self.torchHandler.optimizers_dict.keys())
        self.function = self.func
        self.add_function_button()


    def func(self, loss_function, epochs, optimizer):
        self.torchHandler.fit(epochs, loss_function, optimizer)
        
