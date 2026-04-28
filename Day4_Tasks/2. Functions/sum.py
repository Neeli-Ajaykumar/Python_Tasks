# Write a function to find the sum of elements in a list using a user-defined function.
def sum(list):
    total = 0    
    for i in list:
        total = total + i
    return total
    
list = [10,20,30,40,50]
result = sum(list)
print(result)
