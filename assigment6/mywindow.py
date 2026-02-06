from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication
from bmi import Ui_MainWindow


class BMIApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_bmi)
        self.pushButton_2.clicked.connect(self.calculate)
        self.actionExti.triggered.connect(QApplication.instance().quit)
        self.actionClear.triggered.connect(self.clear_fields)
        self.actionInformation_2.triggered.connect(self.show_information)
        self.actionSave.triggered.connect(self.save_file)


    def calculate_bmi(self):
        try:
            height = float(self.line2.text())
            weight = float(self.line1.text())
            selected_box = self.comboBox.currentIndex()

            if selected_box == 1:
                height = height * 0.3048
            else:
                height = height / 100

            bmi = round((weight / (height ** 2)), 1)
            self.update_label(bmi)
            self.output.setText(str(bmi))

        except ValueError:
            self.output.setText("Invalid Input")

    def calculate(self):
        try:
            metric = float(self.lineEdit.text())
            metric = round((metric / 100 * 3.28084), 5)
            self.output2.setText(str(metric))
        except ValueError:
            self.output2.setText("Invalid Input")

    def update_label(self, bmi):
        base_style = "border-radius: 20px; background-color: lightgray; padding: 5px; background-color: rgba(18, 214, 255, 100);"
        if bmi < 18.5:
            self.output.setText("Underweight")
            self.output.setStyleSheet(base_style + " background-color: rgb(255, 212, 121);;")
        elif 18.5 <= bmi < 25.0:
            self.output.setText("Normal weight")
            self.output.setStyleSheet(base_style + " background-color: green;")
        elif 25.0 <= bmi < 30.0:
            self.output.setText("Overweight")
            self.output.setStyleSheet(base_style + " background-color: rgb(255, 80, 0);")
        else:
            self.output.setText("Obese")
            self.output.setStyleSheet(base_style + " background-color: red;")

    def clear_fields(self):
        self.line1.clear()
        self.line2.clear()
        self.lineEdit.clear()
        self.output.setText("")
        self.output2.setText("")

    def show_information(self):
        info_text = (
            "This is a BMI calculator application.\n\n"
            "To use the BMI calculator:\n"
            "1. Enter your weight in kilograms in the 'Weight' field.\n"
            "2. Enter your height in centimeters in the 'Height' field.\n"
            "3. Select the unit of measurement for height (Metric or Feet).\n"
            "4. Click the 'Click Me' button to calculate your BMI.\n"
            "5. The result will be displayed in the 'Your BMI' section.\n\n"
            "To convert metric to feet:\n"
            "1. Enter the value in centimeters in the input field.\n"
            "2. Click the button next to the input field.\n"
            "3. The result will be displayed in the output field."
        )
        QMessageBox.information(self, "Information", info_text)

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_name[0]:
            with open(file_name[0], "w") as file:
                file.write(self.output.text())
                file.write("\n")
                file.write(self.output2.text())
                file.write("\n")