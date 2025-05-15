from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str ):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, spec):
        super().__init__(make, model, spec)

    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")

class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        super().__init__(make, model, spec)

    def start_engine(self):
        print(f"{self.make} {self.model}: Motor started")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model, spec = "US Spec"):
        return Car(make, model, spec)
    
    def create_motorcycle(self, make, model, spec = "US Spec"):
        return Motorcycle(make, model, spec)
    
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model, spec = "EU Spec"):
        return Car(make, model, spec)
    
    def create_motorcycle(self, make, model, spec = "EU Spec"):
        return Motorcycle(make, model, spec)

if __name__ == "__main__":
    us_ford = USVehicleFactory().create_car("Ford", "Mustang")
    eu_merc = EUVehicleFactory().create_car("Mercedes", "AMG")

    print(f'{us_ford.make} {us_ford.model} ({us_ford.spec})')
    print(f'{eu_merc.make} {eu_merc.model} ({eu_merc.spec})')
