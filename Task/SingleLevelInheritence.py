class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def start(self):
            print(f"{self.name} is starting...")

    def stop(self):
            print(f"{self.name} is stopped...")

class Car(Vehicle):

    def __init__(self, name, brand, color, model):
        super().__init__(name, brand, color)
        self.model = model

    def info(self):
        print(f"Car Info: Name: {self.name} Brand: {self.brand} Color: {self.color} Model: {self.model}")

my_car = Car("BMW","BMW Company","Blue","BM1")
my_car.start()
my_car.stop()
my_car.info()
        