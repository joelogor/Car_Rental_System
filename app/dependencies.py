from fastapi import Depends
from sqlmodel import Session

from app.core.database import get_session
from app.repositories.car_repository import CarRepository
from app.repositories.rental_repository import RentalRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_services import AuthService
from app.services.car_services import CarService
from app.services.rental_services import RentalService


def get_user_repository(session : Session = Depends (get_session)) -> UserRepository:
    return UserRepository(session)

def get_auth_service(user_repository : UserRepository = Depends(get_user_repository)):
    return AuthService(user_repository)

def get_car_repository(session : Session = Depends (get_session)) -> CarRepository:
    return CarRepository(session)

def get_car_service(
        user_repository : UserRepository = Depends(get_user_repository),
        car_repository : CarRepository = Depends(get_car_repository)):
    return CarService(user_repository=user_repository, car_repository=car_repository)

def get_rental_repository(session : Session = Depends (get_session)) -> RentalRepository:
    return RentalRepository(session)

def get_rental_service(
        user_repository : UserRepository = Depends(get_user_repository),
        car_repository : CarRepository = Depends(get_car_repository),
        rental_repository : RentalRepository = Depends(get_rental_repository)):
    return RentalService(user_repository=user_repository, car_repository=car_repository, rental_repository=rental_repository)