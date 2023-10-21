class Passenger:
    def __init__(self, name, numbercar, station):
        self.name = name
        self.numbercar = numbercar
        self.station = station


class TrainCar:
    def __init__(self, number, max_capacity):
        self.number = number
        self.max_capacity = max_capacity
        self.passengers_list = {}

    def add_passenger(self, passenger):
        if len(self.passengers_list) < self.max_capacity:
            self.passengers_list[passenger.name] = passenger
        else:
            print(f"Вагон {self.number} вже заповнений. Вільних місць нема.")

    def __len__(self):
        return len(self.passengers_list)

    def __str__(self):
        passenger_info = ""
        for passenger_name, passenger in self.passengers_list.items():
            passenger_info += f"Passenger name: {passenger_name}\n"
            passenger_info += f"Numbercar: {passenger.numbercar}\n"
            passenger_info += f"Station: {passenger.station}\n\n"
        return f"TrainCar {self.number}:\n{passenger_info}"


class Train:
    def __init__(self):
        self.TrainCar_list = []

    def __len__(self):
        return len(self.TrainCar_list)

    def add_train_car(self, train_car):
        self.TrainCar_list.append(train_car)



# Створюємо пасажирів
John = Passenger("John Dow", 1, "London")
Alex = Passenger("Alex Dawson", 2, "Manchester")
Piter = Passenger("Piter Pen", 2, "West Ham")

# Створюємо вагони
TrainCar1 = TrainCar(1, 5)
TrainCar2 = TrainCar(2, 5)

# Додаємо пасажирів до вагонів
TrainCar1.add_passenger(John)
TrainCar2.add_passenger(Alex)
TrainCar2.add_passenger(Piter)
# Створюємо потяг
SuperTrain = Train()


# Додаємо вагони до потягу
SuperTrain.add_train_car(TrainCar1)
SuperTrain.add_train_car(TrainCar2)

print(len(TrainCar1))

print(len(TrainCar2))

print(TrainCar1)
print(TrainCar2)

print(SuperTrain)
