import pytest
from Lecture17.HW16_MagicMethods import TrainCar, Passenger


@pytest.mark.regression
def test_add_passenger():
    TrainLondon = TrainCar(1, 5)
    Jonni = Passenger("Jonni D", 1, "London")
    TrainLondon.add_passenger(Jonni)
    assert len(TrainLondon.passengers_list) == 1


@pytest.mark.regression
def test_rename_passenger(passenger1):
    passenger1.name = "Gorohov"
    assert passenger1.name == "Gorohov"


@pytest.mark.smoke
@pytest.mark.xfail(reason="настраиваем(учим) выдачу ошибки")
def test_add_passengers_full_train(full_train, passenger1, passenger2, passenger3):
    # Добавляем двух пассажиров, чтобы заполнить поезд
    full_train.add_passenger(passenger1)
    full_train.add_passenger(passenger2)

    # Попытка добавить третьего пассажира должна вызвать ошибку
    with pytest.raises(ValueError, match=f"Вагон вже заповнений. Вільних місць нема."):
        full_train.add_passenger(passenger3)


@pytest.mark.regression
@pytest.mark.parametrize(
    'name_given, name_expected', [("Ivan", "Ivan"), ("Maks", "Maks"), ("Orist", "Oristrat")]
)
def test_rename_with_params(passenger1, name_given, name_expected):
    passenger1.name = name_given
    assert passenger1.name == name_expected