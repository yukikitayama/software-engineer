from enum import Enum


class BookStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOANED = 3
    LOST = 4


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELLED = 3
    BANNED = 4


class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


MAX_BOOKS_ISSUED_TO_A_USER = 5
MAX_LENDING_DAYS = 10