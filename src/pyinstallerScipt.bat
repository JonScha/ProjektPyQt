@echo off

rem Setze den Pfad zur conda-Aktivierungsdatei
set conda_activate=conda activate

rem Setze den Namen der conda-Umgebung
set conda_env="py310"

rem Überprüfe, ob ein Dateipfad als Parameter übergeben wurde
if "%1"=="" (
    echo Bitte gib den Dateipfad zur Hauptdatei als Parameter an.
    exit /b 1
)

rem Aktiviere die conda-Umgebung
call %conda_activate% "py310"

rem Führe PyInstaller aus
pyinstaller --onedir --hidden-import _internal/Plugins.standardPlugins.py --add-data ./src/_internal/Plugins:./Plugins --add-data ./src/_internal/standardPlugins.py:./Plugins %1

rem Weitere Befehle hier...

exit /b 0
