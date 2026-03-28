#Write a program to count the number of vowels in a string.
str = input("Enter a string: ")
count = 0
vowels = "aeiouAEIOU"
for ch in str:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)
