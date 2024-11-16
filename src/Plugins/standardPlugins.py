from Windows.baseClasses import BaseColumnWindow, BaseColumnResultWindow
from Windows.baseClasses.BaseSimplePlugin import BaseSimplePlugin
from main import MainWindow
# from main import MainWindow

"""
    standard Plugins for data engineering 

"""


class testWindow(BaseColumnWindow):

    def __init__(self, main_window, width=700, height=550):
        super().__init__(main_window, width, height)

        self.add_entry("Hey", "es geht!")
        self.function = self.func2
        self.add_ok_button()

        

    def func2(self,col_idx, Hey):

        print("Funktion ausgelöst!!! BaseColumnWindow!")
        print(Hey)
        column_name = self.main_data_set.get_column_name_by_idx(col_idx)
        self.main_data_set.get_main_frame()[column_name] = self.main_data_set.get_main_frame()[column_name] +3

        self.data_viewer.update()
        


# class testWindow2(BaseSimplePlugin):


#     def __init__(self, main_window):
#         super().__init__(main_window)
#         self.function = self.func

#     def func(self,col_idx):

#         print("Funktion ausgelöst!!! SimplePlugin")
#         self.set_name("hans")
#         column_name = self.main_data_set.get_column_name_by_idx(col_idx)
#         self.main_data_set.get_main_frame()[column_name] = self.main_data_set.get_main_frame()[column_name] +3

#         self.data_viewer.update()

        


class Binarize(BaseColumnWindow):


    def __init__(self, main_window: MainWindow, width=700, height=550):
        super().__init__(main_window, width, height)
        self.function = self.func
        self.add_entry("threshold")
        self.set_name("binarize")
        self.add_ok_button()

    def func(self,col_idx : int, threshold : float):
        column_name = self.main_data_set.get_column_name_by_idx(col_idx)
        self.main_data_set.get_main_frame()[column_name] = (self.main_data_set.get_main_frame()[column_name] 
                                                            <= float(threshold)).astype(int)


        self.data_viewer.update()

class FilterTreshhold(BaseColumnWindow):

    def __init__(self, main_window: MainWindow, width=700, height=550):
        super().__init__(main_window, width, height)

        self.function = self.func
        self.set_name("filter_threshold")
        self.add_entry("threshold", "filter all values which are > threshold")
        self.add_ok_button()

    
    def func(self, col_idx, threshold):
        df = self.main_data_set.get_main_frame()
        column_name = self.main_data_set.get_column_name_by_idx(col_idx)
        df = df[df[column_name] <= float(threshold)]
        self.main_data_set.set_main_frame(df)
        self.data_viewer.update()

class TestBaseColumnResultWindow(BaseColumnResultWindow):

    def __init__(self, main_window: MainWindow, width=700, height=550):
        super().__init__(main_window, width, height)

        self.function = self.func
        self.set_name("filter_threshold_return")
        self.add_entry("threshold")
        self.result_names = ["1", "2"]
        self.add_ok_button()

    def func(self, col_idx, threshold):
        df = self.main_data_set.get_main_frame()
        column_name = self.main_data_set.get_column_name_by_idx(col_idx)
        df = df[df[column_name] <= float(threshold)]
        self.main_data_set.set_main_frame(df)
        self.data_viewer.update()

        return 10,20
    

class SelectXValues(BaseSimplePlugin):

    def __init__(self, main_window: MainWindow):
        super().__init__(main_window)
        self.set_name("mark as x data")
        self.function = self.func


    def func(self, col_idx):
        self.main_data_set.mark_as_x_column(col_idx)
        self.data_viewer.set_column_background_color(col_idx, "red")

class SelectYValues(BaseSimplePlugin):

    def __init__(self, main_window: MainWindow):
        super().__init__(main_window)
        self.set_name("mark as y data")
        self.function = self.func


    def func(self, col_idx):
        self.main_data_set.mark_as_y_column(col_idx)
        self.data_viewer.set_column_background_color(col_idx, "blue")