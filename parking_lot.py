from enum import Enum


class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3


class Vehicle:
    def __init__(self, license, maker, type_of_vehicle):
        self.license = license
        self.maker = maker
        self.type_of_vehicle = type_of_vehicle

    def get_type(self):
        return self.type_of_vehicle

    def __eq__(self, other):
        if (
            self.license == other.license
            and self.maker == other.maker
            and self.type_of_vehicle == other.typer_of_vehicle
        ):
            return True
        else:
            return False


class Car(Vehicle):
    def __init__(self, license, maker):
        super().__init__(license, maker, VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self, license, maker):
        super().__init__(license, maker, VehicleType.BIKE)


class BUS(Vehicle):
    def __init__(self, license, maker):
        super().__init__(license, maker, VehicleType.BUS)


class Slot:
    def __init__(self, lane, spot_number, type_of_vehicle):
        self.lane = lane
        self.spot_number = spot_number
        self.vehicle = None
        self.type_of_vehicle = type_of_vehicle

    def is_available(self):
        return self.vehicle is None

    def park(self, vehicle) -> bool:
        if vehicle.type_of_vehicle == vehicle.type_of_vehicle:
            self.vehicle = vehicle
            return True
        else:
            return False

    def remove_vehicle(self):
        self.vehicle = None

    def get_vehicle(self):
        return self.vehicle



# https://github.com/nikuamit/ParkingLot/blob/master/solution/parking_lot.py
# From Car class


if __name__ == "__main__":
    car = Car("ABC", "Toyota")
    print(car.license, car.maker, car.type_of_vehicle)
