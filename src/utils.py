import os
import win32com.client

def create_folder_shortcut(folder_path, shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = folder_path
    shortcut.Save()