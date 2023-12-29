from PySide6 import QtWidgets
from PySide6.QtCore import Qt

class ResultWindow(QtWidgets.QWidget):
    def __init__(self, main_window, results, results_names=None, width=400, height=500):
        super().__init__()
        self.main_window = main_window
        self.results = results
        self.results_names = results_names
        self.width = width
        self.height = height
        self.num_columns = 3
        self.row = 0
        self.column = 0

        self.setWindowTitle("Result Window")
        self.setGeometry(100, 100, width, height)

        layout = QtWidgets.QVBoxLayout(self)
        #layout = QtWidgets.QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addStretch(1)

        self.setMaximumSize(self.width, self.height)
        self.create_labels()
        self.__center()
        self.add_button()

    def create_labels(self):
        if isinstance(self.results, tuple):
            self.create_labels_from_tuple()
        else:
            self.create_labels_from_object()

    def create_labels_from_object(self):
        members = self.results._asdict()
        for key, value in members.items():
            self.check_row_columns()
            label = QtWidgets.QLabel(f"{key}: {value}", self)
            label.setFixedSize(150, 40)
            self.layout().addWidget(label)

            self.column += 1

    def create_labels_from_tuple(self):
        if self.results_names is None:
            raise ValueError("Tuple results need provided output denotation")

        for key, value in zip(self.results_names, self.results):
            self.check_row_columns()
            label = QtWidgets.QLabel(f"{key}: {value}", self)
            label.setFixedSize(150, 40)
            self.layout().addWidget(label)

            self.column += 1


    def check_row_columns(self):
        if self.column % self.num_columns == 0:
            self.row += 1
            self.column = 0

    def add_button(self):
        self.check_row_columns()
        button = QtWidgets.QPushButton("OK", self)
        button.clicked.connect(self.button_fun)
        self.layout().addWidget(button)

    def __center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button_fun(self):
        self.close()
