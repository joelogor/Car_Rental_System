from app.models.car import Car
from app.repositories.car_repository import CarRepository
from app.schema.request.car_request import AddCarRequest


class CarService:

    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository

    def save_car(self, request: AddCarRequest) -> Car:
        car = Car(
            model=request.model,
            brand=request.brand,
            release_year=request.release_year,
            car_state=request.car_state,
            plate_number=request.plate_number,
            total_car_number=request.total_car_number
        )

        return self.car_repository.save(car)

    def get_car_by_id(self, car_id: str):
        return self.car_repository.get_by_id(car_id)

    def get_all_cars(self):
        return self.car_repository.get_all()

    def update_car(self, car_id: str, request: AddCarRequest):
        car = Car(
            id=car_id,
            model=request.model,
            brand=request.brand,
            release_year=request.release_year,
            car_state=request.car_state,
            plate_number=request.plate_number,
            total_car_number=request.total_car_number
        )

        return self.car_repository.update(car)

    def remove_car(self, car_id: str):
        return self.car_repository.remove(car_id)

    def remove_all_cars(self):
        return self.car_repository.remove_all()




