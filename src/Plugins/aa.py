from Windows.baseClasses import BaseColumnWindow
# from main import MainWindow


class testWindow(BaseColumnWindow):

    def __init__(self, main_window, width=700, height=550):
        super().__init__(main_window, width, height)

        self.add_entry("Hey", "es geht!")
        self.function = self.func
        self.add_ok_button()

        self.add_to_data_tabe("heyeqqe")
        

    def func(self,col, Hey):

        print("Funktion ausgelöst!!!")
        print(Hey)