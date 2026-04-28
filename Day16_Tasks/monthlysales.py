"""Monthly Sales Analysis 
Scenario: 
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → month-wise comparison 
○ Pie chart → contribution of each month 
○ Histogram → frequency of sales values 
○ Scatter plot → month index vs sales """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
df = pd.DataFrame({"Sales": sales, "Months": months})
print(df)

plt.figure(figsize=(10,15))

plt.subplot(2,3,1)
plt.plot(df["Months"], df["Sales"], marker = 'o')
plt.title("Line graph")

plt.subplot(2,3,2)
plt.bar(df["Months"], df["Sales"], color='r')
plt.title("Bar chart")

plt.subplot(2,3,3)
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(df["Sales"], labels=df["Months"], explode = explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Pie chart")

plt.subplot(2,3,4)
plt.hist(df["Sales"], bins=5, color='green', histtype = 'bar', edgecolor='black')
plt.title("Histogram")

plt.subplot(2,3,5)
plt.scatter(df.index, df["Sales"], color='red')
plt.title("Scatter plot")

plt.tight_layout()
plt.show()
