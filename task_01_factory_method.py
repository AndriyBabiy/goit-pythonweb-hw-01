import logging
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s: Engine started", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s: Motor started", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str, spec: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str, spec: str) -> None:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model, spec="US Spec") -> Car:
        return Car(make, model, spec)

    def create_motorcycle(self, make, model, spec="US Spec") -> Motorcycle:
        return Motorcycle(make, model, spec)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model, spec="EU Spec") -> Car:
        return Car(make, model, spec)

    def create_motorcycle(self, make, model, spec="EU Spec") -> Motorcycle:
        return Motorcycle(make, model, spec)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    vehicle_1 = USVehicleFactory().create_car("Ford", "Mustang")
    vehicle_1.start_engine()

    vehicle_2 = EUVehicleFactory().create_motorcycle("Harley Davidson", "Sportster")
    vehicle_2.start_engine()
