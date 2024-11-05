from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape."""
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle: π * r^2"""
        return math.pi * self.radius ** 2
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """Calculate the area of a square: side^2"""
        return self.side_length ** 2
circle = Circle(7)
square = Square(4)
print(f"Area of the circle: {circle.area():.2f}")
print(f"Area of the square: {square.area()}")
