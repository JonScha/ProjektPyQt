from torch.nn import Module
from .pytorchDataset import CustomDataset
from .dataSetFrame import DataSetFrame
from typing import TYPE_CHECKING
import torch
import pandas as pd
import sys
import torch.optim as optim
from PySide6.QtWidgets import QFileDialog, QApplication
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F

if TYPE_CHECKING:
    from main import MainWindow
    
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # Fully connected layer 1
        self.fc2 = nn.Linear(hidden_size, output_size) # Fully connected layer 2

    def forward(self, x):
        x = F.relu(self.fc1(x))  # ReLU activation function for the first layer
        x = F.sigmoid(self.fc2(x))          # Output layer without activation function
        return x


class torchModuleHandler():


    def __init__(self,main_window, datasetframe : DataSetFrame, model : Module = torch.nn.Module()) -> None:

        self.main_window = main_window
        self.__model : Module = model

        self.__dataframe = datasetframe


        self.loss_dict = {
            "mean_squared_error": nn.MSELoss(),
            "mean_absolute_error": nn.L1Loss(),
            "binary_cross_entropy": nn.BCELoss(),
            "cross_entropy": nn.CrossEntropyLoss(),
            "poisson_nll": nn.PoissonNLLLoss(),
            "kldiv_loss": nn.KLDivLoss(),
            "smooth_l1_loss": nn.SmoothL1Loss(),
            # Weitere Verlustfunktionen können hier hinzugefügt werden
        }

        self.optimizers_dict = {
            "sgd": optim.SGD,
            "adam": optim.Adam,
            "adadelta": optim.Adadelta,
            "adagrad": optim.Adagrad,
            "rmsprop": optim.RMSprop,
            # Weitere Optimierer können hier hinzugefügt werden
        }


    def save_model(self):
        path, _ = QFileDialog.getSaveFileName(self.main_window)

        if path != "":
            torch.save(self.__model, path)

    def load_model(self):
        path, _ = QFileDialog.getOpenFileName(self.main_window)
        if path != "":
            self.__model = torch.load(path)
        

    def get_model(self) -> Module:
        return self.__model
    


    def fit(self,epochs : int, loss_function : str, optimizer : str):
        
        self.dataset = CustomDataset(self.__dataframe)
        loss_function  = self.loss_dict[loss_function]
        optimizer = self.optimizers_dict[optimizer]
        data_loader = DataLoader(self.dataset)

        opt : torch.optim.Optimizer = optimizer(self.__model.parameters(), lr = 0.01)

        for epoch in range(epochs):
            for i, data in enumerate(data_loader):

                inputs, labels = data 
                opt.zero_grad()

                outputs = self.__model(inputs)  # Vorwärtsdurchlauf
                loss : torch.nn.modules.loss._Loss = loss_function(outputs, labels)  # Berechnung der Verlustfunktion
                loss.backward()  # Rückwärtsdurchlauf (Berechnung der Gradienten)
                opt.step()  # Aktualisierung der Gewichte

            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

    def predict(self, input_data):
        return self.__model.forward(input_data)
     


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model_1 = SimpleNN(2,10,1)


    test_data = torch.randn(1, 10)

    data = {
    'feature1': [1, 2, 3, 4, 5,6,7,8,9,10],
    'feature2': [0, 1, 0, 1, 0,1,0,1,0,1],
    'target': [0, 1, 0, 1, 0,1,0,1,0,1]
    }   
    
    df = DataSetFrame(pd.DataFrame(data))
    df.mark_as_x_column(0)
    df.mark_as_x_column(1)
    df.mark_as_y_column(1)
    a = DataSetFrame()
    modelHandler = torchModuleHandler(df, model_1)
    modelHandler.fit(100, "mean_absolute_error", "adam")

    print("Ergebnis: " , modelHandler.predict(torch.FloatTensor([1,0])))
    print("Ergebnis: " , modelHandler.predict(torch.FloatTensor([2,1])))
    print("Ergebnis: " , modelHandler.predict(torch.FloatTensor([3,0])))
    print("Ergebnis: " , modelHandler.predict(torch.FloatTensor([4,1])))
    print("Ergebnis: " , modelHandler.predict(torch.FloatTensor([5,0])))
    print("Ergebnis: " , modelHandler.predict(torch.FloatTensor([160,1])))

    sys.exit(app)
