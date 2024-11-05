class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width
    def area(self):
        return self.length * self.width
square = Rectangle(5)

rectangle = Rectangle(4, 6)

print(f"Area of square: {square.area()}")
print(f"Area of rectangle: {rectangle.area()}")
