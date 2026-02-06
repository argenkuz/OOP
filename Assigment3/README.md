# Personal Bank Account System

## Overview
This project uses Python to construct a basic personal bank account system. There are two primary classes in it:

- **Amount**: Indicates the amount of a transaction together with its type and timestamp.
- **PersonalAccount**:  that keeps track of deposits, withdrawals, and transaction history is represented by the **PersonalAccount**.

By enabling user input for deposits and withdrawals, the `main.py` program illustrates how to use these classes.

## Features
- Establish a private bank account.
- Make deposits and withdrawals.
- Keep a record of all transactions.
- Get the balance and account information.
- The `+` and `-` operators for deposits and withdrawals are overloaded.


## Class Structure
### `Amount` Class
- **Attributes:**
  - `amount (float)`: Transaction amount.
  - `timestamp (datetime)`: Transaction date and time.
  - `transaction_type (str)`: Transaction type ('DEPOSIT' or 'WITHDRAWAL').
- **Methods:**
  - `__init__(self, amount, timestamp, transaction_type)`: Initializes an Amount object.
  - `__str__(self)`: Returns a string representation of the transaction.

### `PersonalAccount` Class
- **Attributes:**
  - `account_number (int)`: Unique account identifier.
  - `account_holder (str)`: Name of the account holder.
  - `balance (float)`: Current balance.
  - `transactions (list)`: List of Amount objects.
- **Methods:**
  - `__init__(self, account_number, account_holder)`: Initializes an account with a zero balance.
  - `deposit(self, amount)`: Deposits money and updates transaction history.
  - `withdraw(self, amount)`: Withdraws money if the balance allows and updates transaction history.
  - `print_transaction_history(self)`: Displays all transactions.
  - `get_balance(self)`: Returns the current balance.
  - `get_account_number(self) / set_account_number(self, account_number)`: Get/set account number.
  - `get_account_holder(self) / set_account_holder(self, account_holder)`: Get/set account holder name.
  - `__str__(self)`: Returns a string representation of the account.
  - `__add__(self, amount)`: Overloads `+` operator to deposit money.
  - `__sub__(self, amount)`: Overloads `-` operator to withdraw money.




# **UML Class Diagram**


<img width="1091" alt="Снимок экрана 2025-02-11 в 11 03 45" src="https://github.com/user-attachments/assets/b640b6e0-3f83-4847-99a1-fef1de67ab87" />

