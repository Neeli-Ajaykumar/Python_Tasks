""" Product Sales & Profit Analysis 
Scenario: 
sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → product vs sales 
○ Pie chart → sales contribution 
○ Histogram → profit distribution 
○ Scatter plot → sales vs profit """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"sales": sales, "profit": profit, "products": products})
print(df)


plt.figure(figsize=(10,15))

plt.subplot(2,3,1)
plt.plot(df["products"], df["sales"], marker = 'o')
plt.title("Line graph")

plt.subplot(2,3,2)
plt.bar(df["products"], df["sales"], color='r')
plt.title("Bar chart")

plt.subplot(2,3,3)
explode = (0.1, 0, 0, 0, 0)
plt.pie(df["sales"], labels=df["products"], explode = explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Pie chart")

plt.subplot(2,3,4)
plt.hist(df["profit"], bins=5, color='green', histtype = 'bar', edgecolor='black')
plt.title("Histogram")

plt.subplot(2,3,5)
plt.scatter(df["sales"], df["products"], color='red')
plt.title("Scatter plot")

plt.tight_layout()
plt.show()
