# BMIApp

## Overview
BMIApp is a simple Python application that calculates the Body Mass Index (BMI) based on user input for weight and height. The application uses PyQt6 for the graphical user interface.

## Classes and Methods

### `BMIApp`
- **Purpose:** Main application window class that inherits from `QMainWindow` and `Ui_MainWindow`.
- **Methods:**
  - `__init__(self)`: Initializes the main window and connects the button click to the `calculate_bmi` method.
  - `calculate_bmi(self)`: Calculates the BMI based on the input weight and height, and displays the result.
  - `update_label(self, bmi)`: Updates the label based on the BMI value.
  - `clear_fields(self)`: Clears all input fields and output labels.
  - `show_information(self)`: Displays information about how to use the application.
  - `save_file(self)`: Saves the BMI and conversion results to a file.
    
## How to Run the Code
### 1.Run the main script:
```sh
   python shapes_classes.py
```
### 2.Enter the weight and height in the respective fields.
### 3.Click the "Click Me" button to calculate the BMI.
### 4.To convert metric to feet, enter the value in centimeters in the input field and click the button next to the input field.
## Sample Input/Output

### Example 1
- **Input:**
  - Weight: 70 kg
  - Height: 175 cm
- **Output:**
  - BMI: 22.9

### Example 2
- **Input:**
  - Weight: 85 kg
  - Height: 169 cm
- **Output:**
  - BMI: 29.8

## Screenshots

### Example 1
![Снимок экрана 2025-03-04 в 15.46.42.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-04%20%D0%B2%2015.46.42.png)
### Example 2
![Снимок экрана 2025-03-04 в 15.49.07.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-04%20%D0%B2%2015.49.07.png)

Features
- Calculate BMI based on weight and height.
- Convert height from metric to feet.
- Clear input fields and output labels.
- Display information about how to use the application.
- Save BMI and conversion results to a file.