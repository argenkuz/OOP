Here is the `README.md` file with the requested documentation:

# User Management System

## Overview

This project is a simple user management system implemented in Python. It includes classes for managing users, validating user information, and performing various operations such as adding, updating, and deleting users.

## Classes and Methods

### `User` Class

- **Purpose**: Represents a user with attributes such as user ID, name, surname, email, password, and birthday.
- **Methods**:
  - `__init__(self, user_id, name, surname, email, password, birthday)`: Initializes a new user.
  - `get_details(self)`: Returns the user's details as a formatted string.
  - `get_age(self)`: Calculates and returns the user's age.

### `UserService` Class

- **Purpose**: Manages a list of users and provides methods to add, find, delete, and update users.
- **Methods**:
  - `add_user(cls, user)`: Adds a user to the list.
  - `find_user(cls, user_id)`: Finds and returns a user by their ID.
  - `delete_user(cls, user_id)`: Deletes a user by their ID.
  - `update_user(cls, user_id, name, email)`: Updates a user's name and email.
  - `get_number(cls)`: Returns the number of users.

### `UserUtil` Class

- **Purpose**: Provides utility methods for generating user IDs, passwords, and emails, and for validating passwords and emails.
- **Methods**:
  - `generate_user_id()`: Generates a new user ID.
  - `generate_password()`: Generates a strong password.
  - `is_strong_password(password)`: Checks if a password is strong.
  - `generate_email(name, surname, domain)`: Generates an email address.
  - `validate_email(email)`: Validates an email address.

## How to Run the Code

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory.
4. Run the `main.py` file to interact with the user management system:
   ```sh
   python main.py
   ```
5. To run the tests, use the following command:
   ```sh
   python -m unittest discover
   ```

## UML Class Diagram



## Sample Runs

### Input
```
Enter your name: John
Enter your surname: Doe
Enter your birthday YYYY-MM-DD (like 2000-01-01): 1990-05-15
```

### Output
```
User added successfully!
ID:230121012
Name: John
Surname: Doe
Email: john.doe@gmail.com
Password: P@ssw0rd!
Birthday: 1990-05-15

User age: 33

Email validation: john.doe@gmail.com is Valid email
Password strength: P@ssw0rd! is strong
```

### Test Output
```
test_add_user (__main__.TestUserService) ... ok
test_delete_user (__main__.TestUserService) ... ok
test_find_user (__main__.TestUserService) ... ok
test_update_user (__main__.TestUserService) ... ok
test_generate_email (__main__.TestUseUtil) ... ok
test_generate_password (__main__.TestUseUtil) ... ok
test_generate_user_id (__main__.TestUseUtil) ... ok
test_is_strong_password (__main__.TestUseUtil) ... ok
test_validate_email (__main__.TestUseUtil) ... ok
test_get_age (__main__.TestUser) ... ok
test_get_details (__main__.TestUser) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```

This documentation provides an overview of the classes and methods, instructions on how to run the code, a UML class diagram, and sample runs to demonstrate the functionality.