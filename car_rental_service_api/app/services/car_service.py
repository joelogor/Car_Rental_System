from app.models.car import Car
from app.repositories.car_repository import CarRepository


class CarService:

    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository

    def save_car(self, car: Car) :
        return self.car_repository.save(car)

    def get_car_by_id(self, car_id: str):
        return self.car_repository.get_by_id(car_id)

    def get_all_cars(self):
        return self.car_repository.get_all()

    def update_car(self, car: Car):
        return self.car_repository.update(car)

    def remove_car(self, car: Car):
        return self.car_repository.remove(car)

    def remove_all_cars(self):
        return self.car_repository.remove_all()




