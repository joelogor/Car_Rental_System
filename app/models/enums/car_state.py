from enum import StrEnum ,auto

class CarState(StrEnum):
    AVAILABLE = auto()
    RENTED = auto()
    MAINTENANCE =auto()
