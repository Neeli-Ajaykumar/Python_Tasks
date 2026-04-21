""" Boolean Masking for Salary Analysis 
Scenario: 
Employee salaries: 
[25000, 40000, 15000, 50000, 30000] 
Task: 
● Filter salaries above 30000. 
● Count how many employees satisfy this condition. """

import numpy as np

Employee_salaries = np.array([25000, 40000, 15000, 50000, 30000])
print(Employee_salaries)

emp = Employee_salaries > 30000
print(emp)

salaries = Employee_salaries[emp]
print(salaries)

count = np.sum(Employee_salaries > 30000)
print(count)
