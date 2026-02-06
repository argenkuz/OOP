from PyQt6.QtWidgets import QMainWindow
from calculator import Ui_MainWindow
from model import Model

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = Model()
        self.initUI()

    def initUI(self):
        self.pushButton_0.clicked.connect(lambda: self.append_number('0'))
        self.pushButton_1.clicked.connect(lambda: self.append_number('1'))
        self.pushButton_2.clicked.connect(lambda: self.append_number('2'))
        self.pushButton_3.clicked.connect(lambda: self.append_number('3'))
        self.pushButton_4.clicked.connect(lambda: self.append_number('4'))
        self.pushButton_5.clicked.connect(lambda: self.append_number('5'))
        self.pushButton_6.clicked.connect(lambda: self.append_number('6'))
        self.pushButton_7.clicked.connect(lambda: self.append_number('7'))
        self.pushButton_8.clicked.connect(lambda: self.append_number('8'))
        self.pushButton_9.clicked.connect(lambda: self.append_number('9'))
        self.pushButton_dot.clicked.connect(lambda: self.append_number('.'))
        self.pushButton_plus.clicked.connect(lambda: self.append_operator('+'))
        self.pushButton_minus.clicked.connect(lambda: self.append_operator('-'))
        self.pushButton_multiple.clicked.connect(lambda: self.append_operator('*'))
        self.pushButton_division.clicked.connect(lambda: self.append_operator('/'))
        self.pushButton_equal.clicked.connect(self.calculate_result)
        self.pushButton_ac.clicked.connect(self.clear_display)
        self.pushButton_pm.clicked.connect(self.change_sign)
        self.pushButton_percentage.clicked.connect(self.delete_number)

    def append_number(self, number):
        self.model.append_number(number)
        self.lineEdit.setText(self.model.get_expression())

    def append_operator(self, operator):
        self.model.append_operator(operator)
        self.lineEdit.setText(self.model.get_expression())

    def calculate_result(self):
        result = self.model.calculate_result()
        self.lineEdit.setText(result)

    def clear_display(self):
        self.model.clear_display()
        self.lineEdit.clear()

    def change_sign(self):
        self.model.change_sign()
        self.lineEdit.setText(self.model.get_expression())

    def delete_number(self):
        self.model.delete_number()
        self.lineEdit.setText(self.model.get_expression())