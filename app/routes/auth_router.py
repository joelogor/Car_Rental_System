from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_auth_service
from app.exceptions.user_excepton import UsernameAlreadyExistsException, EmailAlreadyExistsException, \
    InvalidCredentialsException, UnauthorizedException
from app.schemas.requests.create_staff_request import CreateStaffRequest
from app.schemas.requests.login_request import LoginUserRequest
from app.schemas.requests.logout_request import LogoutUserRequest
from app.schemas.requests.register_request import RegisterUserRequest
from app.schemas.requests.update_profile_request import UpdateProfileRequest
from app.schemas.responses.create_staff_response import CreateStaffResponse
from app.schemas.responses.login_reponse import LoginUserResponse
from app.schemas.responses.logout_response import LogoutUserResponse
from app.schemas.responses.register_response import RegisterUserResponse
from app.schemas.responses.update_profile_response import UpdateProfileResponse
from app.services.auth_services import AuthService

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post("/customer", response_model=RegisterUserResponse)
def register_customer(
        request_data: RegisterUserRequest,
        service : AuthService = Depends(get_auth_service)
):
    try:
        return service.register_customer(request_data)

    except UsernameAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=error.message)

    except EmailAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=error.message)

@auth_router.post("/staff", response_model=CreateStaffResponse)
def register_staff(
        request_data: CreateStaffRequest,
        service : AuthService = Depends(get_auth_service)
):
    try:
        return service.register_staff(request_data)

    except UsernameAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=error.message)

    except EmailAlreadyExistsException as error:
        raise HTTPException(status_code=400, detail=error.message)

@auth_router.post("/login", response_model=LoginUserResponse)
def login(
        request_data: LoginUserRequest,
        service : AuthService = Depends(get_auth_service)

):
    try:
        return service.login(request_data)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=error.message)

@auth_router.post("/logout", response_model=LogoutUserResponse)
def logout(
        request_data: LogoutUserRequest,
        service : AuthService = Depends(get_auth_service)
):
    try:
        return service.logout(request_data)
    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=error.message)

@auth_router.patch("/update_profile", response_model=UpdateProfileResponse)
def update_profile(
        request_data: UpdateProfileRequest,
        service : AuthService = Depends(get_auth_service)
):
    try:
        return service.update_profile(request_data)

    except InvalidCredentialsException as error:
        raise HTTPException(status_code=400, detail=error.message)

    except UnauthorizedException as error:
        raise HTTPException(status_code=400, detail=error.message)