"""Count Occurrences 
You have: 
data = np.array([1, 2, 2, 3, 1, 4, 2, 3]) 
Task: 
● Count how many times each unique number appears. 
● Return numbers with their counts. """

import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
print("data:", data)

counts = {}
for x in data:
    if int(x) in counts:
        counts[int(x)] += 1
    else:
        counts[int(x)] = 1
print(counts)
