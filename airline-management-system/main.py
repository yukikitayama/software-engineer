from enum import Enum


class FligthStatus(Enum):
    ACTIVE = 1
    SCHEDULED = 2
    DELAYED = 3
    DEPARTED = 4
    LANDED = 5
    IN_AIR = 6
    ARRIVED = 7
    CANCELLED = 8
    DIVERTED = 9
    UNKNOWN = 10


# Payment status
# Reservation status
# Seat class
# Seat type
# Account status
# Address

# Account


class Person:
    def __init__(self, name, address, email, phone, account):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.account = account


class Customer(Person):
    def __init__(self, frequent_flyer_number, name, address, email, phone, account):
        super().__init__(name, address, email, phone, account)
        self.frequent_flyer_number = frequent_flyer_number

    def get_itineraries(self):
        pass


# Passenger


class Airport:
    def __init__(self, name, address, code):
        self.name = name
        self.address = address
        self.code = code

    def get_flights(self):
        pass


# Aircraft
# Seat
# Flight seat

# Schedule
# Flight
class Flight:
    def __init__(self, flight_number, departure, arrival, duration_in_minutes):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.duration_in_minutes = duration_in_minutes

        self.schedules = []
        self.flight_instances = []


# Flight instance
class FlightInstance:
    def __init__(self, departure_time, arrival_time, gate, status, aircraft):
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate
        self.status = status
        self.aircraft = aircraft

    def cancel(self):
        pass

    def update_status(self, status):
        pass


# Flight reservation
# Itinerary

