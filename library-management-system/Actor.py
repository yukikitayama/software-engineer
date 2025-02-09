from Type import *


class Account:
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.id = id
        self.password = password
        self.person = person
        self.status = status

    def reset_password(self):
        pass


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_book_item(self, book_item):
        pass

    def block_member(self, member):
        pass

    def un_block_member(self, member):
        pass


