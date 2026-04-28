"""Multi-Line Graph for Sales Comparison 
Scenario: 
data = { 
"Month": ["Jan", "Feb", "Mar"], 
"Store_A": [100, 150, 200], 
"Store_B": [90, 140, 210]} 
Task: 
● Create DataFrame 
● Plot two line graphs on same plot 
● Add legend """


from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd

df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Store_A": [100, 150, 200], "Store_B": [90, 140, 210]})
print(df)

plt.plot(df["Month"], df["Store_A"], label = "months", marker = "o", color="r")
plt.plot(df["Month"], df["Store_B"], label = "sales", marker = "o", color="y")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Multi-LIne Graph")

plt.legend()

plt.show()
