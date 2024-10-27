import pandas as pd
import numpy as np
from typing import Tuple, List, Any
import os
from sklearn.preprocessing import binarize
from PySide6.QtWidgets import QFileDialog
class DataSetFrame:
    """
        Main class to work with datasets fetched from SQL Databases

    Attributes
    ----------
        main_frame : pd.DataFrame
                contains all the data from the SQL query

        x_set : pd.DataFrame
                contains all x-Values for training the NN
        y_set : pd.DataFrame
                contrains all y-Values for training the NN

    Methods
    -------
        replace_all_null_with_values(value)
            replaces all NULL values with value
        filter_all_null_values()
            Drops all rows with atleast 1 NULL value
        head()
            shows first 5 values in the main_frame
        marks_x_data()
            marks all input data for the NN
        marks_y_data()
            marks all output data for the NN
        get_data_split()
            returns the marked x_data and y_data
        get_column_names():
            returns the names of the colums as a list of strings
        get_num_rows()
            returns the number of rows
        get_iloc_row()
            returns the row of an in
        get_row()
            returns the row of a specified index
        get_loc_row()
            returns the row where the index matches
        get_numpy_array()
            returns the DataFrame as numpy array 

    """

    def __init__(self, main_frame = pd.DataFrame()) -> None:
        self.main_frame : pd.DataFrame = main_frame
        self.x_set = pd.DataFrame
        self.y_set = pd.DataFrame
        self.x_marked = []
        self.y_marked = []
        self.backup_frame : pd.DataFrame = main_frame

    def replace_all_null_with_values(self, value : Any, rows : List[str] = []) -> None:
        """
            Replaces all NULL (None) values with given value.
        """
        if len(rows) == 0:
            self.main_frame = self.main_frame.fillna(value=value)
        else:
            self.main_frame[rows] = self.main_frame[rows].fillna(value=value)

    def filter_all_null_values(self) -> None:
        """
            Drops every row, where is atleast 1 NULL (None) value.
        """
        self.main_frame = self.main_frame.dropna(0)


    def mark_as_x_column(self, column_idx : int):
        if column_idx in self.y_marked:
            self.y_marked.remove(column_idx)
        self.x_marked.append(self.get_column_name_by_idx(column_idx))
    
    def mark_as_y_column(self, column_idx : int):
        if column_idx in self.x_marked:
            self.x_marked.remove(column_idx)
        self.y_marked.append(self.get_column_name_by_idx(column_idx))

    def mark_x_data(self, list_of_x_values : List[str] ) -> None:
        """
            marks all columns as input for the NN
        """
        self.x_marked = list_of_x_values

    def mark_y_data(self, list_of_y_values : List[str]) -> None:
        """
            marks all colums as output for the NN
        """
        self.y_marked = list_of_y_values

    def set_main_frame(self, data_frame : pd.DataFrame):
        self.main_frame = data_frame

    def get_main_frame(self):
        return self.main_frame
  
    def get_raw_data_split(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
            returns x_values,y_values
        """
        self.x_set = self.main_frame[self.x_marked]
        self.y_set = self.main_frame[self.y_marked]
        return self.x_set, self.y_set

    def get_column_names(self) -> pd.DataFrame:
        return self.main_frame.columns
    
    def get_x_value(self):
        return self.main_frame[self.x_marked]

    def get_num_rows(self) -> int:
        return len(self.main_frame.index)

    def get_iloc_column(self, index : int) -> pd.Series:
        return self.main_frame.iloc[index]

    def get_row(self, index : int) -> pd.Series:
        return self.main_frame[index]

    def get_loc_column(self, index) -> pd.Series:
        return self.main_frame.loc[index]

    def get_numpy_array(self) -> pd.DataFrame:
        return self.main_frame.to_numpy()
    
    def __import_csv(self, file_path):
        self.main_frame = pd.read_csv(file_path) 
    
    def empty(self):
        tmp = self.main_frame.empty
        return tmp

    def __import_excel(self, file_path):
        self.main_frame = pd.read_excel(file_path)

    def set_headers(self, headers):
        self.main_frame.columns = headers 

    def get_data_shape(self):
        """
            returns the shape of the x data and the y data
        """
        return len(self.x_marked), len(self.y_marked)
    
    def get_x_marked_list(self):
        return self.x_marked
    def get_y_marked_list(self):
        return self.y_marked
    
    def get_data_frame(self) -> pd.DataFrame:
        return self.main_frame
    
    def calc_coeff_matrix(self):
        coeff_matrix = self.main_frame.cov()
        return coeff_matrix
    
    def get_column_name_by_idx(self, idx : int):
        return self.main_frame.columns[idx]
    
    def get_column_values(self, column : str):
        return self.main_frame[column]

    def normalize_column(self, column_idx : int):
        """
        Normalisiert eine Spalte in einem Pandas DataFrame auf den Bereich [0, 1] mithilfe der Min-Max-Normalisierung.
        
        Args:
            
            column_name (str): Der Name der zu normalisierenden Spalte.
        
        """
        column = self.get_column_name_by_idx(column_idx)

        # Überprüfe, ob die Spalte im DataFrame existiert
        if column not in self.main_frame.columns:
            raise ValueError(f"Die Spalte '{column}' existiert nicht im DataFrame.")
        
        # Min-Max-Normalisierung der Spalte
        min_val = self.main_frame[column].min()
        max_val = self.main_frame[column].max()
        
        self.main_frame[column] = (self.main_frame[column] - min_val) / (max_val - min_val)

    def reset_data_frame(self, column_idx : int):
        self.main_frame = self.backup_frame

    def save_to_file(self):
        
        path, _ = QFileDialog.getSaveFileName()
        filename, ending = os.path.splitext(path)

        if ending == ".csv":
            self.main_frame.to_csv(path, index=False)
        elif ending == ".xlsx":
            self.main_frame.to_excel(path, index=False)
        elif ending == "":
            return
        else:
            raise ValueError(f"given file type \"{ending}\" not supported!")
        
    def get_y_value(self):
        return self.main_frame[self.y_marked]
        
    def binare_transform(self, column_idx : int, threshold : float):
        column = self.get_column_name_by_idx(column_idx)
        self.main_frame[column] = binarize(self.main_frame[column], threshold, copy=False)

    def import_file(self):
        """
            Use this method to import csv or excel data
        """
        # filename, ending = os.path.splitext(file_path)
        path, _ = QFileDialog.getOpenFileName()
        filename, ending = os.path.splitext(path)
        if ending == ".csv":
            self.__import_csv(path)
        elif ending == ".xlsx":
            self.__import_excel(path)
        # empty filepath
        elif ending == "":
            return
        else:
            raise ValueError(f"given file type \"{ending}\" not supported!")





# df = DataSetFrame()
# df.import_csv("I:/ProjektPyQt/src/TestDateien/data.csv")


# df.mark_x_data(["x"])
# df.mark_y_data(["y"])


# print(df.get_x_value())
# print("\n")
# print(df.get_y_value())