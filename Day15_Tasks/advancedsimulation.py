"""Advanced Simulation System 
Scenario: 
Simulate exam results and generate reports. 
Task: 
● Generate random marks using random 
● Store in NumPy array 
● Convert to Pandas DataFrame 
● Use OOP to represent Student 
● Use conditions + loops to assign grades 
● Save report to file 
● Handle errors using try-except 
● Use math module for statistics """

import random
import numpy as np
import pandas as pd
import math

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
students = []

names = ["Ajay", "Ravi", "Naresh", "Mahesh", "Arun"]
for name in names:
    marks = random.randint(0, 100)
    print("Random marks:", marks)
    students.append(Student(name, marks))

marks_array = np.array([s.marks for s in students])

df = pd.DataFrame({"Name": [s.name for s in students], "Marks": marks_array})
grades = []

for m in marks_array:
    try:
        if m >= 75:
            grades.append("A")
        elif m >= 50:
            grades.append("B")
        else:
            grades.append("C")
    except:
        grades.append("Error")
df["Grade"] = grades

avg = sum(marks_array) / len(marks_array)
print("\nAverage:", avg)

max_mark = max(marks_array)
print("\nMaximun marks:", max_mark)

min_mark = min(marks_array)
print("\nMinimum marks:", min_mark)

try:
    with open("report.txt", "w") as f:
        f.write(str(df))
        f.write("\n\nAverage: " + str(avg))
        f.write("\nMax: " + str(max_mark))
        f.write("\nMin: " + str(min_mark))
except:
    print("Error writing file")
print(df)
