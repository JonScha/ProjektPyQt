from torch.nn import Module
from torch import save
import torch
import sys
from PySide6.QtWidgets import QFileDialog, QApplication

class torchModuleAdapter(Module):


    def __init__(self) -> None:
        super().__init__()


    def forward(self, x):
        # Hier definieren Sie, wie die Eingabe durch das Netzwerk propagiert wird
        return x
        raise NotImplementedError("forward function from torchModuleAdapter not implemented!")



    def save_model(self):
        path, _ = QFileDialog.getOpenFileName()
        save(self, path)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = torchModuleAdapter()
    input_data = torch.randn(1, 3, 64, 64)
    output = model(input_data)


    model.save_model()

    print(output)

    sys.exit(app)
