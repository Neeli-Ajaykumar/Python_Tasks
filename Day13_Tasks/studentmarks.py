"""Student Marks Analysis 
Given marks of 5 students in 3 subjects: 
marks = np.array([ 
[70, 80, 90], 
[60, 75, 85], 
[50, 65, 70], 
[90, 95, 85], 
[40, 55, 60] 
]) 
Task: 
● Calculate total marks of each student. 
● Identify students whose total marks are above the class average. """

import numpy as np

marks = np.array([[70, 80, 90],[60, 75, 85],[50, 65, 70],[90, 95, 85],[40, 55, 60]])
print("Before operations:", marks)

total_marks = np.sum(marks, axis=1)
class_avg = sum(total_marks) / len(total_marks)
above_avg_students = np.where(total_marks > class_avg)

print("Total Marks:", total_marks)
print("Class Average:", class_avg)
print("Students above average (index):", above_avg_students)
