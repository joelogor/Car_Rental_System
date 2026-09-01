from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_car_service
from app.exceptions.user_excepton import UnauthorizedException, InvalidCredentialsException
from app.schemas.requests.add_car_request import AddCarRequest
from app.schemas.responses.add_car_response import AddCarResponse
from app.services.car_services import CarService

car_router = APIRouter(prefix="/car_api",tags=["Car Service"])

@car_router.post("/car/{username}", response_model=AddCarResponse)
def add_car(
        request_data: AddCarRequest,
        username: str,
        service : CarService = Depends(get_car_service)
):
    try:
        return service.add_car(request_data,username)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=str(error.message))

    except UnauthorizedException as error:
        raise HTTPException(status_code=401, detail=str(error.message))
