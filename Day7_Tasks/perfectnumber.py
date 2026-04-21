#Write a program to check whether a number is a Perfect number.

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Perfect number")
else:
    print("Not a Perfect number")
print(sum)
