"""Employee Salary System (Simple Inheritance) 
A company has two types of employees: Employee and Manager. Create a base class 
Employee containing name and salary. Create a derived class Manager that inherits 
from Employee and displays the employee details."""

class Employee:
    def details(self):
        print("Employee Name:", self.name)
        print("Employee salary:", self.salary)
class Manager(Employee):
    def display(self):
        print("The Employee Details Are:")
        self.details()
d = Manager()
d.name = "Ajay"
d.salary = 100000
d.display()

