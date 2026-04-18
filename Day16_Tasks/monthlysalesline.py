""" Monthly Sales Line Graph 
Scenario: 
A shop records monthly sales: 
sales = np.array([100, 150, 200, 250, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May"] 
Task: 
● Convert data into a Pandas DataFrame 
● Plot a line graph 
● Label X-axis as months and Y-axis as sales """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 150, 200, 250, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May"]

df = pd.DataFrame({"sales": sales, "months": months})
print(df)

plt.figure(figsize=(10,5))

plt.subplot(2,3,1)
plt.plot(df["months"], df["sales"], marker = "o")
plt.title("Line Graph")
plt.xlabel("months")
plt.ylabel("sales")
plt.show()
