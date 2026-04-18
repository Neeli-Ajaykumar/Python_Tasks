"""Student Performance Dashboard 
Scenario: 
A school records marks of students in one subject: 
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 
Task: 
● Convert to Pandas DataFrame 
● Plot: 
○ Line graph → trend of marks 
○ Bar chart → student vs marks 
○ Pie chart → Pass (>50) vs Fail 
○ Histogram → distribution of marks 
○ Scatter plot → index vs marks """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Student": students, "Marks": marks})
print(df)

result = []
for m in df["Marks"]:
    if m > 50:
        result.append("Pass")
    else:
        result.append("Fail")
df["Result"] = result

plt.figure(figsize=(9,3))

plt.subplot(2,3,1)
plt.plot(df["Student"], df["Marks"], marker = 'o')
plt.title("Line graph")

plt.subplot(2,3,2)
plt.bar(df["Student"], df["Marks"], color='r')
plt.title("Bar chart")

plt.subplot(2,3,3)
counts = df["Result"].value_counts()
explode = (0.1, 0)
plt.pie(counts, explode = explode, labels=counts.index, autopct='%1.1f%%', shadow = True, startangle = 90)
plt.title("Pie chart")

plt.subplot(2,3,4)
plt.hist(df["Marks"], bins=5, color='green', histtype = 'bar', edgecolor='black')
plt.title("Histogram")

plt.subplot(2,3,5)
plt.scatter(df.index, df["Marks"], color='red')
plt.title("Scatter plot")

plt.tight_layout()
plt.show()

 
