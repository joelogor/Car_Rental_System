from fastapi import APIRouter, HTTPException, Depends

from app.dependencies import get_rental_service
from app.exceptions.car_exception import CarNotFoundException, InvalidCarStateException
from app.exceptions.user_excepton import InvalidCredentialsException, UnauthorizedException
from app.schemas.requests.booking_request import BookingRequest
from app.schemas.responses.booking_response import BookingResponse
from app.services.rental_services import RentalService

rental_router = APIRouter(prefix="/rental", tags=["Rental Service"])

@rental_router.post("/rent_car", response_model=BookingResponse)
def rent_car(
        request_data: BookingRequest,
        service : RentalService = Depends(get_rental_service),):

    try:
        return service.create_booking(request_data)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400,detail=str(error.message))

    except UnauthorizedException as error:
        raise HTTPException(status_code=401,detail=str(error.message))

    except CarNotFoundException as error:
        raise HTTPException(status_code=404,detail=str(error.message))

    except InvalidCarStateException as error:
        raise HTTPException(status_code=400,detail=str(error.message))