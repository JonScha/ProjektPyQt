from PySide6.QtWidgets import QTableView, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QAbstractTableModel
from Windows.baseClasses import DataFrameTableView
from baseClasses import DataSetFrame
import pandas as pd

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
    df = pd.DataFrame(data)
    df2 = DataSetFrame()
    df2.set_main_frame(df)
    table_view = DataFrameTableView(df2)
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