"""Row Filtering + Aggregation 
A dataset: 
arr = np.array([ 
[100, 200], 
[150, 250], 
[80, 120], 
[300, 400] 
]) 
Task: 
● Convert to DataFrame with columns "Sales", "Profit" 
● Filter rows where Sales > 100 
● Find average Profit of filtered rows """

import numpy as np
import pandas as pd

arr = np.array([[100, 200], [150, 250], [80, 120], [300, 400]])
print("Array:", arr)

df = pd.DataFrame(arr, columns = ["Sales", "Profit"])
print("\nSeries:\n", df)

filter = df[df["Sales"] > 100]
print("\nFilter rows:\n", filter)

avg = filter["Profit"].mean()
print("\nAverage Profit:", avg)
