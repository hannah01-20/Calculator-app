from PySide6.QtWidgets import QMainWindow
from .widget import Widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 600)

        widget = Widget()

        self.setCentralWidget(widget)
        
        
