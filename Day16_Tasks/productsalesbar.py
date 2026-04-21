"""Product Sales Bar Chart 
Scenario: 
products = ["Pen", "Book", "Pencil"] 
sales = np.array([50, 80, 40]) 
Task: 
● Create DataFrame 
● Plot bar chart 
● Add labels and title """

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

products = ["Pen", "Book", "Pencil"] 
sales = np.array([50, 80, 40])

df = pd.DataFrame({"products": products, "sales": sales})
print(df)

plt.figure(figsize=(10,5))
plt.bar(df["products"], df["sales"], color = "red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bar graph")

plt.show()
