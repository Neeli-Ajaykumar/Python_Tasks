"""Remove Outliers 
Given data: 
values = np.array([10, 12, 15, 18, 100, 14, 13]) 
Task: 
● Compute the mean and standard deviation 
● Remove values that are more than 2 standard deviations from the mean """

import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])
print("Values:", values)

mean = sum(values) / len(values)
print("Mean:", mean)

variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)

lower = mean - 2 * std_dev
upper = mean + 2 * std_dev

filtered_values = [int(x) for x in values if x >= lower and x <= upper]
print("Filtered Values:", filtered_values)
