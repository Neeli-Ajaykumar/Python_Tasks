"""Expense Distribution Pie Chart 
Scenario: 
Monthly expenses: 
expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"] 
Task: 
● Create a pie chart 
● Show percentage distribution """

from matplotlib import pyplot as plt
import numpy as np

expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"]

plt.figure(figsize=(10,5))
explode = (0.1,0.1,0)

plt.pie(expenses, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title("Pie chart")

plt.show()
