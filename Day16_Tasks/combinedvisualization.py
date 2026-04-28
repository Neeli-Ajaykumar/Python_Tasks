"""Combined Visualization Dashboard 
Scenario: 
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph (trend) 
○ Bar chart (comparison) 
○ Pie chart (distribution) 
● Show all in single figure (subplots) """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"]

df = pd.DataFrame({"sales": sales, "products": products})
print(df)

plt.figure(figsize=(10,5))

plt.subplot(2,3,1)
plt.plot(df["products"], df["sales"], color = "red")
plt.title("Line Graph")

plt.subplot(2,3,2)
plt.bar(df["products"], df["sales"], color = "y")
plt.title("Bar graph")

plt.subplot(2,3,3)
explode = (0.1, 0, 0.1, 0)
plt.pie(df["sales"], labels=df["products"], explode = explode, shadow = True, autopct="%1.1f%%")
plt.title("Pie chart")


plt.show()
