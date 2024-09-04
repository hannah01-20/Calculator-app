from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QGroupBox, QVBoxLayout, QGridLayout, QSizePolicy
from .widget import Widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 600)
        # Adding components

        widget = Widget()

        self.setCentralWidget(widget)
        
        
