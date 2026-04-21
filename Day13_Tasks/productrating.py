""" Product Rating Normalization 
Ratings from different users: 
ratings = np.array([2, 3, 4, 5, 1]) 
Task: 
● Normalize ratings to a range 0 to 1 using: 
normalized = (value - min) / (max - min) """

import numpy as np

ratings = np.array([2, 3, 4, 5, 1])
print("Ratings:", ratings)

min_val = min(ratings)
max_val = max(ratings)

normalized = [float((value - min_val) / (max_val - min_val)) for value in ratings]
print("Normalized Ratings:", normalized)

