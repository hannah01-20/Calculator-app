from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout, QGroupBox, QSizePolicy
from PySide6.QtCore import Qt

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.lineEdit = QLineEdit("")
        self.lineEdit.returnPressed.connect(self.calculate)
        self.lineEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        groupButtons = QGroupBox(" N A N A C O D E ")
        groupButtons.setAlignment(Qt.AlignHCenter)

        num1 = QPushButton("1")
        num1.clicked.connect(lambda : self.insertValue("1"))
        num1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num2 = QPushButton("2")
        num2.clicked.connect(lambda : self.insertValue("2"))
        num2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num3 = QPushButton("3")
        num3.clicked.connect(lambda : self.insertValue("3"))
        num3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num4 = QPushButton("4")
        num4.clicked.connect(lambda : self.insertValue("4"))
        num4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num5 = QPushButton("5")
        num5.clicked.connect(lambda : self.insertValue("5"))
        num5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num6 = QPushButton("6")
        num6.clicked.connect(lambda : self.insertValue("6"))
        num6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num7 = QPushButton("7")
        num7.clicked.connect(lambda : self.insertValue("7"))
        num7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num8 = QPushButton("8")
        num8.clicked.connect(lambda : self.insertValue("8"))
        num8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num9 = QPushButton("9")
        num9.clicked.connect(lambda : self.insertValue("9"))
        num9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        num0 = QPushButton("0")
        num0.clicked.connect(lambda : self.insertValue("0"))
        num0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        decimal = QPushButton(".")
        decimal.clicked.connect(lambda : self.insertValue("."))
        decimal.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        decimal.setObjectName("redButton")
        plus = QPushButton("+")
        plus.clicked.connect(lambda : self.insertValue("+"))
        plus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        minus = QPushButton("-")
        minus.clicked.connect(lambda : self.insertValue("-"))
        minus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        times = QPushButton("*")
        times.clicked.connect(lambda : self.insertValue("*"))
        times.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        divide = QPushButton("/")
        divide.clicked.connect(lambda : self.insertValue("/"))
        divide.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        clear = QPushButton("C")
        clear.clicked.connect(lambda : self.lineEdit.clear())
        clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        clear.setObjectName("redButton")

        delete = QPushButton("Del")
        delete.clicked.connect(lambda : self.lineEdit.setText(self.lineEdit.text()[:-1]))
        delete.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        delete.setObjectName("redButton")

        enter = QPushButton("=")
        enter.clicked.connect(self.calculate)
        enter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        enter.setObjectName("redButton")


        grid = QGridLayout()
        grid.addWidget(clear, 0, 0)
        grid.addWidget(plus, 0, 1)
        grid.addWidget(minus, 0, 2)
        grid.addWidget(delete, 0, 3)
        grid.addWidget(times, 1, 3)
        grid.addWidget(divide, 2, 3)
        grid.addWidget(enter, 3, 3, 2, 1)
        grid.addWidget(decimal, 4, 0)

        grid.addWidget(num7, 1, 0)
        grid.addWidget(num8, 1, 1)
        grid.addWidget(num9, 1, 2)
        grid.addWidget(num4, 2, 0)
        grid.addWidget(num5, 2, 1)
        grid.addWidget(num6, 2, 2)
        grid.addWidget(num1, 3, 0)
        grid.addWidget(num2, 3, 1)
        grid.addWidget(num3, 3, 2)
        grid.addWidget(num0, 4, 1)

        groupButtons.setLayout(grid)


        # Applying layouts on components

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(groupButtons)

        self.setLayout(layout)


    def insertValue(self, x):
        operands = ["+", "-", "*", "/"]
        currentValue = self.lineEdit.text()

        if currentValue == "":
            for operand in operands:
                if x == operand:
                    return "Not Allowed"
            self.lineEdit.setText(x)
        
        if currentValue == "0":
            self.lineEdit.setText(x)

        for operand in operands:
            if x == operand:
                for operand in operands:
                    if operand == currentValue[-1]:
                        return "Not Allowed"
        
        self.lineEdit.setText(currentValue + x)

    def calculate(self):
        operands = ["+", "-", "*", "/"]
        try:
            for operand in operands:
                if self.lineEdit.text()[-1] == operand:
                    self.lineEdit.clear()
                    return "Missing value"
        except IndexError as e:
            print(e)
            return "There is no to calculate."
        
        try:
            total = eval(self.lineEdit.text())
            self.lineEdit.setText(str(total))
        except ArithmeticError as e:
            self.lineEdit.setText("")