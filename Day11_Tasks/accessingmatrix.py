"""Accessing Matrix Data 
A teacher stores marks of students in two subjects: 
[[78, 85], 
[90, 88], 
[67, 72]] 
Task: 
● Convert it to a NumPy array. 
● Access the second student's second subject mark"""

import numpy as np

arr = np.array([[78, 85], [90, 88], [67, 72]])
print(arr)
print("--------")
print(arr[1])
print(arr[1][1])
