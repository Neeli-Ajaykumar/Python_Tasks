"""Temperature Monitoring System 
Scenario: 
temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → daily temperature trend 
○ Bar chart → day-wise temperature 
○ Pie chart → proportion of high (>30) vs low temps 
○ Histogram → temperature frequency 
○ Scatter plot → day index vs temperature """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"temps": temps, "days": days})
print(df)

result = []
for m in df["temps"]:
    if m > 30:
        result.append("high")
    else:
        result.append("low")
df["Result"] = result

plt.figure(figsize = (10,5))

plt.subplot(2,3,1)
plt.plot(df["days"], df["temps"], marker = "o")
plt.title("Line graph")

plt.subplot(2,3,2)
plt.bar(df["days"], df["temps"], color = "red")
plt.title("Bar graph")

plt.subplot(2,3,3)
counts = df["Result"].value_counts()
explode = (0.1,0)
plt.pie(counts, explode = explode, labels=counts.index, autopct='%1.1f%%', shadow = True, startangle = 90)
plt.title("Pie chart")

plt.subplot(2,3,4)
plt.hist(df["temps"], bins = 7, color = "yellow", histtype = "bar")
plt.title("Historam")

plt.subplot(2,3,5)
plt.scatter(df.index, df["temps"], color = "black")
plt.title("Scatter plot")

plt.tight_layout()
plt.show()
