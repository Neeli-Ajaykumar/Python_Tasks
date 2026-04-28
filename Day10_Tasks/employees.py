""" Multi-Department Data Aggregation 
A company collects employee counts from two branches.
Branch A: 
[[10, 20], 
[30, 40]] 
Branch B: 
[[5, 15], 
[25, 35]] 
Scenario: 
● Combine the two matrices. 
● Calculate the total employees across all departments. 
● Print the combined matrix and total. """

import numpy as np

Branch_A = np.array([[10, 20], [30, 40]])
Branch_B = np.array([[5, 15], [25, 35]])

print("Branch_A:", Branch_A)
print("Branch_B:", Branch_B)

combine = Branch_A + Branch_B
print("combine of 2 matrices:", combine)

total = np.sum(combine)
print("Total employees across all departments:", total)
