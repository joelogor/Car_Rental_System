from app.exceptions.user_excepton import InvalidCredentialsException, UnauthorizedException
from app.models.car import Car
from app.models.enums.role import Role
from app.repositories.user_repository import UserRepository
from app.schemas.requests.add_car_request import AddCarRequest
from app.schemas.responses.add_car_response import AddCarResponse

class CarService:
    def __init__(self,car_repository,user_repository:UserRepository):
        self._car_repository = car_repository
        self._user_repository = user_repository

    def add_car(self,car_request : AddCarRequest,username : str):
        existing_user = self._user_repository.find_by_username(username.lower())

        if not existing_user:
            raise InvalidCredentialsException()

        if existing_user.is_logged_in is False:
            raise UnauthorizedException()

        if existing_user.role != Role.FLEET_MANAGER:
            raise UnauthorizedException("You are not allowed to access this resource")

        car = Car(
            brand=car_request.brand,
            model=car_request.model,
            release_year=car_request.release_year,
            plate_number=car_request.plate_number
        )

        new_car = self._car_repository.save(car)

        response = AddCarResponse(
            id=new_car.id,
            brand=new_car.brand,
            model=new_car.model,
            release_year=new_car.release_year,
            plate_number=new_car.plate_number,
            car_state=new_car.car_state
        )

        return response