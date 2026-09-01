from app.exceptions.user_excepton import UsernameAlreadyExistsException, EmailAlreadyExistsException, \
    InvalidCredentialsException, UnauthorizedException
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.requests.logout_request import LogoutUserRequest
from app.schemas.requests.register_request import RegisterUserRequest
from app.schemas.requests.login_request import LoginUserRequest
from app.schemas.requests.update_profile_request import UpdateProfileRequest
from app.schemas.responses.logout_response import LogoutUserResponse
from app.schemas.responses.register_response import RegisterUserResponse
from app.schemas.responses.login_reponse import LoginUserResponse
from app.schemas.responses.update_profile_response import UpdateProfileResponse


class AuthService:
    def __init__(self, repository : UserRepository):
        self._user_repository = repository

    def register(self, request_data: RegisterUserRequest) -> RegisterUserResponse:
        existing_username = self._user_repository.find_by_username(request_data.username.lower())
        existing_email = self._user_repository.find_by_email(request_data.email.lower())

        if existing_username:
            raise UsernameAlreadyExistsException()

        if existing_email:
            raise EmailAlreadyExistsException()


        user = User(
            username=request_data.username.lower(),
            full_name=request_data.full_name,
            email=request_data.email.lower(),
            password=request_data.password,
            role=request_data.role
        )

        new_user = self._user_repository.save(user)

        response = RegisterUserResponse(
            user_id=new_user.id,
            username=new_user.username,
            email=new_user.email,
            role=new_user.role,
            message='Registered successfully'
        )

        return response


    def login(self,login_user_request: LoginUserRequest ) -> LoginUserResponse:
        existing_user = self._user_repository.find_by_username(login_user_request.username.lower())

        if not existing_user:
            raise InvalidCredentialsException()

        if login_user_request.password != existing_user.password:
            raise InvalidCredentialsException()
        else:
            existing_user.is_logged_in = True
            self._user_repository.save(existing_user)

        login_user_response = LoginUserResponse(
            username=existing_user.username,
            logged_in=existing_user.is_logged_in,
            role=existing_user.role
        )
        return login_user_response

    def logout(self,logout_request: LogoutUserRequest) -> LogoutUserResponse:
        existing_user = self._user_repository.find_by_username(logout_request.username.lower())

        if not existing_user:
            raise InvalidCredentialsException()

        existing_user.is_logged_in = False
        self._user_repository.save(existing_user)

        logout_response = LogoutUserResponse(
            username=existing_user.username,
            message='Logged out successfully'
        )

        return logout_response

    def update_profile(self,update_request : UpdateProfileRequest) -> UpdateProfileResponse:
        existing_user = self._user_repository.find_by_username(update_request.username.lower())

        if not existing_user:
            raise InvalidCredentialsException()

        if existing_user.is_logged_in is False:
            raise UnauthorizedException()

        update_data = update_request.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(existing_user, key, value)

        self._user_repository.save(existing_user)

        response: UpdateProfileResponse = UpdateProfileResponse(
            full_name=existing_user.full_name,
            email=existing_user.email,
            password=existing_user.password,
            username=existing_user.username
        )

        return response
