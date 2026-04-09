"""Inventory Update System 
A warehouse has an inventory stored in a matrix. 
[[10, 15], 
[20, 25]] 
Scenario: 
A new shipment increases every item quantity by 2 units. 
Task: 
● Add 2 to every element using NumPy. 
● Print the updated inventory. """

import numpy as np

warehouse = np.array([[10, 15], [20, 25]])
print("Before Adding:", warehouse)
print ("After Adding 2 units:", warehouse + 2)
