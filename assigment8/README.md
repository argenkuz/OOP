# Employee Management System

This project is an Employee Management System implemented in Python using SQLite for database management. It allows you to perform CRUD (Create, Read, Update, Delete) operations on employee records.

## Classes and Methods

### Employee Class

The `Employee` class represents an employee with the following attributes:
- `id`: The unique identifier for the employee.
- `name`: The name of the employee.
- `position`: The position of the employee.
- `salary`: The salary of the employee.
- `hire_date`: The hire date of the employee.

#### Methods:
- `__init__(self, id=None, name=None, position=None, salary=None, hire_date=None)`: Initializes a new employee instance.
- `__str__(self)`: Returns a string representation of the employee.
- Getter and setter methods for each attribute.

### EmployeeDAO Class

The `EmployeeDAO` class handles database operations for the `Employee` class.

#### Methods:
- `__init__(self, db_name="person.db")`: Initializes the database connection and creates the table if it doesn't exist.
- `create_table(self)`: Creates the `employees` table if it doesn't exist.
- `insert(self, employee)`: Inserts a new employee record into the database.
- `get_by_id(self, id)`: Retrieves an employee record by its ID.
- `get_all(self)`: Retrieves all employee records from the database.
- `update(self, employee)`: Updates an existing employee record in the database.
- `delete(self, id)`: Deletes an employee record by its ID.
- `delete_all(self)`: Deletes all employee records and resets the auto-increment counter.

## How to Run the Code

1. Ensure you have Python installed on your system.
2. Clone the repository or download the project files.
3. Navigate to the project directory.
4. Run the `main.py` file to start the interactive menu:
   ```sh
   python main.py
   
## Sample Input/Output:
### 1 Insert employee
```
MENU OPTIONS
1. Insert employee
2. Get employee by id
3. Get all employees
4. Update employee
5. Delete employee
6. Delete all employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 1
Enter name: Aigerim
Enter position: worker
Enter salary: 15000
```
### 2 Get employee by id
```
MENU OPTIONS
1. Insert employee
2. Get employee by id
3. Get all employees
4. Update employee
5. Delete employee
6. Delete all employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 2
Enter id: 15
Employee(id=15, name=Aigerim, position=worker, salary=15000.0, hire_date=2025-04-01)
```
### 3 Get all employees
```
MENU OPTIONS
1. Insert employee
2. Get employee by id
3. Get all employees
4. Update employee
5. Delete employee
6. Delete all employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 3
Employee(id=1, name=Aidin, position=Manager, salary=50000.0, hire_date=2023-01-15)
Employee(id=2, name=Maga, position=Engineer, salary=45000.0, hire_date=2022-05-20)
Employee(id=3, name=Aidai, position=HR, salary=40000.0, hire_date=2021-07-30)
Employee(id=4, name=Kirill, position=Technician, salary=42000.0, hire_date=2022-09-10)
Employee(id=5, name=Bektur, position=Accountant, salary=47000.0, hire_date=2023-03-12)
Employee(id=6, name=Baisal, position=Sales, salary=43000.0, hire_date=2021-11-05)
Employee(id=7, name=Aiturgan, position=Support, salary=39000.0, hire_date=2022-06-25)
Employee(id=8, name=Beks, position=Consultant, salary=52000.0, hire_date=2023-04-18)
Employee(id=9, name=Zhenishbek, position=CEO, salary=55000.0, hire_date=2023-02-01)
Employee(id=10, name=Iman, position=Analyst, salary=48000.0, hire_date=2022-08-15)
Employee(id=14, name=Meder, position=VR, salary=3000.0, hire_date=2025-04-01)
Employee(id=15, name=Aigerim, position=worker, salary=15000.0, hire_date=2025-04-01)
```

### 4 Update employee
```
MENU OPTIONS
1. Insert employee
2. Get employee by id
3. Get all employees
4. Update employee
5. Delete employee
6. Delete all employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 4
Enter updated id: 15
Enter updated name: Aikusha
Enter updated position: worker
Enter updated salary: 100000
Employee updated successfully
```
### 5 Delete employee
```
MENU OPTIONS
1. Insert employee
2. Get employee by id
3. Get all employees
4. Update employee
5. Delete employee
6. Delete all employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 5
Enter id to delete: 14
Employee deleted successfully
```
### To show Final Result
```
MENU OPTIONS
1. Insert employee
2. Get employee by id
3. Get all employees
4. Update employee
5. Delete employee
6. Delete all employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 3
Employee(id=1, name=Aidin, position=Manager, salary=50000.0, hire_date=2023-01-15)
Employee(id=2, name=Maga, position=Engineer, salary=45000.0, hire_date=2022-05-20)
Employee(id=3, name=Aidai, position=HR, salary=40000.0, hire_date=2021-07-30)
Employee(id=4, name=Kirill, position=Technician, salary=42000.0, hire_date=2022-09-10)
Employee(id=5, name=Bektur, position=Accountant, salary=47000.0, hire_date=2023-03-12)
Employee(id=6, name=Baisal, position=Sales, salary=43000.0, hire_date=2021-11-05)
Employee(id=7, name=Aiturgan, position=Support, salary=39000.0, hire_date=2022-06-25)
Employee(id=8, name=Beks, position=Consultant, salary=52000.0, hire_date=2023-04-18)
Employee(id=9, name=Zhenishbek, position=CEO, salary=55000.0, hire_date=2023-02-01)
Employee(id=10, name=Iman, position=Analyst, salary=48000.0, hire_date=2022-08-15)
Employee(id=15, name=Aikusha, position=worker, salary=100000.0, hire_date=2025-04-01)
```
