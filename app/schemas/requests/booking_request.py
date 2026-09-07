from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field

class BookingRequest(BaseModel):
    username: str
    car_plate_number : str
    price : Decimal
    rental_datetime : datetime = Field(default_factory=datetime.now)
    expected_return_date : datetime


