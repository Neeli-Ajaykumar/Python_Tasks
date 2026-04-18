"""Employee Management System (OOP + File + Dict) 
Scenario: 
Manage employee data. 
Task: 
● Create a class Employee 
● Store employees in a dictionary 
● Save data to a file 
● Use exception handling for invalid salary input 
● Use loop to display all employees """

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

employees = {}

while True:
    print("\n1. Add Employee")
    print("2. Show Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")

        try:
            salary = float(input("Enter Salary: "))
        except:
            print("Invalid salary!")
            continue

        employees[emp_id] = Employee(emp_id, name, salary)

    elif choice == "2":
        for emp in employees.values():
            print(emp.emp_id, emp.name, emp.salary)

    elif choice == "3":
        file = open("emp.txt", "w")
        for emp in employees.values():
            file.write(f"{emp.emp_id},{emp.name},{emp.salary}\n")
        file.close()
        break

    else:
        print("Invalid choice")
    
