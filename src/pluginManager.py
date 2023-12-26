import importlib
import inspect
import os
import sys
from typing import TYPE_CHECKING
from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
from Windows.baseClasses import BaseColumnWindow
from Windows.baseClasses.BaseSimplePlugin import BaseSimplePlugin
if TYPE_CHECKING:
    from main import MainWindow
    
    

class PluginManager:
    def __init__(self, plugin_folder, main_window : "MainWindow"):
        self.plugin_folder = plugin_folder
        self.plugins = []
        self.main_window = main_window
        self.data_viewer = self.main_window.data_viewer
        self.plugin_files = []

        self.plugin_types = [BaseColumnWindow, BaseSimplePlugin]

    def import_plugins(self):
        """
            imports all plugins in the ./Plugins directory 
        """
        dateien = [f for f in os.listdir(self.plugin_folder) if f.endswith(".py")]

        for datei in dateien:
            module_name = os.path.splitext(datei)[0]
            modulpfad = os.path.join(self.plugin_folder, datei)
            
            modul = importlib.import_module(f"{self.plugin_folder}.{module_name}")

            for class_name in dir(modul):
                objekt = getattr(modul, class_name)
                if inspect.isclass(objekt) and self.__check_plugin_type(objekt) and objekt not in self.plugin_types:
                    print(f"import class {class_name} from module {module_name}")
                    self.plugins.append(objekt)
                    objekt(self.main_window).initialize()

    def __check_plugin_type(self, cls):
        """
            returns true if the a class is a valid plugin type
        """
        for plug_type in self.plugin_types:
            if(issubclass(cls, plug_type)):
                return True
        return False
       