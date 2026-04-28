"""Rectangle Area Calculator (Constructor) 
A geometry application needs to calculate the area of rectangles. Create a Rectangle 
class that uses a constructor to initialize length and width. Add a method to calculate 
and display the area."""

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of Rectangle is:", self.length * self.width)
r = rectangle(10,20)
r.area()
