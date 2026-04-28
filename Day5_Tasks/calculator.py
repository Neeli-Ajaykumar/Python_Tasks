"""Create a Python module named calculator.py that contains functions to perform: 
● Addition 
● Subtraction 
● Multiplication 
● Division 
Then write another Python program that imports this module and performs calculations 
based on user input.

import calculator
x = int(input("Enter any value of x:"))
y = int(input("Enter any value of y:"))
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul (x,y):
    return x * y
def div (x,y):
    return x / y
print(x)
print(y)"""


import calculator

x = int(input("Enter any value of x: "))
y = int(input("Enter any value of y: "))

print("Addition:", calculator.add(x, y))
print("Subtraction:", calculator.sub(x, y))
print("Multiplication:", calculator.mul(x, y))

if y != 0:
    print("Division:", calculator.div(x, y))
else:
    print("Division by zero not allowed")
