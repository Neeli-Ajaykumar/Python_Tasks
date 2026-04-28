#Write a program using the built-in max() function to find the largest number in a list.
def max(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest
list = [10,20,30,40,50,60,70]
largest_number = max(list)
print("The largest number in the list is:", largest_number)
