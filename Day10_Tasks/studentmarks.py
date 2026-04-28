"""Student Marks Analysis 
A teacher stores the marks of 5 students in a NumPy array. 
Scenario: 
You are given marks [45, 67, 89, 56, 72]. 
Task: 
● Convert the list into a NumPy array. 
● Add 5 grace marks to every student. 
● Print the updated marks """

import numpy as np

arr = np.array([45, 67, 89, 56, 72])
print("Without adding grace marks:", arr)
print("After Adding 5 grace marks to every student:", arr + 5)

