# PyQt6 Calculator

This is a simple calculator application built using PyQt6. The application supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Classes and Methods

### `Model` Class
- **Purpose**: This class handles the calculator logic.
- **Methods**:
  - `__init__(self)`: Initializes the model with an empty expression.
  - `append_number(self, number)`: Appends a number to the expression.
  - `append_operator(self, operator)`: Appends an operator to the expression.
  - `calculate_result(self)`: Evaluates the expression and returns the result.
  - `clear_display(self)`: Clears the expression.
  - `change_sign(self)`: Changes the sign of the current number.
  - `delete_number(self)`: Deletes the last character from the expression.
  - `get_expression(self)`: Returns the current expression.

### `Controller` Class
- **Purpose**: This class represents the main window of the calculator application and handles the UI.
- **Methods**:
  - `__init__(self)`: Initializes the calculator window, sets up the UI, and connects the buttons to their respective functions.
  - `initUI(self)`: Connects the buttons to their respective functions.
  - `append_number(self, number)`: Appends a number to the display.
  - `append_operator(self, operator)`: Appends an operator to the display.
  - `calculate_result(self)`: Evaluates the expression and displays the result.
  - `clear_display(self)`: Clears the display.
  - `change_sign(self)`: Changes the sign of the current number.
  - `delete_number(self)`: Deletes the last character from the display.

## How to Run

1. Ensure you have Python and PyQt6 installed. You can install PyQt6 using pip:
   ```sh
   pip install PyQt6
    ```
2. Run the `main.py` file:
    ```sh
   python shapes_classes.py
    ```

## Sample Input/Output
### Example 1
**Input**: 5 + 3 = **Output**: 8

### Example 2
**Input**: 10 / 2 = **Output**: 5

### Example 3
**Input**: 7*6 = **Output**: 42

### Example 4
**Input**: 10 / 0 = **Output**: undefined

