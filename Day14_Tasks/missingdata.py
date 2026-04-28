""" Missing Data Handling (NumPy + Pandas) 
A dataset: 
arr = np.array([10, np.nan, 30, np.nan, 50]) 
Task: 
● Convert to Pandas Series 
● Replace NaN values with the mean of the Series 
● Print updated data """

import numpy as np
import pandas as pd

arr = np.array([10, np.nan, 30, np.nan, 50]) 
print("Array:\n", arr)

S = pd.Series(arr)
print("\nSeries:\n", S)

mean_value = S.mean()
print("\nMean value:", mean_value)

S_updated = S.replace(np.nan, S.mean())
print("\nUpdated Series:\n", S_updated)
