from AbstractAnimalHome import AbstractAnimalHome


class Farm(AbstractAnimalHome):
    _default_Farm = None

    @staticmethod
    def get_instance():
        if Farm._default_Farm is None:
            Farm._default_Zoo = Farm()
        return Farm._default_Zoo

    # ініціалізовуємо атрибути обєктів
    def __init__(self, name, location, area, typeq, money_for_farm_food):
        super().__init__(name, location, area)
        self.typeq = typeq
        self.money_for_farm_food = money_for_farm_food
        self.description()

    # реалізація методу
    def description(self):
        print("Name: " + self.name + " Location: " + self.location + " Area: " + str(self.area) + " Type: " + str(
            self.typeq) + " Money for farm food per month: " + str(self.money_for_farm_food))

    # метод конвертації обєкта у стрічку
    def __str__(self):
        return f"Farm: {self.name}, Location: {self.location}, Area: {self.area}, Capacity: {self.typeq}, Money for " \
               f"farm food per month: {self.money_for_farm_food}"

    # реалізація методу для рахування витрат для зоопарку
    def calculate_cost_per_month(self):
        print("Money for by food for  farm: " + str(self.money_for_farm_food * 30))
