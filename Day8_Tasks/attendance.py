"""1. Student Attendance Record 
A teacher wants to store student attendance in a file named attendance.txt. Write a 
Python program that takes a student name as input and appends it to the file. Then 
display the contents of the file. """

student_name = input("Enter students name:")
with open("attendance.txt", "a") as file:
    file.write(student_name + "\n")
print("\nAttendance:")
with open("attendance.txt", "r") as file:
    content = file.read()
    print(content)
