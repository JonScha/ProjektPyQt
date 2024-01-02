import importlib
import inspect
import os
import sys
import glob
import re

from typing import TYPE_CHECKING
from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
from Windows.baseClasses import BaseColumnWindow, BaseColumnResultWindow
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

        self.plugin_types = [BaseColumnWindow, BaseSimplePlugin, BaseColumnResultWindow]
        sys.path.append(os.path.abspath(self.plugin_folder))

    def lade_python_dateien(self):
        # Stelle sicher, dass der angegebene Pfad ein gültiger Ordner ist
        if not os.path.isdir(self.plugin_folder):
            print(f"{self.plugin_folder} ist kein gültiger Ordnerpfad.")
            return

        # Verwende die glob-Funktion, um alle Python-Dateien im Ordner zu finden
        python_dateien = glob.glob(os.path.join(self.plugin_folder, '*.py'))

        print("Dateien: ", python_dateien)

        # Durchlaufe jede gefundene Python-Datei
        for dateipfad in python_dateien:
            try:
                modul_name = os.path.splitext(os.path.basename(dateipfad))[0]
                modul = __import__(modul_name)

                # Durchsuche das Modul nach Klassen, die von der Basisklasse abgeleitet sind
                for name, obj in inspect.getmembers(modul):
                    if inspect.isclass(obj) and self.__check_plugin_type(obj) and obj not in self.plugin_types:
                        print(f"class {name} from {dateipfad} imported.")
                        object = obj(self.main_window)
                        object.initialize()

            except Exception as e:
                print(f"error whiel loading module: {modul_name} from file {dateipfad}: {str(e)}")



    def __check_plugin_type(self, cls):
        """
            returns true if the a class is a valid plugin type
        """
        for plug_type in self.plugin_types:
            if(issubclass(cls, plug_type)):
                return True
        return False
       