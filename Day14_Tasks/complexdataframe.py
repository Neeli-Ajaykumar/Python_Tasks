"""Complex DataFrame Transformation 
A DataFrame: 
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] 
}) 
Scenario: 
● Students scoring below 50 failed 
Task: 
1. Create a column Status ("Pass"/"Fail") 
2. Filter only passed students 
3. Calculate average marks of passed students"""

import pandas as pd
import numpy as np

df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Marks": [50, 80, 30, 90]})
print("Original Data:\n", df)

df["Status"] = np.where(df["Marks"] >= 50, "Pass", "Fail")
print("\nWith Status:\n", df)

passed_students = df[df["Status"] == "Pass"]
print("\nPassed Students:\n", passed_students)

avg_marks = passed_students["Marks"].mean()
print("\nAverage Marks of Passed Students:", avg_marks)
