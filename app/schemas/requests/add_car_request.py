from pydantic import BaseModel

from app.models.enums.car_brand import CarBrand
from app.models.enums.car_model import CarModel
from app.models.enums.release_year import ReleaseYear

class AddCarRequest(BaseModel):
    brand : CarBrand
    model : CarModel
    release_year : ReleaseYear
    plate_number : str
    username : str
