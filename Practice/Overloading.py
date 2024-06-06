class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, c, d):
        return a + b + c + d

# Create an instance of the Calculator class
calc = Calculator()

# Test the overloaded methods
print("Adding two numbers:", calc.add(3, 4))            # Calls the add(a, b) method
print("Adding three numbers:", calc.add(3, 4, 5))       # Calls the add(a, b, c) method
print("Adding four numbers:", calc.add(3, 4, 5, 6))     # Calls the add(a, b, c, d) method
