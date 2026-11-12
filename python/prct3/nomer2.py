class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_description(self):
        return f"Транспортное средство: {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def get_description(self):
        return f"Легковой автомобиль: {self.brand} {self.model}, количество дверей: {self.doors}"


class Bicycle(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def get_description(self):
        return f"Велосипед: {self.brand} {self.model}, тип: {self.bike_type}"


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def get_description(self):
        return f"Грузовик: {self.brand} {self.model}, грузоподъемность: {self.load_capacity} т"


# Демонстрация полиморфизма:
vehicles = [
    Car("Toyota", "Camry", 4),
    Bicycle("Trek", "Marlin 5", "горный"),
    Truck("Volvo", "FH16", 20)
]

for vehicle in vehicles:
    print(vehicle.get_description())