from fastapi import APIRouter, Depends

from app.dependencies import get_car_service
from app.models import Car
from app.schema.request.car_request import AddCarRequest
from app.services.car_service import CarService

router = APIRouter(
    prefix="/cars",
    tags=["Cars"]
)

@router.post("/")
def create_car(
    request: AddCarRequest,
    service: CarService = Depends(get_car_service)
):

    return service.save_car(request)

@router.get("/")
def get_all_cars(
    service: CarService = Depends(get_car_service)
):
    return service.get_all_cars()

@router.get("/{car_id}")
def get_car_by_id(
    car_id: str,
    service: CarService = Depends(get_car_service)
):
    return service.get_car_by_id(car_id)

@router.put("/{car_id}")
def update_car(
    car_id: str,
    request: AddCarRequest,
    service: CarService = Depends(get_car_service)
):
    return service.update_car(car_id, request)

@router.delete("/{car_id}")
def remove_car(
    car_id: str,
    service: CarService = Depends(get_car_service)
):
    return service.remove_car(car_id)

@router.delete("/")
def remove_all_cars(
    service: CarService = Depends(get_car_service)
):
    return service.remove_all_cars()