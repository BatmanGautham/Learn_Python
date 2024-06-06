from abc import ABC, abstractmethod
import math as m

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def area(self, radius):
        return m.pi * radius**2

    def perimeter(self, radius):
        return 2 * m.pi * radius

class Square(Shape):
    def area(self, side):
        return side**2

    def perimeter(self, side):
        return 4 * side

# Create instances of Circle and Square
circle = Circle()
square = Square()

# Test the methods
radius = 5
side = 4

print("Circle - Radius:", radius)
print("Area:", circle.area(radius))
print("Perimeter:", circle.perimeter(radius))

print("\nSquare - Side length:", side)
print("Area:", square.area(side))
print("Perimeter:", square.perimeter(side))
