import pytest
from pydantic import ValidationError
from sqlmodel import Session

from app.exceptions.user_excepton import UsernameAlreadyExistsException, EmailAlreadyExistsException, \
    InvalidCredentialsException, UnauthorizedException
from app.repositories.user_repository import UserRepository
from app.models.enums.role import Role
from app.schemas.requests.login_request import LoginUserRequest
from app.schemas.requests.logout_request import LogoutUserRequest
from app.schemas.requests.register_request import RegisterUserRequest
from app.schemas.requests.update_profile_request import UpdateProfileRequest
from app.services.auth_services import AuthService

class TestAuthServices:

    @pytest.fixture
    def user_repository(self,session : Session) -> UserRepository:
        return UserRepository(session)

    @pytest.fixture
    def auth_service(self, user_repository : UserRepository):
        return AuthService(user_repository)

    def test_create_auth_service(self, user_repository : UserRepository, auth_service : AuthService):

        assert auth_service is not None

    def test_register_user(self, user_repository : UserRepository, auth_service : AuthService):

        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        register_response = auth_service.register(user_request)

        assert user_repository.count() == 1

        assert register_response.username == user_request.username


    def test_register_user_with_missing_fields(self, user_repository : UserRepository, auth_service : AuthService):
        with pytest.raises(ValidationError):
            RegisterUserRequest(
                username="gracey",
                email="lifeisTuff@gmail.com",
                password='12345678',
                role=Role.FRONT_DESK,
            )

    def test_register_two_users_with_same_username_throws_exception(self, user_repository : UserRepository, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        user_two_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        with pytest.raises(UsernameAlreadyExistsException):
            auth_service.register(user_two_request)

    def test_register_user_with_duplicate_email(self, user_repository : UserRepository, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        user_two_request = RegisterUserRequest(
            full_name="onwere grace",
            username="fakegrace",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        with pytest.raises(EmailAlreadyExistsException):
            auth_service.register(user_two_request)

    def test_register_two_users(self, user_repository: UserRepository, auth_service: AuthService):
        user_request = RegisterUserRequest(
            full_name="Oluyemi Isire",
            username="Zoe",
            email="zoecomfort@gmail.com",
            password='yemiZoe09!',
            role=Role.FLEET_MANAGER,
        )

        auth_service.register(user_request)

        user_two_request = RegisterUserRequest(
            full_name="Onwere Grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.ADMIN
        )

        auth_service.register(user_two_request)

        assert user_repository.count() == 2

    def test_login_user(self, user_repository : UserRepository, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        login_request = LoginUserRequest(
            username='gracey',
            password='12345678',
        )

        login_response = auth_service.login(login_request)

        assert login_response.logged_in is True

    def test_login_fake_user(self, user_repository : UserRepository, auth_service : AuthService):

        login_request = LoginUserRequest(
            username='fakegrace',
            password='567890eee',
        )

        with pytest.raises(InvalidCredentialsException):
            auth_service.login(login_request)

    def test_login_user_with_password_mismatch(self, user_repository : UserRepository, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        login_request = LoginUserRequest(
            username='gracey',
            password='123456789',
        )

        with pytest.raises(InvalidCredentialsException):
            auth_service.login(login_request)

    def test_logout_user(self, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        login_request = LoginUserRequest(
            username='gracey',
            password='12345678',
        )

        auth_service.login(login_request)

        logout_request = LogoutUserRequest(

            username='gracey',
        )

        response = auth_service.logout(logout_request)

        assert response.message == 'Logged out successfully'

    def test_update_fake_user_throws_exception(self, auth_service : AuthService):

        update_request = UpdateProfileRequest(
            username='fakegrace212',
            email='lifeisSoft@gmail.com',
            password='121245678'
        )

        with pytest.raises(InvalidCredentialsException):
            auth_service.update_profile(update_request)

    def test_update_user(self, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        login_request = LoginUserRequest(
            username='gracey',
            password='12345678',
        )

        auth_service.login(login_request)

        update_request = UpdateProfileRequest(
            username='gracey',
            email='lifeisSoft@gmail.com',
            password='121245678'
        )

        response = auth_service.update_profile(update_request)

        assert response.email == update_request.email
        assert response.username == update_request.username
        assert response.password == update_request.password

    def test_update_user_not_logged_in_throws_exception(self, auth_service : AuthService):
        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FRONT_DESK,
        )

        auth_service.register(user_request)

        update_request = UpdateProfileRequest(
            username='gracey',
            email='lifeisSoft@gmail.com',
            password='121245678'
        )

        with pytest.raises(UnauthorizedException):
            auth_service.update_profile(update_request)