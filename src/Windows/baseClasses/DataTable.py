from PySide6.QtWidgets import QTableView, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QAbstractTableModel
from typing import TYPE_CHECKING
import pandas as pd


from baseClasses.dataSetFrame import DataSetFrame

class DataFrameTableView(QTableView):
    def __init__(self, main_frame : DataSetFrame):
        super().__init__()
        self.main_set = main_frame
        self.df = main_frame.get_main_frame()
        self.setModel(self.createTableModel(self.main_set))
        self.setSortingEnabled(True)
    
    def createTableModel(self, df):
        model = DataFrameTableModel(df)
        return model
    
    def updateTable(self):
        self.df = self.main_set.get_main_frame()
        self.model().updateData(self.df)

class DataFrameTableModel(QAbstractTableModel):
    def __init__(self, df : "DataSetFrame"):
        super().__init__()
        self.dataFrame = df.get_main_frame()

    def rowCount(self, parent=None):
        return len(self.dataFrame)

    def columnCount(self, parent=None):
        return len(self.dataFrame.columns)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self.dataFrame.iloc[index.row(), index.column()])
        return None  # Returning Python object directly

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.dataFrame.columns[section])
            if orientation == Qt.Vertical:
                return str(self.dataFrame.index[section])
        return None  # Returning Python object directly
    def updateData(self, new_df):
        self.beginResetModel()
        self.dataFrame = new_df
        self.endResetModel()

def update_data():
    # Hier könnten Sie Ihren DataFrame aktualisieren
    # Zum Beispiel: df = pd.read_csv('neue_daten.csv')
    # Hier verwenden wir ein Beispiel für die Aktualisierung der Daten
    data = {
        'Name': ['Eve', 'Frank'],
        'Alter': [28, 45],
        'Stadt': ['Hannover', 'Stuttgart']
    }
    df = pd.DataFrame(data)
    table_view.df = df
    table_view.updateTable()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setGeometry(100, 100, 800, 600)
    main_window.setWindowTitle('Tabellendarstellung mit PySide6')

    # Daten aus einem DataFrame erstellen (Beispiel)
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Alter': [25, 30, 35, 40],
        'Stadt': ['Berlin', 'Hamburg', 'München', 'Köln']
    }
    df = DataSetFrame()
    df.set_main_frame(data)

    table_view = DataFrameTableView(df)
    main_window.setCentralWidget(table_view)

    update_button = QPushButton("Daten aktualisieren")
    update_button.clicked.connect(update_data)

    widget = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(table_view)
    layout.addWidget(update_button)
    widget.setLayout(layout)

    main_window.setCentralWidget(widget)

    main_window.show()
    sys.exit(app.exec_())
