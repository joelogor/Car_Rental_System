import pytest
from sqlmodel import Session

from app.exceptions.user_excepton import InvalidCredentialsException, UnauthorizedException
from app.models.enums.car_brand import CarBrand
from app.models.enums.car_model import CarModel
from app.models.enums.release_year import ReleaseYear
from app.models.enums.role import Role
from app.repositories.car_repository import CarRepository
from app.repositories.user_repository import UserRepository
from app.schemas.requests.add_car_request import AddCarRequest
from app.schemas.requests.login_request import LoginUserRequest
from app.schemas.requests.logout_request import LogoutUserRequest
from app.schemas.requests.register_request import RegisterUserRequest
from app.schemas.responses.login_reponse import LoginUserResponse
from app.services.auth_services import AuthService
from app.services.car_services import CarService


class TestCarServices:

    @pytest.fixture
    def setup_dependencies(self,session:Session):
        user_repository = UserRepository(session)
        car_repository = CarRepository(session)
        car_service = CarService(car_repository,user_repository)
        return user_repository, car_repository, car_service

    @pytest.fixture
    def user(self,setup_dependencies : tuple):
        user_repository, _, _ = setup_dependencies
        auth_service = AuthService(user_repository)

        user_request = RegisterUserRequest(
            full_name="onwere grace",
            username="gracey",
            email="lifeisTuff@gmail.com",
            password='12345678',
            role=Role.FLEET_MANAGER
        )
        login_request = LoginUserRequest(
            username='gracey',
            password='12345678',
        )
        auth_service.register(user_request)

        response = auth_service.login(login_request)

        return response

    def test_create_car_service(self,setup_dependencies : tuple):

        _, _, car_service = setup_dependencies

        assert car_service is not None

    def test_add_car(self,setup_dependencies : tuple,user : LoginUserResponse):

        user_repository, car_repository, car_service = setup_dependencies

        car_request =AddCarRequest(
            brand=CarBrand.LEXUS,
            model=CarModel.RX350,
            release_year = ReleaseYear.YEAR_2015,
            plate_number = "0101"
        )
        car_service.add_car(car_request,user.username)

        assert user_repository.count() == 1
        assert car_repository.count() == 1
        assert user.logged_in is True

    def test_add_car_with_fake_user(self,setup_dependencies : tuple):

        user_repository, car_repository, car_service = setup_dependencies
        fake_user = "fake_user"
        car_request = AddCarRequest(
            brand=CarBrand.LEXUS,
            model=CarModel.RX350,
            release_year=ReleaseYear.YEAR_2015,
            plate_number="0101"
        )

        with pytest.raises(InvalidCredentialsException):
            car_service.add_car(car_request,fake_user)

        assert user_repository.count() == 0
        assert car_repository.count() == 0


    def test_add_car_with_user_not_logged_in(self,setup_dependencies : tuple,user : LoginUserResponse):

        user_repository, car_repository, car_service = setup_dependencies

        auth_service = AuthService(user_repository)

        logout_request = LogoutUserRequest(
            username=user.username
        )

        response = auth_service.logout(logout_request)

        car_request = AddCarRequest(
            brand=CarBrand.LEXUS,
            model=CarModel.RX350,
            release_year=ReleaseYear.YEAR_2015,
            plate_number="0101"
        )

        with pytest.raises(UnauthorizedException):

            car_service.add_car(car_request,response.username)









