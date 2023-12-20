from Windows.baseClasses import BaseColumnWindow
from Windows.baseClasses import BaseSimplePlugin
# from main import MainWindow


class testWindow(BaseColumnWindow):

    def __init__(self, main_window, width=700, height=550):
        super().__init__(main_window, width, height)

        self.add_entry("Hey", "es geht!")
        self.function = self.func
        self.add_ok_button()

        

    def func(self,col_idx, Hey):

        print("Funktion ausgelöst!!!")
        print(Hey)
        column_name = self.main_data_set.get_column_name_by_idx(col_idx)
        self.main_data_set.get_main_frame()[column_name] = self.main_data_set.get_main_frame()[column_name] +3

        self.data_viewer.update()
        


class testWindow2(BaseSimplePlugin):


    def __init__(self, main_window):
        super().__init__(main_window)
        self.function = self.func


    def func(self,col_idx):

        print("Funktion ausgelöst!!!")
        column_name = self.main_data_set.get_column_name_by_idx(col_idx)
        self.main_data_set.get_main_frame()[column_name] = self.main_data_set.get_main_frame()[column_name] +3

        self.data_viewer.update()