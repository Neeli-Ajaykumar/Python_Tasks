"""Employee Salary Insights 
Scenario: 
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
Task: 
● Convert into DataFrame 
● Plot: 
○ Line graph → salary trend 
○ Bar chart → department-wise salary comparison 
○ Pie chart → department distribution 
○ Histogram → salary distribution 
○ Scatter plot → index vs salary """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df = pd.DataFrame({"salaries": salaries, "departments": departments})
print(df)

plt.figure(figsize=(10,15))

plt.subplot(2,3,1)
plt.plot(df["departments"], df["salaries"], marker = 'o')
plt.title('Line graph')

dept_avg = df.groupby("departments")["salaries"].mean()
plt.subplot(2,3,2)
plt.bar(dept_avg.index, dept_avg.values, color='r')
plt.title('Bar graph')

dept_counts = df["departments"].value_counts()
plt.subplot(2,3,3)
explode = (0.1, 0, 0)
plt.pie(dept_counts, labels=dept_counts.index, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Pie chart")

plt.subplot(2,3,4)
plt.hist(df["salaries"], bins=5, color='green', histtype = 'bar', edgecolor = 'black')
plt.title("Histogram")

plt.subplot(2,3,5)
plt.scatter(df.index, df["salaries"], color = 'red')
plt.title("Scatter plot")

plt.tight_layout()
plt.show()
