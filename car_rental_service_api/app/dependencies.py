from app.database import SessionLocal
from app.repositories.car_repository import CarRepository
from app.services.car_service import CarService


def get_car_service():
    session = SessionLocal()

    try:
        repository = CarRepository(session)
        service = CarService(repository)

        yield service

    finally:
        session.close()