from PySide6.QtWidgets import QMainWindow, QMenu
from baseMenu import BaseMenu
from baseClasses import DataSetFrame

class FileMenu(BaseMenu):

    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)

        main_menu = self.add_main_menu("File")
        # self.menu : QMenu = self.add_sub_menu("import")

        self.add_action_to_sub_menu(main_menu, "import", )
        
        