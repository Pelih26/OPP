class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 55

    def description_person(self):
        """Получение описания человека"""
        description = f"{self.name},\nему - {self.age},\nего рост - {self.height},\nего вес - {self.weight}"
        print("Нашего человека зовут - " + description)

    def get_weight(self):
        """Получение веса человека"""
        print(f"Вес нашего человека - {self.weight}")

    def update(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс война"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родитель"""
        super().__init__(name, age, height)



# warrior = Warrior("Конон", 32, 200)
# warrior.update(150)
# warrior.description_person()


man = Person("Кирилл", 32, 180)
man.update(150)
# man.weight = 100
# man.description_person()
man.get_weight()




# woman = Person("Юлия", 35, 150)
#
# woman.description_person()