class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year

    def get_description(self):
        description = f"\n{self.brand} {self.model} ({self.get_year})"
        print(description)
        return description

    def start_engine(self):
        engine_status = "Двигатель запущен"
        print(engine_status)
        return engine_status

    @property
    def __set_year(self):
        __edited_year = int(self._year) + 1
        return __edited_year

    @property
    def get_year(self):
        official_year = self.__set_year
        return official_year

class ElectroCar(Car):

    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        engine_status = "Электродвигатель запущен"
        print(engine_status)
        return engine_status

    def get_battery_info(self):
        battery_info = f"Емкость батареи: {self.battery_capacity} кВтч"
        print(battery_info)
        return battery_info


class Vehicle(Car):

    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def get_load_info(self):
        load_capacity_info = f"Грузоподъемность: {self.load_capacity} т"
        print(load_capacity_info)
        return load_capacity_info


car = Car("car_brand", "car_model", "1998")
electrocar = ElectroCar("electrocar_brand", "electrocar_model", "2021", "135")
car.get_description()
car.start_engine()
electrocar.get_description()
electrocar.start_engine()
electrocar.get_battery_info()

vehicle = Vehicle("vehicle_brand", "vehicle_model", "2004", "20")
vehicle.get_description()
vehicle.start_engine()
vehicle.get_load_info()
