class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

class Car(Vehicle):
    def drive_on_road(self):
        print(f"{self.brand} is driving on the road.")


class Boat(Vehicle):
    def sail_on_water(self):
        print(f"{self.brand} is sailing on water.")

class AmphibiousVehicle(Car, Boat):
    def transform_mode(self, mode):
        print(f"Transforming to {mode} mode.")

amphi = AmphibiousVehicle("Gibbs Quadski")


amphi.start()            
amphi.drive_on_road()    
amphi.sail_on_water()    
amphi.transform_mode("boat")  
