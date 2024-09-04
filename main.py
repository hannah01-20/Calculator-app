from PySide6.QtWidgets import QApplication
from src.mainwindow import MainWindow
app = QApplication()

window = MainWindow()
with open("src/styles.qss", "r") as _styles:
    app.setStyleSheet(_styles.read())
window.show()

app.exec()