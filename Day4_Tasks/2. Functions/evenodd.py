#Write a function to check whether a number is even or odd.
def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
num = int(input("Enter any value:"))
result = even_odd(num)
#print(result)

