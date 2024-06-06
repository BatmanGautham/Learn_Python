class Vehicle:
    def vehicle_method(self):
        print("This is a method from the Vehicle class")

class Car(Vehicle):
    def car_method(self):
        print("This is a method from the Car class")

class Bike(Vehicle):
    def bike_method(self):
        print("This is a method from the Bike class")

class Engine(Car, Bike):
    def engine_method(self):
        print("This is a method from the Engine class")

class HybridVehicle(Car):
    def hybrid_method(self):
        print("This is a method from the HybridVehicle class")

car = Car()
bike = Bike()
engine = Engine()
hybrid_vehicle = HybridVehicle()

car.car_method()
car.vehicle_method()

bike.bike_method()
bike.vehicle_method()

engine.engine_method()
engine.car_method()
engine.bike_method()
engine.vehicle_method()

hybrid_vehicle.hybrid_method()
hybrid_vehicle.car_method()
hybrid_vehicle.vehicle_method()
