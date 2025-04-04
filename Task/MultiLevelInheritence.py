class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.name} vehicle is starting...")

    def stop(self):
        print(f"{self.name} vehicle is stopped...")

class Car(Vehicle):
    def __init__(self, name, brand, color, model):
        super().__init__(name, brand, color)
        self.model = model

    def drive(self):
        print(f"Driving {self.name} {self.brand} {self.model} in {self.color} color.")

class ElectricCar(Car):
    def __init__(self, name, brand, color, model, battery_capacity):
        super().__init__(name, brand, color, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.model}. Battery capacity: {self.battery_capacity} kWh.")


my_tesla = ElectricCar("Electric Car", "Tesla", "White", "Model S", 100)

my_tesla.start()     
my_tesla.stop()      
my_tesla.charge()    
my_tesla.drive()     
