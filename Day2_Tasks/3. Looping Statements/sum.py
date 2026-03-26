#Write a program to find the sum of numbers from 1 to N using a loop.
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("The sum from 1 to", n, "is:", total)
