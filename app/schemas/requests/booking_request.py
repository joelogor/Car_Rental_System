from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field

class BookingRequest(BaseModel):
    customer_name : str
    customer_phone_number : str
    customer_email : EmailStr
    customer_address : str
    car_plate_number : str
    sold_by : str
    price : Decimal
    rental_datetime : datetime = Field(default_factory=datetime.now)
    expected_return_date : datetime


