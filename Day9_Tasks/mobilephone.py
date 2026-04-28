"""Online Shopping System (Multilevel Inheritance) 
An e-commerce company organizes products using multiple levels. Create classes 
Product → ElectronicProduct → MobilePhone using multilevel inheritance and 
display product details. """

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)

class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand
        
    def display_electronic(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, storage, camera):
        self.name = name
        self.price = price
        self.brand = brand
        self.storage = storage
        self.camera = camera

    def display_mobile(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Storage:", self.storage)
        print("Camera:", self.camera)

phone = MobilePhone("smartphone", 100000, "apple", "256GB", "64MP")
phone.display_mobile()

    
