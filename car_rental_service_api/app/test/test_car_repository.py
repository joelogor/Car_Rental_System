from unittest import TestCase

from app.database import SessionLocal
from app.models.car import Car
from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState
from app.repositories.car_repository import CarRepository


class TestCarRepository(TestCase):
    def test_save_car(self):
        db = SessionLocal()

        try:
            repository = CarRepository(db)
            repository.remove_all()

            car = Car(
                model=CarModel.COROLLA,
                brand=CarBrand.TOYOTA,
                release_year=2016,
                car_state=CarState.AVAILABLE,
                plate_number= "0012",
                total_car_number=1

            )

            saved_car = repository.save(car)

            self.assertEqual(car, saved_car)


        finally:
            db.close()

    def test_get_car_by_id(self):
        db = SessionLocal()

        try:
            repository = CarRepository(db)
            repository.remove_all()

            car = Car(
                model=CarModel.COROLLA,
                brand=CarBrand.TOYOTA,
                release_year=2016,
                car_state=CarState.AVAILABLE,
                plate_number="0022",
                total_car_number=1
            )

            saved_car = repository.save(car)

            found_car = repository.get_by_id(saved_car.id)

            # self.assertIsNotNone(found_car)
            self.assertEqual(saved_car.id, found_car.id)

        finally:
            db.close()

    def test_get_all_cars(self):
        db = SessionLocal()

        try:
            repository = CarRepository(db)
            repository.remove_all()

            car1 = Car(
                model=CarModel.COROLLA,
                brand=CarBrand.TOYOTA,
                release_year=2016,
                car_state=CarState.AVAILABLE,
                plate_number="0033",
                total_car_number=1
            )

            car2 = Car(
                model=CarModel.CAMRY,
                brand=CarBrand.TOYOTA,
                release_year=2015,
                car_state=CarState.AVAILABLE,
                plate_number="0044",
                total_car_number=1
            )
            save_car1 = repository.save(car1)
            save_car2 = repository.save(car2)
            cars = repository.get_all()

            car_list = [save_car1, save_car2]
            self.assertEqual(cars, car_list)

        finally:
            db.close()

    def test_update_car(self):
        db = SessionLocal()


        try:
            repository = CarRepository(db)
            repository.remove_all()

            car = Car(
                model=CarModel.COROLLA,
                brand=CarBrand.TOYOTA,
                release_year=2016,
                car_state=CarState.AVAILABLE,
                plate_number="0055",
                total_car_number=1
            )

            saved_car = repository.save(car)

            saved_car.car_state = CarState.NOT_AVAILABLE

            updated_car = repository.update(saved_car)

            self.assertEqual(
                CarState.NOT_AVAILABLE,
                updated_car.car_state
            )

        finally:
            db.close()

    def test_remove_car(self):
        db = SessionLocal()

        try:
            repository = CarRepository(db)
            repository.remove_all()

            car = Car(
                model=CarModel.COROLLA,
                brand=CarBrand.TOYOTA,
                release_year=2016,
                car_state=CarState.AVAILABLE,
                plate_number="0077",
                total_car_number=1
            )

            saved_car = repository.save(car)

            removed_car = repository.remove(saved_car)

            self.assertEqual(saved_car.id, removed_car.id)

            found_car = repository.get_by_id(saved_car.id)

            self.assertIsNone(found_car)

        finally:
            db.close()

    def test_remove_all_cars(self):
        db = SessionLocal()

        try:
            repository = CarRepository(db)

            repository.remove_all()

            car1 = Car(
                model=CarModel.COROLLA,
                brand=CarBrand.TOYOTA,
                release_year=2016,
                car_state=CarState.AVAILABLE,
                plate_number="0088",
                total_car_number=1
            )

            car2 = Car(
                model=CarModel.CAMRY,
                brand=CarBrand.TOYOTA,
                release_year=2015,
                car_state=CarState.AVAILABLE,
                plate_number="0099",
                total_car_number=1
            )

            saved_car1 = repository.save(car1)
            saved_car2 = repository.save(car2)

            expected_cars = [saved_car1, saved_car2]

            deleted_cars = repository.remove_all()

            self.assertCountEqual(expected_cars, deleted_cars)

            remaining_cars = repository.get_all()

            self.assertEqual([], remaining_cars)

        finally:
            db.close()
