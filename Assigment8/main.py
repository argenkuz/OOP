import sqlite3
from datetime import datetime

class Employee:
    def __init__(self, id=None, name=None, position=None, salary=None, hire_date=None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return f"Employee(id={self.id}, name={self.name}, position={self.position}, salary={self.salary}, hire_date={self.hire_date})"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_hire_date(self):
        return self.hire_date

    def set_hire_date(self, hire_date):
        self.hire_date = hire_date

class EmployeeDAO:
    def __init__(self, db_name="person.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL,
            hire_date TEXT NOT NULL
        )""")
        self.conn.commit()


    def insert(self, employee):
        self.cursor.execute("""INSERT INTO employees (name, position, salary, hire_date) VALUES (?, ?, ?, ?)""",
                            (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()

    def get_by_id(self,id):
        self.cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
        row = self.cursor.fetchone()
        if row:
            return Employee(*row)
        return f"We can' find this id {id} "

    def get_all(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        return [Employee(*row) for row in rows]

    def update(self, employee):
        self.cursor.execute("""UPDATE employees SET name=?, position=?, salary=?, hire_date=? WHERE id=?""",
                            (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self,id):
        self.cursor.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM employees")  # Очистка всех данных
        self.cursor.execute("DELETE FROM sqlite_sequence WHERE name='employees'")  # Сброс автоинкремента
        self.conn.commit()

if __name__ == "__main__":
    dao = EmployeeDAO()

    while True:
        print("MENU OPTIONS")
        print("1. Insert employee")
        print("2. Get employee by id")
        print("3. Get all employees")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Delete all employees")
        print("7. Exit")


        choices = int(input("Enter your choice (1,2,3,4,5,6,7): "))

        if choices == 1:
            name  = input("Enter name: ")
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            hire_date = datetime.now().strftime("%Y-%m-%d")
            employee = Employee(name=name, position=position, salary=salary, hire_date=hire_date)
            dao.insert(employee)

        elif choices == 2:
            id1 = int(input("Enter id: "))
            employee = dao.get_by_id((id1))
            print(employee)

        elif choices == 3:
            employees = dao.get_all()
            for employee in employees:
                print(employee)

        elif choices == 4:
            id = int(input("Enter updated id: "))
            name = input("Enter updated name: ")
            position = input("Enter updated position: ")
            salary = float(input("Enter updated salary: "))
            hire_date = datetime.now().strftime("%Y-%m-%d")
            employee = Employee(id, name, position, salary, hire_date)
            dao.update(employee)
            print("Employee updated successfully")

        elif choices == 5:
            id = int(input("Enter id to delete: "))
            dao.delete(id)
            print("Employee deleted successfully")

        elif choices == 7:
            print("Exiting...")
            break
        elif choices == 6:
            dao.delete_all()
            print("All employees deleted successfully")

        else:
            print("Invalid choice. Please try again")

