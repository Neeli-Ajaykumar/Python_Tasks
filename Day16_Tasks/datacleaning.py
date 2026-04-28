"""Data Cleaning + Visualization 
Scenario: 
data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
Task: 
1. Convert to Pandas Series 
2. Replace NaN with mean 
3. Plot: 
○ Line graph of cleaned data 
○ Bar chart of values > average """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = np.array([100, np.nan, 200, 150, np.nan, 300])

s = pd.Series(data)
print("Series data:", s)

mean_value = s.mean()
print("\nMean value:", mean_value)

s = s.replace(np.nan, mean_value)
print("\nReplacing mean with nan:\n", s)

plt.figure(figsize=(10, 5))

plt.subplot(2, 3, 1)
plt.plot(s, marker="o", color="blue")
plt.title("Line Graph")

above_avg = s[s > mean_value]

plt.subplot(2, 3, 2)
plt.bar(above_avg.index, above_avg.values, color="green")
plt.title("Values > Average")

plt.tight_layout()
plt.show()
