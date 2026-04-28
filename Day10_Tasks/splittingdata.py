"""Splitting Data for Parallel Processing 
A dataset contains the following values: 
[5, 10, 15, 20, 25, 30] 
Scenario: 
You want to distribute the data across 3 processors. 
Task: 
● Store the data in a NumPy array. 
● Split it into 3 equal parts using NumPy. """

import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30])
print("Before splitting:", arr)
new_arr = np.array_split(arr, 3)
print("After splitting:",new_arr)
