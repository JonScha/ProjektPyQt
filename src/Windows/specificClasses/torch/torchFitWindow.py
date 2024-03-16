from Windows.baseClasses import BaseFunctionWindow
from typing import TYPE_CHECKING
from baseClasses import torchModuleHandler

if TYPE_CHECKING:
    from main import MainWindow


class torchFitWindow(BaseFunctionWindow):


    def __init__(self, main_window: "MainWindow", torchHandler, has_2_datasets=False, width=700, height=550):
        super().__init__(main_window, has_2_datasets, width, height)


        self.torchHandler : torchModuleHandler = torchHandler

        self.add_entry("epochs")
        self.add_dropdown("loss_function", self.torchHandler.loss_dict.keys())
        self.add_dropdown("optimizer", self.torchHandler.optimizers_dict.keys())
        self.add_button("load button", self.torchHandler.load_model)
        self.function = self.func
        self.add_function_button()


    def func(self, loss_function, epochs, optimizer):
        self.torchHandler.fit(epochs, loss_function, optimizer)
        
