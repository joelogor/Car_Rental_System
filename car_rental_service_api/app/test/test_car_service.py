from unittest import TestCase
from unittest.mock import Mock

from app.models.car import Car
from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState
from app.schema.request.car_request import AddCarRequest
from app.services.car_service import CarService


class TestCarService(TestCase):

    def test_save_car(self):
        repository = Mock()

        request = AddCarRequest(
            model=CarModel.COROLLA,
            brand=CarBrand.TOYOTA,
            release_year=2016,
            car_state=CarState.AVAILABLE,
            plate_number="0011",
            total_car_number=1
        )

        car = Car(
            model=request.model,
            brand=request.brand,
            release_year=request.release_year,
            car_state=request.car_state,
            plate_number=request.plate_number,
            total_car_number=request.total_car_number
        )

        repository.save.return_value = car

        service = CarService(repository)

        saved_car = service.save_car(request)

        self.assertEqual(saved_car.model, request.model)
        self.assertEqual(saved_car.brand, request.brand)
        self.assertEqual(saved_car.release_year, request.release_year)
        self.assertEqual(saved_car.car_state, request.car_state)
        self.assertEqual(saved_car.plate_number, request.plate_number)
        self.assertEqual(saved_car.total_car_number, request.total_car_number)

    def test_get_car_by_id(self):
        repository = Mock()

        car = Car(
            model=CarModel.COROLLA,
            brand=CarBrand.TOYOTA,
            release_year=2016,
            car_state=CarState.AVAILABLE,
            plate_number="0011",
            total_car_number=1
        )

        repository.get_by_id.return_value = car

        service = CarService(repository)

        found_car = service.get_car_by_id(car.id)

        self.assertEqual(car, found_car)
        repository.get_by_id.assert_called_once_with(car.id)

    def test_get_all_cars(self):
        repository = Mock()

        car1 = Car(
            model=CarModel.COROLLA,
            brand=CarBrand.TOYOTA,
            release_year=2016,
            car_state=CarState.AVAILABLE,
            plate_number="0011",
            total_car_number=1
        )

        car2 = Car(
            model=CarModel.CAMRY,
            brand=CarBrand.TOYOTA,
            release_year=2018,
            car_state=CarState.AVAILABLE,
            plate_number="0022",
            total_car_number=1
        )

        expected_cars = [car1, car2]

        repository.get_all.return_value = expected_cars

        service = CarService(repository)

        actual_cars = service.get_all_cars()

        self.assertEqual(expected_cars, actual_cars)
        repository.get_all.assert_called_once_with()

    def test_update_car(self):
        repository = Mock()

        car = Car(
            model=CarModel.COROLLA,
            brand=CarBrand.TOYOTA,
            release_year=2016,
            car_state=CarState.AVAILABLE,
            plate_number="0011",
            total_car_number=1
        )

        repository.update.return_value = car

        service = CarService(repository)

        updated_car = service.update_car(car)

        self.assertEqual(car, updated_car)
        repository.update.assert_called_once_with(car)

    def test_remove_car(self):
        repository = Mock()

        car = Car(
            model=CarModel.COROLLA,
            brand=CarBrand.TOYOTA,
            release_year=2016,
            car_state=CarState.AVAILABLE,
            plate_number="0011",
            total_car_number=1
        )

        repository.remove.return_value = car

        service = CarService(repository)

        removed_car = service.remove_car(car)

        self.assertEqual(car, removed_car)
        repository.remove.assert_called_once_with(car)

    def test_remove_all_cars(self):
        repository = Mock()

        car1 = Car(
            model=CarModel.COROLLA,
            brand=CarBrand.TOYOTA,
            release_year=2016,
            car_state=CarState.AVAILABLE,
            plate_number="0011",
            total_car_number=1
        )

        car2 = Car(
            model=CarModel.CAMRY,
            brand=CarBrand.TOYOTA,
            release_year=2018,
            car_state=CarState.AVAILABLE,
            plate_number="0022",
            total_car_number=1
        )

        expected_cars = [car1, car2]

        repository.remove_all.return_value = expected_cars

        service = CarService(repository)

        deleted_cars = service.remove_all_cars()

        self.assertCountEqual(expected_cars, deleted_cars)
        repository.remove_all.assert_called_once_with()



