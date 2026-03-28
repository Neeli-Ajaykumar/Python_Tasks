# Write a function that returns the factorial of a number.
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter any value:"))
r = fact(n)
print("factorial of", n, "is:", r)
