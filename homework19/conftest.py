import pytest

from Lecture17.HW16_MagicMethods import Passenger, TrainCar

@pytest.fixture
def new_traincar():
    train_london = TrainCar(2, 2)
    yield train_london


@pytest.fixture
def passenger1():
    print("renamed")
    yield Passenger("Alexander", 1, "London")


@pytest.fixture
def full_train():
    return TrainCar(1, 2)  # Поезд с максимальной вместимостью 2 пассажира


@pytest.fixture
def passenger2():
    return Passenger("IVAN", 2, "London")

@pytest.fixture
def passenger3():
    return Passenger("SERYI", 1, "London")

