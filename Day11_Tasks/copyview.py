"""Copy vs View Behavior in Data Processing 
Scenario: 
A dataset: 
[10, 20, 30, 40] 
Task: 
● Create a copy of the array. 
● Modify the original array. 
● Show that the copy does not change. 
● Repeat using view() and observe the difference."""

import numpy as np

arr = np.array([10, 20, 30, 40])
print("before operations:", arr)

x = arr.copy()
print("After copying:", x)

arr[0] = 100
print("After modifying:", arr)

x = arr.view()
print("using view:", x)

arr[1] = 200

print(arr)

 
