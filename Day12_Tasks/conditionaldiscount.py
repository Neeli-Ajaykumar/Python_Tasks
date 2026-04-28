"""Conditional Discount System (List Comprehension) 
A shop has prices: 
prices = [100, 200, 300, 400] 
Scenario: 
● Apply a 10% discount only if price > 200. 
Task: 
● Use list comprehension with condition to create updated price list. """

prices = [100, 200, 300, 400]
print(prices)
updated_price = [p * 0.9 if p > 200 else p for p in prices]
print(updated_price)
