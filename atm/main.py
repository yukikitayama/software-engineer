from enum import Enum


class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSITE_CHECK, WITHDRAW, TRANSFER = 1, 2, 3, 4, 5


# Transaction status
# Customer status
# Address
# Customer
# Card


class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.total_balance = 0.0
        self.available_balance = 0.0

    def get_available_balance(self):
        return self.available_balance


class CheckingAccount(Account):
    def __init__(self, debit_card_number, account_number):
        super().__init__(account_number)
        self.debit_card_number = debit_card_number


# Saving account
# Bank


class Screen:
    def __init__(self):
        pass

    def show_message(self):
        pass


class ATM:
    def __init__(self, id_, location):
        self.id_ = id_
        self.location = location
        self.screen = Screen()
        # cash dispenser
        # keypad
        # printer
        # check deposit slot
        # cash deposit slot

    def authenticate_user(self):
        pass

    def make_transaction(self, customer, transaction):
        pass


# Cash dispenser
# Keypad
# printer
# check deposit slot
# cash deposit slot


class Transaction:
    def __init__(self, id_, creation_date, status):
        self.id_ = id_
        self.creation_date = creation_date
        self.status = status

    def make_transaction(self):
        pass


class BalanceInquiry(Transaction):
    def __init__(self, account_id, transaction_id, creation_date, status):
        super().__init__(transaction_id, creation_date, status)
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id


# Deposit transaction
# Check deposit transaction
# Cash deposit transaction
# Withdraw transaction
# Transfer transaction
