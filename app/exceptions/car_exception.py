class CarNotFoundException(Exception):
    def __init__(self,message="Car not found"):
        self.message = message

class InvalidCarStateException(Exception):
    def __init__(self,message="Invalid car state"):
        self.message = message

class CarAlreadyExistsException(Exception):
    def __init__(self,message="Car already exists"):
        self.message = message