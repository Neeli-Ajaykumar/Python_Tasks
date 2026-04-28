#Write a program that searches for a number in a list and breaks the loop when found
x = [10, 20, 30, 40, 50]
#x = int(input("Enter any values:"))
y = int(input("Enter number to search: "))
found = False
for n in x:
    if n == y:
        print("Number found!")
        found = True
        break
if not found:
    print("Number not found!")
