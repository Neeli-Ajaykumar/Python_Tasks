""" Temperature Trend Line Plot 
Scenario: 
Daily temperatures: 
temps = np.array([28, 30, 32, 31, 29]) 
Task: 
● Convert into Pandas Series 
● Plot a line graph 
● Add title and grid """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

temps = np.array([28, 30, 32, 31, 29])

S = pd.Series(temps)
print(S)

plt.figure(figsize=(10,5))

plt.plot(temps, marker = "o")
plt.title("Line graph")
plt.grid(True)

plt.show()
