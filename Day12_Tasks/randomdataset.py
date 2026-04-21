"""Random Dataset Normalization + Filtering 
Scenario: 
● Generate 8 random float values between 0 and 1. 
Task: 
1. Normalize by multiplying with 100 
2. Filter values greater than 50 
3. Sort the filtered values """

import numpy as np

data = np.random.rand(8)
data = np.round(data, 2)
print("Original Data:", data)

normalized = np.round(data * 100, 2)
print("Normalized Data:", normalized)

filtered = normalized[normalized > 50]
print("Filtered:", filtered)

sorted_values = np.sort(filtered)
print("Sorted Filtered Values:", sorted_values)
