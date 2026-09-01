from uuid import UUID

from pydantic import BaseModel

from app.models.enums.car_brand import CarBrand
from app.models.enums.car_model import CarModel
from app.models.enums.car_state import CarState
from app.models.enums.release_year import ReleaseYear

class AddCarResponse(BaseModel):
    id : UUID
    brand: CarBrand
    model: CarModel
    release_year: ReleaseYear
    plate_number: str
    car_state : CarState