""" Find Maximum Value 
A dataset: 
arr = np.array([12, 45, 22, 67, 34]) 
Task: 
● Convert to Pandas Series 
● Find the maximum value """

import numpy as np
import pandas as pd

arr = np.array([12, 45, 22, 67, 34])
print(arr)

S = pd.Series(arr)
print("Series:", S)

max = S.max()
print("maximum value:", max)
