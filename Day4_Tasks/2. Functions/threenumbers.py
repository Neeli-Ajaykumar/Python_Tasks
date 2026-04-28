#Write a Python program with a function that returns the largest of three numbers.
def larger(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
result = larger(a,b,c)
print("The largest of three numbers are:", result)
