#Write a program to count the frequency of each character in a string
string = input("Enter a string: ")
frequency = {}
for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)
