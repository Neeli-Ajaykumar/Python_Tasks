""" =========================================================================
 📊 Project Title: IGN
 Analyze ign dataset using NumPy, Pandas, Matplotlib
 ============================================================================

 ============================================================================
 📦 Import Required Libraries
 ============================================================================
 👉 Import numpy
 👉 Import pandas
 👉 Import matplotlib.pyplot
 👉 (Optional) Import os for folder creation"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

"""=========================================================================
 🟢 SCENARIO 1: Data Loading & Preprocessing 
 ============================================================================ 
You are given the ign.csv dataset containing game reviews. 
Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows (head()) 
○ Last 5 rows (tail()) 
○ Shape of dataset 
3. Remove the unnecessary column: 
○ "Unnamed: 0" (index column) 
4. Check for missing values in: 
○ score, genre, platform 
5. Handle missing values: 
○ Fill numeric column score with mean 
○ Fill categorical column genre with mode 
6. Ensure correct data types: 
○ score → float 
○ release_year, release_month, release_day → integer""" 

#Load the dataset using Pandas.
df = pd.read_csv("ign.csv")

#Displaying first 5 rows and last 5 rows and shape
print("First 5 rows\n", df.head())
print("================================================")
print("last 5 rows\n", df.tail())
print("================================================")
print("shape", df.shape)
print("================================================")

#Removing the unnecessary column
df = df.drop("Unnamed: 0", axis = 1)

#Checking for missing values
print(df[["score", "genre", "platform"]].isnull().sum())
print("================================================")
print("================================================")

#Handling missing values
#Fill numeric column score with mean 
score_mean = df["score"].mean()
df["score"] = df["score"].replace(np.nan, score_mean)

#Fill categorical column genre with mode
genre_mode = df["genre"].mode()[0]
df["genre"] = df["genre"].replace(np.nan, genre_mode)

#Ensure correct data types
df["score"] = df["score"].astype(float)

df["release_year"] = df["release_year"].astype(int)

df["release_month"] = df["release_month"].astype(int)

df["release_day"] = df["release_day"].astype(int)

#--------------------------------------------------------------------------------------

"""=========================================================================
 🟢 Scenario 2: Line Graph (Score Trend) + Save  
 ============================================================================
You want to analyze how game scores change over time. 
Tasks: 
1. Group data by release_year. 
2. Calculate average score per year using Pandas. 
3. Convert results into NumPy arrays. 
4. Plot a line graph: 
○ X-axis → release_year 
○ Y-axis → average score 
5. Add: 
○ Title: "Average Game Score Over Years" 
○ Axis labels 
6. Save the graph: plt.savefig("avg_score_trend.png") """

#Group data by release_year and Calculate average score per year using Pandas.
yearly_avg = df.groupby("release_year")["score"].mean()
print("(S2)yearly_avg\n", yearly_avg)
print("================================================")

#convert to numpy arrays
x = yearly_avg.index.values
print(type(x))

y = yearly_avg.values
print(type(y))
print("================================================")
print("================================================")

#Plot a line graph:

plt.plot(x,y, marker = 'o')
plt.title("Line Graph Of Average Game Score Over The Years")
plt.xlabel("release_year")
plt.ylabel("average score")
plt.savefig("Line Graph avg_score_trend.png")
plt.grid()
plt.show()

#--------------------------------------------------------------------------------------

""" =========================================================================
 🟢 Scenario 3: Filtering + Bar Chart + Save 
 ============================================================================
You want to compare top platforms. 
Tasks: 
1. Filter dataset where: 
○ score > 7 
2. Count number of high-rated games per platform. 
3. Select top 10 platforms using Pandas. 
4. Convert data into NumPy arrays. 
5. Plot a bar chart: 
○ X-axis → platform 
○ Y-axis → count of games 
6. Rotate x-axis labels for readability. 
Save the graph: plt.savefig("top_platforms_bar.png") """

#Filter dataset where: score > 7
dataset = df[df["score"] > 7]
print("(S3) dataset preview")
print(dataset.head())
print("================================================")

#Count number of high-rated games per platform of top 10 platforms
high_rated = dataset["platform"].value_counts().head(10)
print("(S3)high_rated\n", high_rated)
print("================================================")

#Convert data into NumPy arrays.
x = high_rated.index.values
print(type(x))
y = high_rated.values
print(type(y))
print("================================================")
print("================================================")

#Plot a bar chart:
plt.bar(x, y)
plt.xticks(rotation=45)
plt.title("Bar Chart for Top 10 platforms")
plt.xlabel("platform")
plt.ylabel("count of games")
plt.savefig("Bar Charttop_platforms_bar.png")
plt.show()

#--------------------------------------------------------------------------------------

""" =========================================================================
 🟢 Scenario 4: Aggregation + Pie Chart + Save 
 ============================================================================
You want to analyze genre distribution.
Tasks: 
1. Count the number of games per genre. 
2. Select top 5 genres using Pandas. 
3. Prepare labels and values. 
4. Plot a pie chart: 
○ Labels → genre 
○ Values → count 
5. Add percentage labels (autopct). 
Save the graph: plt.savefig("genre_distribution.png")"""

#Count the number of games per genre
genre_counts = df["genre"].value_counts()
print("(S4)genre_counts\n", genre_counts)
print("================================================")

#Select top 5 genres
top5 = genre_counts.head(5)
print("(S4)top 5 genres\n", top5)
print("================================================")
print("================================================")

#Prepare labels and values
labels = top5.index
values = top5.values

#Plot pie chart
explode = (0.1, 0.1, 0.1, 0.1, 0)
plt.pie(values, labels = labels, explode = explode, autopct = "%1.1f%%", shadow = True, startangle = 140)
plt.title("Pie Chart Top 5 Genres Game Distribution")
plt.xlabel("genre")
plt.ylabel("count")
plt.savefig("Pie Chart genre_distribution.png")
plt.show()

#--------------------------------------------------------------------------------------

""" =========================================================================
 🟢 Scenario 5: Advanced Analysis + Multiple Graphs 
 ============================================================================
You are asked to perform a detailed analysis of review patterns. 
Part 1: Feature Engineering 
  1. Create a new column: 
    ○ score_category: 
        score >= 9 → "Excellent" 
        7 <= score < 9 → "Good" 
        < 7 → "Average" 
  2. Convert editors_choice: 
     ○ Y → 1, N → 0
     
Part 2: NumPy Analysis 
  3. Use NumPy to: 
    ○ Calculate yearly score growth using np.diff() on average yearly scores 

Part 3: Visualizations 
Line Graph 
  4. Plot trend of: 
    ○ Average score per release_year 

Stacked Bar Chart 
  5. Show count of: 
    ○ score_category per release_year 

Histogram 
  6. Plot distribution of: 
    ○ score 

Part 4: Save All Graphs 
plt.savefig("score_trend.png") 
plt.savefig("score_category_stacked.png") 
plt.savefig("score_distribution.png") """

#Create a new column:
def categorize(score):
    if score >= 9:
        return "Excellent"
    elif score >=7:
        return "Good"
    else:
        return "Average"

df["score_category"] = df["score"].apply(categorize)
print("(S5)score_category\n", df["score_category"])
print("================================================")

# Convert editors_choice (Y/N → 1/0)
df["editors_choice"] = (df["editors_choice"] == "Y").astype(int)
print("(S5)editors_choice\n", df["editors_choice"])
print("================================================")

# Average score per year
avg_yearly = df.groupby("release_year")["score"].mean().sort_index()
print("(S5)avg_yearly", avg_yearly)
print("================================================")
print("================================================")

#Line Graph: Average score per year
plt.plot(yearly_avg.index, yearly_avg.values, marker='o')
plt.title("Line Graph Average Score per Year")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.savefig("Line Graph1 score_trend.png")
plt.show()

#Stacked Bar Chart: score_category per year
pd.crosstab(df["release_year"], df["score_category"]).plot(kind="bar", stacked=True)
plt.title("Stacked Bar Chart Score Category per Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.savefig("Stacked Bar Chart score_category_stacked.png")
plt.show()

# 3. Histogram: score distribution
plt.hist(df["score"], bins=10)
plt.title("Histogram Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("Histogram score_distribution.png")
plt.show()



