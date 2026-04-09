"""Sorting Customer Names 
A system stores customer names: 
["Ravi", "Anil", "Sita", "John"] 
Task: 
● Convert it to a NumPy array. 
● Sort the names alphabetically."""

import numpy as np

arr = np.array(["Ravi", "Anil", "Sita", "John"])
print("Before sorting:", arr)
newarr = np.sort(arr)
print("After sorting;", newarr)
