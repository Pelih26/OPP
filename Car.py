class Car():
    """Создаем автомобиль"""

    def __init__(self, model, age, volume_engine, price, mileage):
        """Инизиализация атрибутов автомобиля"""
        self.model = model
        self.age = age
        self.volume_engine = volume_engine
        self.price = price
        self.mileage = mileage
        self.wheel = 4

    def description_car(self):
        description = (f"Модель авто - {self.model}\n"
                       f"Год выпуска - {self.age} год\n"
                       f"Объём двигателя - {self.volume_engine} куб.см\n"
                       f"Цена - {self.price} руб.\n"
                       f"Пробег (км) - {self.mileage} км\n"
                       f"Количество колес - {self.wheel}")
        print(description)

class Truck(Car):
    """Создаем класс грузовик, наследуем втрибуты от класса автомобиль"""

    def __init__(self, model, age, volume_engine, price, mileage):
        """Инициализация атрибутов родительского класса"""
        super().__init__(model, age, volume_engine, price, mileage)
        self.wheel = 8


car = Car("ВАЗ", 2020, 2.0, 1000, 20000)     # Создаем экземпляр класса Авто
car.description_car()

truck = Truck("Камаз", 2022, 12, 5000, 300)  # Создаем экземпляр класса Грузовик
truck.description_car()
