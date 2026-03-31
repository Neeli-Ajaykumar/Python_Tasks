#Write a program to check whether a number is Prime.

n = int(input("Enter a number: "))
if n <= 1:
    print("Not a Prime number")
else:
    for i in range(1, n):
        if n % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
