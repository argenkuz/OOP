from main import EmployeeDAO, Employee
from datetime import datetime

if __name__ == "__main__":
    dao = EmployeeDAO()

    new_employee = Employee(name = "Argen", position = "programmer", salary = "600000", hire_date = datetime.now().strftime("%Y-%m-%d"))
    dao.insert(new_employee)
    print("Employee inserted.")

    # Retrieve and display an employee by ID
    employ = dao.get_by_id(11)
    print("\nRetrieved employee by ID:", employ,"\n")

    all = dao.get_all()
    for employee in all:
        print(employee)

    updated_employer = Employee(id = 11, name="Madina", position="worker", salary="100", hire_date=datetime.now().strftime("%Y-%m-%d"))
    dao.update(updated_employer)
    print("\nEmployee updated.", dao.get_by_id(11))

    deleted_employee = dao.delete(11)
    print("\nEmployee deleted.", deleted_employee)

    for employee in all:
        print(employee)
#