#Write a program to convert a tuple to a list and modify the element.
tuple = (10,20,30,40,50)
print(type(tuple))
list = list(tuple)
print("tuple is converted to list", type(list))
print("Before modifying the list:",list)
list[1] = 60
print("After modifying the list",list)
