"""Multi-Level List Transformation (Advanced List Comprehension) 
A dataset contains: 
data = [[1, 2, 3], [4, 5], [6]] 
Task: 
● Flatten the list using list comprehension. 
● Then create a new list containing squares of only even numbers."""

data = [[1, 2, 3], [4, 5], [6]]

flat_list = []
for list in data:
    for num in list:
        flat_list.append(num)

even_squares = [num**2 for num in flat_list if num % 2 == 0]


print("Flattened List:", flat_list)
print("Even Squares:", even_squares)
