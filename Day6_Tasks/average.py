"""1: Develop a Python program to manage student marks for three subjects. Store the subject 
names in a tuple, maintain unique student names in a set, and store each student’s marks 
in a list inside a dictionary where the key is the student name. Create user-defined 
functions to add a student with marks, display all student records, and calculate the average 
marks of a student. Implement a recursive function to calculate the total marks from the list of 
marks. The program should interact with the user through a simple menu. Also include 
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a 
student name entered does not exist in the dictionary). """


subjects = ("Math", "Science", "English")
student_names = set()
student_marks = {}

def calculate_total(marks_list):
    if not marks_list:  # Base case
        return 0
    return marks_list[0] + calculate_total(marks_list[1:])

def add_student():
    try:
        name = input("Enter student name: ")

        if name in student_names:
            print("Student already exists!")
            return

        marks = []

        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)

        
        student_names.add(name)
        student_marks[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter numeric values for marks.")
    except TypeError:
        print("Error: Invalid data type entered.")

def display_students():
    if not student_marks:
        print("No student records found.")
    else:
        for name, marks in student_marks.items():
            print(f"{name} : {marks}")

def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in student_marks:
            raise NameError

        marks = student_marks[name]

        total = calculate_total(marks)
        average = total / len(marks)

        print(f"Total Marks: {total}")
        print(f"Average Marks: {average}")

    except NameError:
        print("Error: Student not found.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero (no marks available).")
    except TypeError:
        print("Error: Marks contain invalid data.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        calculate_average()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")

















