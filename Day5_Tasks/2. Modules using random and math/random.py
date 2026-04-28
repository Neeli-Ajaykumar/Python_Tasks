"""Write a Python program using the random module to generate 10 random integers 
between 1 and 100 and store them in a list. Print the list."""
import random
num = []
for i in range(10):
    num.append(random.randrange(1,100))
print(num)
