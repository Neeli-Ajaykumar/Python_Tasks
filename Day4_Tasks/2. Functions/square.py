#Write a function to find the square of a number.
def square(num):
    return num ** 2
    #return num * num
n = int(input("enter any value:"))
result = square(n)
print("The square of", n, "is:", result)  
