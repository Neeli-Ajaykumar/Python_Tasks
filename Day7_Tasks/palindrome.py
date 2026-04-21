#Write a program to check whether a number is a Palindrome. 
num = input("Enter any number:")
reverse = num[::-1]
if num == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
