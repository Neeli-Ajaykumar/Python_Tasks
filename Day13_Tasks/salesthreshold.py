"""Sales Threshold Filtering 
You are given monthly sales: 
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000]) 
Task: 
● Filter all sales values greater than the average sales 
● Return the filtered array. """

import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
print("Before operations:", sales)

avg_sales = sum(sales) / len(sales)
print("Average sales:", avg_sales)

filtered_sales = sales[sales > avg_sales]
print("Filtered array:", filtered_sales)
