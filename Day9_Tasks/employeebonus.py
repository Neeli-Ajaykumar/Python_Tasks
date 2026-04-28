"""Employee Bonus Calculator (Decorators & OOP) 
A company wants to apply a bonus calculation automatically before displaying the 
salary. Create an Employee class and use a decorator that modifies the salary by 
adding a bonus before displaying it."""

def apply_bonus(func):
    def wrapper(self):
        bonus_amount = self.salary * (self.bonus / 100)
        print("bonus_amount is:", bonus_amount)
        total_salary = self.salary + bonus_amount
        return func(self, total_salary)
    return wrapper

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    @apply_bonus
    def display_salary(self, total_salary):
        print("Employee:", self.name)
        print("Salary after bonus:", total_salary)

name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
bonus = float(input("Enter bonus percentage: "))

emp = Employee(name, salary, bonus)
emp.display_salary()
