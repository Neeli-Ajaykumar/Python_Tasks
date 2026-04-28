#Write a program to remove duplicate characters from a string.
str = "heelloo"
str1 = ""
for ch in str:
    if ch not in str1:
        str1 += ch
print(str1)
