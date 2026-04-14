"""Filter Values Using Condition 
A dataset: 
arr = np.array([10, 25, 30, 15, 40]) 
Task: 
● Convert to Pandas Series 
● Filter values greater than 20 """

import numpy as np
import pandas as pd

arr = np.array([10, 25, 30, 15, 40]) 
print(arr)

S = pd.Series(arr)
print("\nS:", S)

filter = arr[arr > 20]
print(filter)
