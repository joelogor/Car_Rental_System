
from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from app.models.car import Car


class CarRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, car: Car):
        self.session.add(car)
        self.session.commit()
        self.session.refresh(car)

        return car
    def get_by_id(self, car_id: str):
        statement = select(Car).where(Car.id == car_id)
        return self.session.scalar(statement)

    def get_all(self):
        statement = select(Car).order_by(Car.id)
        return self.session.scalars(statement).all()

    def update(self, car: Car):
        existing_car = self.get_by_id(car.id)

        if existing_car is None:
            return None

        existing_car.model = car.model
        existing_car.brand = car.brand
        existing_car.release_year = car.release_year
        existing_car.car_state = car.car_state
        existing_car.plate_number = car.plate_number
        existing_car.total_car_number = car.total_car_number

        self.session.commit()
        self.session.refresh(existing_car)

        return existing_car

    def remove(self, car_id: str):
        existing_car = self.get_by_id(car_id)

        if existing_car is None:
            return None

        self.session.delete(existing_car)
        self.session.commit()

        return existing_car


    def remove_all(self):
        statement = select(Car)
        cars = list(self.session.scalars(statement).all())

        for car in cars:
            self.session.delete(car)

        self.session.commit()

        return cars
