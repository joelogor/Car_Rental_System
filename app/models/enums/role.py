from enum import StrEnum, auto

class Role(StrEnum):
    FLEET_MANAGER = auto()
    FRONT_DESK = auto()
    ADMIN = auto()