"""Student Marks Bar Chart 
Scenario: 
Marks of students: 
names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90]) 
Task: 
● Create a DataFrame 
● Plot a bar graph 
● Show student names on X-axis """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({"names": names, "marks": marks})
print(df)

plt.figure(figsize=(10,5))

plt.bar(df["marks"], df["names"], color = "red")
plt.title("Bar chart")
plt.xlabel("students")

plt.show()
