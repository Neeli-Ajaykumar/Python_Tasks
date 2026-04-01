"""Student Marks File Analyzer 
A teacher stores student marks in a file marks.txt in the format: 
Name Marks 
Example: 
Rahul 80 
Anita 90 
Ravi 75 
Write a Python program to: 
● Read the file 
● Display all student records 
● Calculate and display the average marks of the class """

file = open("marks.txt", "r")
total = 0
count = 0
print("Student Records:\n")
lines = file.readlines()
#print(lines)
for line in lines[1:]:
    line = line.strip()
    if line:
        parts = line.split()
        name = parts[0]
        marks = int(parts[1])
        print(name, marks)
        total += marks
        count += 1
file.close()
if count > 0:
    average = total / count
    print("Average Marks:", average)
else:
    print("No records found.")
