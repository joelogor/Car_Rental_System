from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql.coercions import expect

from app.dependencies import get_car_service
from app.exceptions.car_exception import CarNotFoundException, InvalidCarStateException, CarAlreadyExistsException
from app.exceptions.user_excepton import UnauthorizedException, InvalidCredentialsException
from app.schemas.requests.add_car_request import AddCarRequest
from app.schemas.requests.update_car_request import UpdateCarRequest
from app.schemas.responses.add_car_response import AddCarResponse
from app.schemas.responses.update_car_response import UpdateCarResponse
from app.services.car_services import CarService

car_router = APIRouter(prefix="/car_api",tags=["Car Service"])

@car_router.post("/car", response_model=AddCarResponse)
def add_car(
        request_data: AddCarRequest,
        service : CarService = Depends(get_car_service)
):
    try:
        return service.add_car(request_data)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=str(error.message))

    except UnauthorizedException as error:
        raise HTTPException(status_code=401, detail=str(error.message))

    except CarAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=str(error.message))

@car_router.patch("/update", response_model=UpdateCarResponse)
def update_car(
        request_data: UpdateCarRequest,
        service : CarService = Depends(get_car_service)
):
    try:
        return service.update_car_state(request_data)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=str(error.message))

    except UnauthorizedException as error:
        raise HTTPException(status_code=401, detail=str(error.message))

    except CarNotFoundException as error:
        raise HTTPException(status_code=404, detail=str(error.message))

    except InvalidCarStateException as error:
        raise HTTPException(status_code=400, detail=str(error.message))