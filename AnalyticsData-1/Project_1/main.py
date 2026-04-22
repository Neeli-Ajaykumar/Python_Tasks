""" =========================================================================
 📊 Project Title: Railway Gauge Data Analysis
 Analyze railway gauge dataset using NumPy, Pandas, Matplotlib
 ============================================================================

 ============================================================================
 📦 1. Import Required Libraries
 ============================================================================
 👉 Import numpy
 👉 Import pandas
 👉 Import matplotlib.pyplot
 👉 (Optional) Import os for folder creation"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

""" =========================================================================
 📂 2. Load Dataset
 ============================================================================
 👉 Load CSV file into DataFrame
 👉 Display first 5 rows
 👉 Display column names"""

d = pd.read_csv("railway_gauges.csv")
print(d.head())
print(d.columns)

""" =========================================================================
 🟢 SCENARIO 1: Data Cleaning
 ============================================================================
 👉 Check missing values in dataset
 👉 Replace missing values with 0
 👉 Convert columns:
     Broad Gauge
     Metre Gauge
     Narrow Gauge
     Total
 👉 Ensure all are numeric type
 👉 Print data types after conversion"""

# Check missing values
print(d.isnull().sum())

# Replace missing values with 0
d = d.replace(np.nan, 0)

# Convert columns to numeric
cols = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']
for col in cols:
    d[col] = pd.to_numeric(d[col], errors='coerce')

""" ========================================================================
 🟢 SCENARIO 2: Line Graph (Total Tracks)
 ===========================================================================
 👉 Extract Year column
 👉 Extract Total column
 👉 Plot line graph
 👉 Add:
     Title
   X-label (Year)
     Y-label (Total Tracks)
 👉 Save graph inside "graphs" folder
 👉 Display graph
 👉 Write observation:
     Is trend increasing or decreasing?
 Extract Year and Total columns and plot"""

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

"""========================================================================
 🟡 SCENARIO 3: Bar Chart (After 2000)
 ==========================================================================
 👉 Filter dataset for Year > 2000
 👉 Extract:
     Broad Gauge
     Metre Gauge
     Narrow Gauge
 👉 Create positions for bars (NumPy)
 👉 Plot grouped bar chart
 👉 Add:
     Title
     Labels
     Legend
 👉 Rotate X-axis labels if needed
 👉 Save graph inside "graphs" folder
 👉 Display graph
 👉 Write observation:
     Which gauge is dominant?"""

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

"""=========================================================================
 🟡 SCENARIO 4: Pie Chart (Gauge Contribution)
 ===========================================================================
 👉 Calculate total sum of:
     Broad Gauge
     Metre Gauge
     Narrow Gauge
 👉 Store values in a list/structure
 👉 Plot pie chart
 👉 Add:
     Labels
     Percentage (autopct)
     Title
 👉 Save graph inside "graphs" folder
 👉 Display graph
 👉 Write observation:
     Which gauge contributes the most?"""

# Calculate total sum of each gauge
totals = d[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum()

# Plot pie chart
explode = (0.1, 0, 0)
plt.pie(totals, labels=totals.index, explode = explode, shadow = True, autopct='%1.1f%%')
plt.title("Pie graph Gauge Contribution Distribution")

# Save graph
plt.savefig("graphs/gauge_pie.png")
plt.show()

""" ========================================================================
 🔴 SCENARIO 5: Advanced Analysis
 ===========================================================================
 👉 Create new columns:
     % Broad Gauge
     % Metre Gauge
     % Narrow Gauge
 👉 Use NumPy to calculate year-to-year growth of Total tracks
 👉 Add growth as a new column
 👉 Plot line graph for:
     Broad Gauge
     Metre Gauge
     Total
 👉 Add title, labels, legend
 👉 Save graph
 👉 Display graph
 👉 Plot stacked bar chart:
     Broad at bottom
     Metre on top of Broad
     Narrow on top of both
 👉 Add title, labels, legend
 👉 Rotate X-axis labels
 👉 Save graph
 👉 Display graph
 👉 Identify:
     Year with highest growth
     Any declining gauge
 👉 Final Conclusion:
     Is railway shifting to a single dominant gauge?
     Explain in 2–3 lines"""

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

