"""Random Data & Filtering 
Generate random numbers: 
nums = np.random.randint(1, 100, 10) 
Task: 
● Filter values that are divisible by 5 
● Return sorted result."""

import numpy as np

nums = np.random.randint(1, 100, 10)
print("Numbers:", nums)

filtered = [int(x) for x in nums if x % 5 == 0]
filtered.sort()
print("Filtered & Sorted:", filtered)
