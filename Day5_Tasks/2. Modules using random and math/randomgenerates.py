"""Write a Python program that generates 20 random numbers between 1 and 200 using 
the random module and store them in a list. 
Then using the math module, compute and display: 
● Maximum value 
● Minimum value 
● Square root of the maximum number 
● Logarithm of the minimum number"""


import random
from math import sqrt, log
num = []
for i in range(20):
    num.append(random.randrange(1,200))
print(num)
max_value = max(num)
min_value = min(num)
square_root = sqrt(max_value)
logarithm = log(min_value)
print("The maximum value of the random list is:",max_value)
print("The minimum value of the random list is:",min_value)
print("The Square Root of the Maximum value is:",square_root)
print("The logaritham value of the minimum value is:",logarithm)
