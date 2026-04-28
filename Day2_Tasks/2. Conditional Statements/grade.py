#Write a program to assign grades based on marks (for example: A, B, C, Fail).
marks = float(input("Enter your marks from(0-100):"))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >=70 and marks < 80:
    print("Grade C")
else:
    print("Fail")
    
