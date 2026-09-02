import uuid


from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, Integer, CHAR, String

from app.database import Base
from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState



class Car(Base):
    __tablename__ = "cars"

    id: Mapped[str] = mapped_column(
        CHAR(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    model: Mapped[CarModel] = mapped_column( SQLEnum(CarModel))
    brand: Mapped[CarBrand] = mapped_column( SQLEnum(CarBrand))
    release_year: Mapped[int] = mapped_column( Integer)
    car_state: Mapped[CarState] = mapped_column( SQLEnum(CarState))
    plate_number: Mapped[str] = mapped_column(String(20), unique=True,
    nullable=False)
    total_car_number: Mapped[int] = mapped_column(Integer)

