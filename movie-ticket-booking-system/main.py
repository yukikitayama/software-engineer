from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime


class BookingStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CHECKED_IN = 4
    CANCELED = 5
    ABANDONED = 6


class Person:
    def __init__(self, name, address, email, phone, account):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.account = account


class Customer(Person):
    def make_booking(self, booking):
        pass

    def get_bookings(self):
        pass


class Guest:
    def register_account(self):
        pass


class Show:
    def __init__(self, show_id, played_at, movie, start_time, end_time):
        self.show_id = show_id
        self.played_at = played_at
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.created_at = datetime.now()


class Booking:
    def __init__(self, booking_number, status, show, payment, number_of_seats, show_seats):
        self.booking_number = booking_number
        self.show = show
        self.payment = payment
        self.status = status
        self.number_of_seats = number_of_seats
        self.show_seats = show_seats
        self.created_at = datetime.now()

    def make_payment(self, payment):
        pass

    def cancel(self):
        pass

    def assign_seats(self, seats):
        pass


class Cinema:
    def __init__(self, name, number_of_cinema_halls, address, halls):
        self.name = name
        self.number_of_cinema_halls = number_of_cinema_halls
        self.address = address
        self.halls = halls


# Interface
class Search(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass


class Catalog(Search):
    def __init__(self):
        self.title_to_movies = {}

    def search_by_title(self, title):
        return self.title_to_movies[title]


