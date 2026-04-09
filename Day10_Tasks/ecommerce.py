"""An e-commerce company stores product prices in a NumPy array. 
Scenario: 
Prices = [499, 299, 799, 199, 599]
Task: 
● Convert it into a NumPy array. 
● Sort the prices in ascending order. """

import numpy as np

prices = np.array([499, 299, 799, 199, 599])
print("Before sorting:", prices)
print("After sorting:", np.sort(prices))
