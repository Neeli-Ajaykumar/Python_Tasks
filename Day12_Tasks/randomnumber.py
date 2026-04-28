"""Random Sales Simulation 
Scenario: 
A company wants to simulate 10 days of sales (range 100–500). 
Task: 
● Generate random integers using NumPy. 
● Print the array. 
● Find the average sales"""

import numpy as np

sales = np.random.randint(100, 500, 10)
print("Sales:", sales)

avg = sum(sales) / len(sales)
print("Average Sales:", avg)

