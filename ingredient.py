from enum import Enum, auto

class Form(Enum):
    POWDER = auto()
    CREAM = auto()

class Type(Enum):
    PAIN = auto()
    HORMONE = auto()

class Status(Enum):
    ACTIVE = auto()
    DEACTIVATED = auto()

class API:
    def __init__(self, name, brand, boh, form=Form.POWDER, status=Status.ACTIVE):
        self.name = name
        self.brand = brand
        self.boh = boh
        self.form = form
        self.status = status

    def adjust_boh(self, amount):
        self.boh = amount

    def subtract_boh(self, amount):
        self.boh -= amount

    def add_boh(self, amount):
        self.boh += amount

    def deactivate(self):
        self.status = Status.DEACTIVATED

    def reactivate(self):
        self.status = Status.ACTIVE

    def update_status(self):
        if self.boh <= 0 and self.status == Status.ACTIVE:
            self.deactivate()
        elif self.boh > 0 and self.status == Status.DEACTIVATED:
            self.reactivate()


class CreamBase:
    def __init__(self, name, brand, boh, type, form=Form.CREAM, status=Status.ACTIVE):
        self.name = name
        self.brand = brand
        self.boh = boh
        self.type = type
        self.form = form
        self.status = status
    
    def adjust_boh(self, amount):
        self.boh = amount

    def subtract_boh(self, amount):
        self.boh -= amount

    def add_boh(self, amount):
        self.boh += amount

    def deactivate(self):
        self.status = Status.DEACTIVATED

    def reactivate(self):
        self.status = Status.ACTIVE

    def update_status(self):
        if self.boh <= 0 and self.status == Status.ACTIVE:
            self.deactivate()
        elif self.boh > 0 and self.status == Status.DEACTIVATED:
            self.reactivate()
