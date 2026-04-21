"""Temperature Alert System 
Temperatures recorded in a city: 
temps = np.array([28, 32, 35, 31, 29, 40, 38]) 
Task: 
● Identify days where temperature is greater than 30. 
● Return their indices. """

import numpy as np

temp = np.array([28, 32, 35, 31, 29, 40, 38]) 
print("before operations:", temp)

values = temp[temp > 30]
print("temperatures (>30):", values)

indices = np.where(temp > 30)
print("indices are:", indices[0])
