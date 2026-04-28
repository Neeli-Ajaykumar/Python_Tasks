"""Data Processing Pipeline 
A data pipeline receives the following array: 
[12, 7, 25, 3, 18, 10] 
Scenario: 
1. Convert the list into a NumPy array. 
2. Sort the array. 
3. Split the sorted array into two equal parts. 
4. Calculate the sum of each part. 
Output: 
● Sorted array 
● Two split arrays 
● Sum of each part """

import numpy as np

arr = np.array([12, 7, 25, 3, 18, 10])
print("Before operations:", arr)

sorted_arr = np.sort(arr)
print("After sortting:", sorted_arr)

split_arr = np.array_split(sorted_arr, 2)
print("After splitting:", split_arr)

sum1 = np.sum(split_arr[0])
sum2 = np.sum(split_arr[1])

print("Sum of first part:", sum1)
print("Sum of second part:", sum2)
