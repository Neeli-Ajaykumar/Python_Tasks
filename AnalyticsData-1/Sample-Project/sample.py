import pandas as pd
from matplotlib import pyplot as plt

d = pd.read_csv("railway_gauges.csv")

print(d.head())
print(d.tail())

d = d.drop('Total', axis=1)

ax = d.plot(x="Year", kind="bar")

plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Total")
plt.title("Gauges: Number of railway tracks installed per year")

plt.savefig("rail_gauges.png")
plt.show()
