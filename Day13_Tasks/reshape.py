"""Reshape & Row Averages 
A dataset: 
data = np.arange(1, 13) 
Task: 
● Reshape it into a 3×4 matrix 
● Compute average of each row """

import numpy as np

data = np.arange(1, 13)
print("Data:", data)

matrix = data.reshape(3, 4)
print("Matrix:\n", matrix)

row_averages = [float(sum(row) / len(row)) for row in matrix]
print("Row Averages:", row_averages)
