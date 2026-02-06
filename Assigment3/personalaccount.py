from amount import Amount

class PersonalAccount():
    def __init__(self, account_number:int, account_holder:str, balance:float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        self.transaction = []

    def deposit(self, amount:float):
        if amount > 0:
            deposit_amount = Amount(amount, "DEPOSIT")
            self.transaction.append(deposit_amount)
            self.__balance += amount
        else:
            print("Deposit amount cannot be negative")

    def withdraw(self, amount:float):
        if 0 < amount < self.__balance:
            withdraw_amount = Amount(amount, "WITHDRAW")
            self.transaction.append(withdraw_amount)
            self.__balance -= amount

    def print_transaction_history(self):
        for transaction in self.transaction:
            print(transaction)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Balance: {self.__balance} \nAccount number: {self.account_number}\nAccount holder: {self.account_holder}"

    def __add__(self, amount):
        if amount > 0:
            self.__balance += amount

        else:
            print("Amount amount cannot be negative")

    def __sub__(self, amount):
        if amount > 0:
            self.__balance -= amount

        else:
            print("Amount amount cannot be negative")



