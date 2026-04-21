#Write a program to check whether a key exists in a dictionary.
dict = {"1":"ajay",2:"chandu",3:"ram",4:"arun",5:"mahesh"}
key = int(input("Enter any thing:"))
#key = input("Enter any thing:")
if key in dict:
    print("Key exists in dictonary")
else:
    print("Key doesn't exists in dictonary")
