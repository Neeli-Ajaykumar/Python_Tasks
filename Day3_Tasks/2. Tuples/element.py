#Write a program to check whether an element exists in a tuple
tuple = (10,20,30,40,50)
n = int(input("Enter any value:"))
if n in tuple:
    print("Element exist")
else:
    print("Element doesnot exist")
