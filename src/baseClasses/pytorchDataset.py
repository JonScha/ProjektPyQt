import pandas as pd
import torch
from torch.utils.data import Dataset
from dataSetFrame import DataSetFrame


class CustomDataset(Dataset):
    def __init__(self, dataframe : DataSetFrame):
        self.dataframe = dataframe
        self.main_frame = self.dataframe.get_main_frame()
        self.dataframe.mark_x_data(["feature1"])
        self.dataframe.mark_y_data(["feature2"])
        self.x_data, self.y_data = self.dataframe.get_raw_data_split()

    def __len__(self):
        return len(self.main_frame)


    # returns a sample for the training loop
    def __getitem__(self, idx):
        features = self.x_data.iloc[idx].values
        target = self.y_data.iloc[idx]
        return torch.tensor(features, dtype=torch.float), torch.tensor(target, dtype=torch.float)