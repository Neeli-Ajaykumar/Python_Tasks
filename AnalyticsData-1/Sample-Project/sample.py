#import Required Libraries
import pandas as pd
from matplotlib import pyplot as plt

# Load Dataset
d = pd.read_csv("railway_gauges.csv")

# Display first 5 rows and last 5 rows
print(d.head())
print(d.tail())

# Droping Total colum from the Dataset
d = d.drop('Total', axis=1)

# plotting bar graph
ax = d.plot(x="Year", kind="bar")

# Adding labels and title to the bar graph
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Total")
plt.title("Gauges: Number of railway tracks installed per year")

# saving figure and dislaying
plt.savefig("rail_gauges.png")
plt.show()
