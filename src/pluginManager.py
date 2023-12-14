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

            
            #classes = [cls_name for cls_name, cls_obj in inspect.getmembers(module) if inspect.isclass(cls_obj)]

            import_directory = f'{self.plugin_folder}.{plugin_file}'
            print(import_directory)
            module = importlib.import_module(plugin_file, import_directory)
            print(module)
            # 
            #cls = getattr(module, "" )


    def importiere_module_und_klassen_aus_ordner(self):
        dateien = [f for f in os.listdir(self.plugin_folder) if f.endswith(".py")]

        for datei in dateien:
            modulname = os.path.splitext(datei)[0]
            modulpfad = os.path.join(self.plugin_folder, datei)
            
            modul = importlib.import_module(f"{self.plugin_folder}.{modulname}")

            for name in dir(modul):
                objekt = getattr(modul, name)
                if inspect.isclass(objekt) and issubclass(objekt,BaseColumnWindow) and objekt != BaseColumnWindow:
                    print(f"Importiere Klasse {name} aus Modul {modulname}")
                    self.plugins.append(objekt)
                    objekt(self.main_window)

# Beispielaufruf
# mein_modulordner = "dein/ordnerpfad"
# importiere_module_und_klassen_aus_ordner(mein_modulordner)
