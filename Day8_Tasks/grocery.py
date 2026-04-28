""". Grocery List Manager 
A user wants to save grocery items in a file grocery.txt. Write a Python program that 
takes multiple items from the user and writes them into the file, with each item on a 
new line. 

Item = input("Enter grocery items:")
with open("grocery.txt", "a") as file:
    file.write(Item + "\n")
print("\nGrocerys items are:")
with open("grocery.txt", "r") as file:
    content = file.read()
    print(content)"""


file = open("grocery.txt", "w")

print("Enter grocery items (type 'done' to stop):")

while True:
    item = input("Item: ")
    
    if item.lower() == "done":
        break
    
    file.write(item + "\n")

file.close()

print("Grocery list saved successfully!")
