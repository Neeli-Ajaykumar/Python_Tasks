#Write a program to check whether a string is a palindrome.
str = input("Enter an Element:")
reverse = str[::-1]
if str == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
