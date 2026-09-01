from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_auth_service
from app.exceptions.user_excepton import UsernameAlreadyExistsException, EmailAlreadyExistsException, \
    InvalidCredentialsException
from app.schemas.requests.login_request import LoginUserRequest
from app.schemas.requests.logout_request import LogoutUserRequest
from app.schemas.requests.register_request import RegisterUserRequest
from app.schemas.responses.login_reponse import LoginUserResponse
from app.schemas.responses.logout_response import LogoutUserResponse
from app.schemas.responses.register_response import RegisterUserResponse
from app.services.auth_services import AuthServices

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post("/register", response_model=RegisterUserResponse)
def register(
        request_data: RegisterUserRequest,
        service : AuthServices = Depends(get_auth_service),
):
    try:
        return service.register(request_data)

    except UsernameAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=error.message)

    except EmailAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=error.message)

@auth_router.post("/login", response_model=LoginUserResponse)
def login(
        request_data: LoginUserRequest,
        service : AuthServices = Depends(get_auth_service)

):
    try:
        return service.login(request_data)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=error.message)

@auth_router.post("/logout", response_model=LogoutUserResponse)
def logout(
        request_data: LogoutUserRequest,
        service : AuthServices = Depends(get_auth_service)
):
    try:
        return service.logout(request_data)
    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=error.message)