class Animals:
    """Класс по созданию животных"""

    def __init__(self, rod, vid):
        self.rod = rod
        self.vid = vid
        # print("Животное создано")

    def detachment(self):
        if self.rod == "Хищник":
            print(f"{self.rod} {"Имеет клыки"}")
        else:
            print(f"{self.rod} {"Имеет копыта"}")

    def behaviour(self):
        if self.vid == "Гепард":
            print(f"{self.vid} {"Охотиться"}")
        elif self.vid == "Корова":
            print(f"{self.vid} {"Охотиться"}")


# animal = Animals("Хищник", "Гепард")
animal_1 = Animals("Травоядное", "Корова")
# print(animal.rod)
print(f"{animal_1.rod} {animal_1.vid}")

# animal.detachment()
# animal_1.detachment()
# animal.behaviour()
# animal_1.behaviour()
