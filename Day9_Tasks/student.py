"""Student Information System (Class & Object) 
A school wants a program to store student details. Create a Student class with 
attributes such as name, roll number, and marks. Create objects for at least three 
students and display their details. """

class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_num)
        print("Marks:", self.marks)
        print("----------------------")


student1 = Student("Ajay", 1, 80)
student2 = Student("Arun", 2, 90)
student3 = Student("Naresh", 3, 70)

student1.display()
student2.display()
student3.display()
