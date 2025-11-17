from enum import Enum, auto

class Type(Enum):
    PAIN = auto()
    HORMONE = auto()
    DERM = auto()

class Status(Enum):
    ACTIVE = auto()
    DEACTIVATED = auto()

class API:
    def __init__(self, name, brand, boh):
        self.name = name
        self.brand = brand
        self.boh = boh
        self.status = Status.ACTIVE

    def get_name(self):
        return self.name

    def get_brand(self):
        return self.brand

    def deactivate(self):
        self.status = Status.DEACTIVATED

    def reactivate(self):
        self.status = Status.ACTIVE

    def get_boh(self):
        return self.boh
    
    def adjust_boh(self, amount):
        self.boh = amount

    def subtract_boh(self, amount):
        self.boh -= amount

    def add_boh(self, amount):
        self.boh += amount

class CreamBase:
    def __init__(self, name, brand, boh, type):
        self.name = name
        self.brand = brand
        self.boh = boh
        self.type = type
        self.status = Status.ACTIVE

    def get_name(self):
        return self.name
    
    def get_brand(self):
        return self.brand

    def get_boh(self):
        return self.boh
    
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