"""Develop a Python program for a small shop to process customer purchases. Store product 
names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
and product details using tuples. Create functions to display products, add items to the cart, and 
calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
name entered by the user does not exist)."""


products = {"pen": 10,"book": 50,"pencil": 5}
categories = {"Stationery"}
cart = []
def calculate_total(cart_items):
    if not cart_items:
        return 0
    item = cart_items[0]
    return (item[1] * item[2]) + calculate_total(cart_items[1:])

def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(name, ":", price)

def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        item = (name, products[name], quantity)
        cart.append(item)

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")
    except NameError:
        print("Product not found in store.")
    except TypeError:
        print("Cart data type error.")

def view_total():
    try:
        if not cart:
            print("Cart is empty.")
            return

        print("Items in Cart:")
        for item in cart:
            print(f"{item[0]} x {item[2]}")

        total = calculate_total(cart)

        print("Total Bill:", total)

    except ZeroDivisionError:
        print("Calculation error: division by zero.")
    except TypeError:
        print("Cart data type error.")

while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        display_products()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_total()
    elif choice == '4':
        print("Thank you!")
        break
    else:
        print("Invalid choice")
