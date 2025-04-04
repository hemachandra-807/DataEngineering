class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is being driven.")

class Bike(Vehicle):
    def ride(self):
        print(f"{self.brand} bike is being ridden.")

car = Car("Toyota")
bike = Bike("Yamaha")

car.start()
car.drive()

bike.start()
bike.ride()
