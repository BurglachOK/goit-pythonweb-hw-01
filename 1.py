from __future__ import annotations

import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logging.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (EU Spec)")


def main():
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicle1: Vehicle = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2: Vehicle = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()