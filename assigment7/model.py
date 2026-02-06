class Model:
    def __init__(self):
        self.expression = ""

    def append_number(self, number):
        self.expression += number

    def append_operator(self, operator):
        if self.expression and self.expression[-1] in ['+', '-', '*', '/']:
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator

    def calculate_result(self):
        try:
            if '/0' in self.expression:
                return f"{self.expression}=undefined"
            else:
                result = eval(self.expression)
                return f"{self.expression}={result}"
        except Exception:
            return "Error"

    def clear_display(self):
        self.expression = ""

    def change_sign(self):
        if self.expression and self.expression[0] == '-':
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression

    def delete_number(self):
        self.expression = self.expression[:-1]

    def get_expression(self):
        return self.expression