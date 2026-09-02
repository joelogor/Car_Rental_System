from pydantic import BaseModel

from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState


class AddCarRequest(BaseModel):
    model: CarModel
    brand: CarBrand
    release_year: int
    car_state: CarState
    plate_number: str
    total_car_number: int