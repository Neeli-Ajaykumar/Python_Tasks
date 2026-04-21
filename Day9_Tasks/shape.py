""". Shape Area Calculator (Polymorphism) 
A graphics application needs to calculate the area of different shapes. Create classes 
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate 
polymorphism by calling the same method for different objects."""

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
c = Circle(10)
r = Rectangle(10,20)
t = Triangle(10,20)

print("Area for Circle is:", c.area())
print("Area for Rectangle is:", r.area())
print("Area for Triangle is:", t.area())
