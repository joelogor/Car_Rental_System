from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, EmailStr
from sqlmodel import Field
from app.models.enums.rental_status import RentalStatus
from app.models.enums.role import Role

class BookingResponse(BaseModel):
    customer_name: str
    customer_phone_number: str
    customer_email: EmailStr
    customer_address: str
    car_id : UUID
    sold_by: str
    user_role : Role
    price: Decimal
    rental_datetime: datetime = Field(default_factory=datetime.now)
    expected_return_date: datetime
    is_active: RentalStatus