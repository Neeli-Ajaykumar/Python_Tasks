# Write a program using the built-in function len() to find the length of a list.
def len(list):
    count = 0
    for i in list:
        count += 1
    return count
list = [10, 20, 30, 40, 50]
length = len(list)
print("The length of the list is:", length)
