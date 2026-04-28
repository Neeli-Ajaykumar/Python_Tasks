""". Word Counter Program 
A writer saves an article in a file called article.txt. Write a Python program that: 
● Opens and reads the file 
● Counts the number of words, lines, and characters in the file 
● Displays the results. """

file = open("article.txt", "r")
content = file.read()
lines = file.readlines()
words = content.split()
w = len(words)
lines = content.splitlines()
l =len(lines)
char = len(content)
print("Number of words in an article is",w)
print("Number of lines in an article is",l)
print("Number of characters in an article is:",char)
file.close()
