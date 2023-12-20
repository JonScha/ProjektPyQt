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


if TYPE_CHECKING:
    from main import MainWindow
    

class PluginManager:
    def __init__(self, plugin_folder, main_window : "MainWindow"):
        self.plugin_folder = plugin_folder
        self.plugins = []
        self.main_window = main_window
        self.data_viewer = self.main_window.data_viewer
        self.plugin_files = []

        self.plugin_types = [BaseColumnWindow]


    def load_plugins(self):
        # To be able to execute the plugin they need to be locatable
 
        files : list[str] = os.listdir(self.plugin_folder)

        for file in files:
            if file.endswith(".py"):
                self.plugin_files.append(file)
        
        for plugin_file in self.plugin_files:
            import_directory = f'{self.plugin_folder}.{plugin_file}'
            print(import_directory)
            module = importlib.import_module(plugin_file, import_directory)
            print(module)



    def import_plugins(self):
        dateien = [f for f in os.listdir(self.plugin_folder) if f.endswith(".py")]

        for datei in dateien:
            module_name = os.path.splitext(datei)[0]
            modulpfad = os.path.join(self.plugin_folder, datei)
            
            modul = importlib.import_module(f"{self.plugin_folder}.{module_name}")

            for class_name in dir(modul):
                objekt = getattr(modul, class_name)
                if inspect.isclass(objekt) and issubclass(objekt,BaseColumnWindow) and objekt != BaseColumnWindow:
                    print(f"import class {class_name} from module {module_name}")
                    self.plugins.append(objekt)
                    objekt(self.main_window).initialize()
