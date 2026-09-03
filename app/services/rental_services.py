from app.exceptions.car_exception import CarNotFoundException, InvalidCarStateException
from app.exceptions.user_excepton import InvalidCredentialsException, UnauthorizedException
from app.models import Rental
from app.models.enums.car_state import CarState
from app.models.enums.role import Role
from app.repositories.car_repository import CarRepository
from app.repositories.rental_repository import RentalRepository
from app.repositories.user_repository import UserRepository
from app.schemas.requests.booking_request import BookingRequest


class RentalService:
    def __init__(self,user_repository : UserRepository,car_repository : CarRepository,rental_repository : RentalRepository):
        self._user_repository = user_repository
        self._car_repository = car_repository
        self._rental_repository = rental_repository

    def create_booking(self,booking_request : BookingRequest):
        existing_user = self._user_repository.find_by_username(booking_request.sold_by)

        if not existing_user:
            raise InvalidCredentialsException()

        if existing_user.is_logged_in is False:
            raise UnauthorizedException()

        if existing_user.role == Role.FLEET_MANAGER:
            raise UnauthorizedException("You are not authorized to make a booking")

        car = self._car_repository.find_by_plate_number(booking_request.car_plate_number)

        if not car:
            raise CarNotFoundException("Car with plate number {} not found".format(booking_request.car_plate_number))

        if car.car_state == CarState.MAINTENANCE or car.car_state == CarState.RENTED:
            raise InvalidCarStateException()

        rental_details = Rental(
            car_id=car.car_id,
            customer_name=booking_request.customer_name,
            customer_phone_number=booking_request.customer_phone_number,
            customer_address=booking_request.customer_address,
            customer_email=booking_request.customer_email,
            sold_by_id=existing_user.id,

        )


