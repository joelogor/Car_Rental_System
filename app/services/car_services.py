from app.exceptions.car_exception import CarNotFoundException, InvalidCarStateException, CarAlreadyExistsException
from app.exceptions.user_excepton import InvalidCredentialsException, UnauthorizedException
from app.models.car import Car
from app.models.enums.car_state import CarState
from app.models.enums.role import Role
from app.repositories.user_repository import UserRepository
from app.schemas.requests.add_car_request import AddCarRequest
from app.schemas.requests.update_car_request import UpdateCarRequest
from app.schemas.responses.add_car_response import AddCarResponse
from app.schemas.responses.update_car_response import UpdateCarResponse


class CarService:
    def __init__(self,car_repository,user_repository:UserRepository):
        self._car_repository = car_repository
        self._user_repository = user_repository

    def add_car(self,car_request : AddCarRequest):
        existing_user = self._user_repository.find_by_username(car_request.username.lower())

        if not existing_user:
            raise InvalidCredentialsException()

        if existing_user.is_logged_in is False:
            raise UnauthorizedException()

        if existing_user.role != Role.FLEET_MANAGER:
            raise UnauthorizedException("You are not allowed to access this resource")

        existing_car = self._car_repository.find_by_plate_number(car_request.plate_number)

        if existing_car:
            raise CarAlreadyExistsException("Car with plate number {} already exists".format(car_request.plate_number))

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

    def update_car_state(self,update_car_request : UpdateCarRequest):
        existing_user = self._user_repository.find_by_username(update_car_request.username.lower())

        if not existing_user:
            raise InvalidCredentialsException()

        if existing_user.is_logged_in is False:
            raise UnauthorizedException()

        if existing_user.role != Role.FLEET_MANAGER:
            raise UnauthorizedException("You are not allowed to access this resource")

        car = self._car_repository.find_by_plate_number(update_car_request.plate_number)

        if not car:
            raise CarNotFoundException("Car with plate number {} not found".format(update_car_request.plate_number))

        if car.car_state == CarState.RENTED:
            raise InvalidCarStateException()

        if car.car_state == CarState.AVAILABLE:
            car.car_state = CarState.MAINTENANCE
            self._user_repository.save(car)
        else:
            car.car_state = CarState.AVAILABLE
            self._user_repository.save(car)

        response = UpdateCarResponse(
            brand=car.brand,
            model=car.model,
            release_year=car.release_year,
            plate_number=car.plate_number,
            car_state=car.car_state
        )

        return response