#Write a program to find the largest of three numbers using if-elif-else.
x = int(input("Enter any number for x:"))
y = int(input("Enter any number for y:"))
z = int(input("Enter any number for z:"))
if x > y and x > z:
    print("x is larger")
elif y > z:
    print("y is larger")
else:
    print("z is larger")
    
