"""Data Analysis Tool (NumPy + Pandas) 
Scenario: 
Analyze student marks. 
Task: 
● Generate marks using NumPy 
● Convert into Pandas DataFrame 
● Use conditions to filter passing students 
● Calculate mean using math/NumPy 
● Use loop to print results"""

import numpy as np
import pandas as pd

marks = np.array([35, 67, 80, 45, 90, 55, 30])

df = pd.DataFrame(marks, columns=["Marks"])
print("Data Frame:\n", df)

passing = df[df["Marks"] >= 40]
mean_marks = np.mean(marks)

print("\nAll Student Marks:")
for m in marks:
    print(m)

print("\nPassing Students Marks:")
for m in passing["Marks"]:
    print(m)

print("\nAverage Marks:", mean_marks)
