from PySide6.QtWidgets import QApplication
from src.mainwindow import MainWindow
app = QApplication()

window = MainWindow()
window.show()

app.exec()