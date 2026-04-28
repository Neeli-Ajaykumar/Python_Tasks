"""Data Alignment Issue in Series Addition 
Two Series: 
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"]) 
Task: 
● Add both Series 
● Explain why some values become NaN 
● Replace NaN with 0 and compute final result"""

import pandas as pd
import numpy as np

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("original S1 data:\n", S1)

S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
print("\noriginal S2 data:\n", S2)

S = S1 + S2
print("\nAdding both series:\n", S)

S_updated = S.replace(np.nan, 0)
print("\nFinal Series:\n", S_updated)

