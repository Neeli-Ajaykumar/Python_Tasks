#Write a program to find the student with the highest marks from a dictionary.
students = {"ajay":90,"mahesh":80,"naresh":70,"arun":60}
std = max(students, key=students.get)
print("Student with highest marks:", std)
print("Marks:", students[std])
