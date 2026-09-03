from uuid import UUID

from sqlmodel import Session, select
from app.models.car import Car
from app.models.enums.car_brand import CarBrand
from app.models.enums.car_state import CarState


class CarRepository:
    def __init__(self, session: Session):
        self._session = session

    def save(self,car: Car):
        self._session.add(car)
        self._session.commit()
        self._session.refresh(car)
        return car

    def find_by_id(self,car_id: UUID):
        return self._session.get(Car, car_id)

    def find_all(self):
        statement = select(Car)
        return self._session.exec(statement).all()

    def delete_by_id(self,car_id: UUID)-> bool:
        car = self.find_by_id(car_id)

        if car is not None:
            self._session.delete(car)
            self._session.commit()
            return True
        return False

    def count(self):
        cars = self.find_all()
        return len(cars)

    def find_by_brand(self,car_brand: CarBrand):
        statement = select(Car).where(Car.brand == car_brand)
        return self._session.exec(statement).all()

    def find_by_plate_number(self,plate_number: str):
        statement = select(Car).where(Car.plate_number == plate_number)
        return self._session.exec(statement).one_or_none()