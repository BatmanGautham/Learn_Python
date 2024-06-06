class Vehicle():
    def Parent_method(self):
        print("\nThis is from Vehicle class!\n")

class Car(Vehicle):
    def Child_method(self):
        print("\nThis is from Car class!\n")


obj1 = Vehicle()
obj2 = Car()

obj1.Parent_method()
obj2.Child_method()

obj2.Parent_method()