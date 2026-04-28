"""Shopping Cart System 
Scenario: A user adds items to a shopping cart. 
Task: 
● Store items in a list 
● Convert to set to remove duplicates 
● Use loop + condition to calculate total cost 
● Handle invalid input using try-except """


store_items = []
n = int(input("Enter number of items:"))
for i in range(n):
    items = input("Enter item names:")
    store_items.append(items)
print("store_items are:", store_items)

S = set(store_items)
print("Set:", S)

prices = {"apple": 50, "mango": 100, "pen": 10, "chocolates": 20}

total = 0
for items in store_items:
    if items in prices:
        total = total + prices[items]
print("Total cost:", total)

try:
    discount = int(input("Enter discount amount:"))
    final_amount = total - discount
    print("Final amount after discount is:", final_amount)

except:
    print("Invalid input discount must be a number")
