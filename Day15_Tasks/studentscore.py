"""Student Score Processor 
Scenario: 
A teacher stores student names and marks in a list of tuples. 
Task: 
● Convert data into a dictionary 
● Use a loop + condition to find students scoring above 50 
● Use math module to calculate average 
● Store results in a text file """

import math

students = [("Ajay", 70), ("Bunny", 60), ("Satish", 50), ("Naresh", 40)]
student_dict = dict(students)
print("Data into a dictionary:\n", student_dict)

above_50 = []
for name, marks in student_dict.items():
    if marks > 50:
        above_50.append((name, marks))
print("\nStudents scroing above(50):\n", above_50)

total = 0
for marks in student_dict.values():
    total = total + marks
average = total / len(student_dict)
print("\nAverage:", average)


with open("studentresult.txt", "w") as file:
    file.write("student scoring above 50:\n")
    for name, marks in above_50:
        file.write(f"{name}: {marks}\n")
    file.write(f"\nAverage marks:")
print("Results saved to studentresult.txt")
