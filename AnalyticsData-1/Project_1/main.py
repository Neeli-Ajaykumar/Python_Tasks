#import Required Libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# SCENARIO 1: Basic Data Loading & Cleaning

# Load Dataset
d = pd.read_csv("railway_gauges.csv")

# Display first 5 rows and column names
print(d.head())
print(d.columns)

# Check missing values
print(d.isnull().sum())

# Replace missing values with 0
d = d.replace(np.nan, 0)

# Convert columns to numeric
cols = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']
for col in cols:
    d[col] = pd.to_numeric(d[col], errors='coerce')

# SCENARIO 2: Line Graph (Total Track Growth)

# Extract Year and Total columns and plot
plt.plot(d['Year'], d['Total'], marker='o')

# Add title and labels
plt.title("Total Railway Track Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")

plt.xticks(rotation=70)
plt.tight_layout()

# Save graph
plt.savefig("graphs/total_growth.png")
plt.show()

# SCENARIO 3: Filtering + Bar Chart

# Filter data for years after 2000
d_modern = d[d['Year'] >= '2000-01']

# Plot grouped bar chart
ax = d_modern.plot(x="Year", y=['Broad Gauge', 'Metre Gauge', 'Narrow Gauge'], kind="bar")
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Bar graph Gauge Comparison After 2000")
plt.legend()

# Save graph
plt.savefig("graphs/gauge_bar.png")
plt.show()

# SCENARIO 4: Pie Chart (Gauge Contribution)

# Calculate total sum of each gauge
totals = d[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum()

# Plot pie chart
explode = (0.1, 0, 0)
plt.pie(totals, labels=totals.index, explode = explode, shadow = True, autopct='%1.1f%%')
plt.title("Pie graph Gauge Contribution Distribution")

# Save graph
plt.savefig("graphs/gauge_pie.png")
plt.show()

# SCENARIO 5: Advanced Analysis

# Create percentage columns
d['% Broad'] = (d['Broad Gauge'] / d['Total']) * 100
d['% Metre'] = (d['Metre Gauge'] / d['Total']) * 100
d['% Narrow'] = (d['Narrow Gauge'] / d['Total']) * 100

# Calculate yearly growth using NumPy
d['Growth'] = np.diff(d['Total'], prepend=d['Total'].iloc[0])

# Line graph for all gauges
plt.plot(d['Year'], d['Broad Gauge'], label='Broad', marker = 'o')
plt.plot(d['Year'], d['Metre Gauge'], label='Metre', marker = 'o')
plt.plot(d['Year'], d['Narrow Gauge'], label='Narrow', marker = 'o')

plt.legend()
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Line graph Gauge Trends Over Time")

plt.tight_layout()
plt.savefig("graphs/gauge_trends.png")
plt.show()

# Stacked bar chart
plt.bar(d['Year'], d['Broad Gauge'], label='Broad')
plt.bar(d['Year'], d['Metre Gauge'], bottom=d['Broad Gauge'], label='Metre')
plt.bar(d['Year'], d['Narrow Gauge'], bottom=d['Broad Gauge'] + d['Metre Gauge'], label='Narrow')

plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.title("Stacked bar graph Gauge Composition")
plt.legend()

plt.tight_layout()
plt.savefig("graphs/stacked_chart.png")
plt.show()

# Identify highest growth
print("Year with highest growth:")
print(d.loc[d['Growth'].idxmax()])

