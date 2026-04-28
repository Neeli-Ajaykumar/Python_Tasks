#Write a program to remove duplicate elements from a list.
"""li = [10,20,30,30,40,20,50]
list = list(set(li))
print("After removing the dublicate values:",list)"""

#using loops
li = [10,20,30,30,40,50,20]
list = []
for item in li:
    if item not in list:
        list.append(item)

print("List after removing duplicates:", list)
