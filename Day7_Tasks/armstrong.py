#Write a program to check whether a given number is an Armstrong number or not.
num = int(input("Enter any number:"))
temp = num
digits = len(str(num))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
