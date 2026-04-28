"""Vehicle Management System (Inheritance) 
A transport company manages different vehicles. Create a base class Vehicle with 
attributes like brand and speed. Create derived classes Car and Bike that inherit from 
Vehicle and display their details. """

class Vehicle:
    def details(self):
        print("brand:", self.brand)
        print("speed:", self.speed)
        
class car(Vehicle):
    def display(self):
        print("The car is:")
        self.details()

class bike(Vehicle):
    def display(self):
        print("The bike is:")
        self.details()
d = car()
d1 = bike()

d.brand = "suzuki"
d.speed = 80

d1.brand = "honda"
d1.speed = 40

d.display()
print("---------------")
d1.display()
            
