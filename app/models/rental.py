import uuid

from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional
from decimal import Decimal
from app.models.enums.rental_status import RentalStatus

class Rental(SQLModel,table=True):
    id : UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    car_id : UUID = Field(foreign_key='car.id')
    customer_name : str
    customer_phone_number : str
    customer_address : str
    customer_email : str
    sold_by_id: UUID = Field(foreign_key='user.id',index=True)
    price : Decimal
    rental_datetime : datetime = Field(default_factory=datetime.now)
    expected_return_date : datetime
    actual_return_date: Optional[datetime] = None
    is_active: RentalStatus = Field(default=RentalStatus.ACTIVE)