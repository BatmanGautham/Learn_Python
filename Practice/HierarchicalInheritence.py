class Vehicle():
    def Parent_method(self):
        print("\nParent : This is from Vehicle class!\n")

class Car(Vehicle):
    def Child1(self):
        print("\n This is from Car class!\n")

class Bike(Vehicle):
    def Child2(self):
        print("\nThis is from Bike class!\n")

class Bus(Vehicle):
    def Child3(self):
        print("\nThis is from Bus class!\n")


obj1 = Vehicle()
obj2 = Car()
obj3 = Bike()
obj4 = Bus()


obj1.Parent_method()
obj2.Child1()
obj3.Child2()
obj4.Child3()

obj2.Parent_method()
obj3.Parent_method()
obj4.Parent_method()

