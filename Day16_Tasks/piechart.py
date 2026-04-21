""" Pie Chart with Conditional Data 
Scenario: 
scores = np.array([40, 60, 80, 30, 90]) 
Task: 
● Categorize into: 
○ Pass (>50) 
○ Fail (<=50) 
● Count using NumPy/Pandas 
● Plot pie chart for Pass vs Fail """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

scores = np.array([40, 60, 80, 30, 90])
print(scores)

df = pd.DataFrame({"scores": scores})
print(df)

df["Result"] = np.where(df["scores"] > 50, "Pass", "Fail")
print(df)

counts = df["Result"].value_counts()
print(counts)

explode = (0.1, 0)
plt.pie(counts, labels=counts.index, explode = explode, autopct="%1.1f%%", shadow = True, colors=["green", "red"])
plt.title(" pie chart for Pass vs Fail")

plt.show()
