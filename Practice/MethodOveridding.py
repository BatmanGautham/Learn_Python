import math as m

class Shape:
    def area(self):
        pass  # Placeholder method, to be overridden by subclasses

    def perimeter(self):
        pass  # Placeholder method, to be overridden by subclasses

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


circle = Circle()
square = Square()

print("Circle - Radius: 5")
print("Area:", circle.area(5))
print("Perimeter:", circle.perimeter(5))

print("\nSquare - Side length: 4")
print("Area:", square.area(4))
print("Perimeter:", square.perimeter(4))
