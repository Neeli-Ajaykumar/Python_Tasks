"""Employee Salary Management System 
A company stores employee data in a file employees.txt in the format: 
EmployeeName Salary 
Example: 
Ramesh 25000 
Sita 30000 
Arun 28000 
Write a Python program that: 
● Reads employee data from the file 
● Displays all employee details 
● Finds the employee with the highest salary 
● Appends a new employee record to the file."""

file = open("employee.txt", "r")
print("Employee Details:\n")

lines = file.readlines()

highest_salary = -1
employee = ""

for line in lines:
    line = line.strip()
    
    if line:
        parts = line.split()

        if len(parts) != 2 or not parts[1].isdigit():
            continue
        
        Employee_name = parts[0]
        Salary = int(parts[1])
        
        print(Employee_name, Salary)
        if Salary > highest_salary:
            highest_salary = Salary
            employee = Employee_name
file.close()

file = open("employee.txt", "a")
Employee_name = input("Enter employee name:")
Salary = int(input("Enter employee salary:"))

file.write(f"{Employee_name} {Salary}\n")
file.close()

print("\nHighest Salary Employee:")
print(employee, highest_salary)

