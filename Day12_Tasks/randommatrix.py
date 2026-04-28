""" Random Matrix and Condition Filtering 
Scenario: 
● Generate a 3×3 matrix of random numbers (0–50). 
Task: 
● Filter elements greater than 25. 
● Print filtered values. """

import numpy as np

numbers = np.random.randint(0, 50, 9)
print("Random Numbers:", numbers)


matrix = numbers.reshape(3, 3)
print("\nMatrix:\n", matrix)

filtered = matrix[matrix > 25]
print("\nFiltered values:", filtered)
