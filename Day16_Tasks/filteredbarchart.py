"""Filtered Bar Chart 
Scenario: 
marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"] 
Task: 
● Convert to DataFrame 
● Filter students with marks > 50 
● Plot bar chart only for filtered students """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"marks": marks, "names": names})
print(df)

filtered = df[df["marks"] > 50]
print("\nfiltered students\n", filtered)

plt.bar(filtered["names"], filtered["marks"], color = "green")
plt.title("Filtered students")
plt.xlabel("names")
plt.ylabel("marks")

plt.show()
