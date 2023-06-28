from Models.AbstractAnimalHome import AbstractAnimalHome


class Cover(AbstractAnimalHome):
    __default_Zoo = None

    @staticmethod
    def get_instance():
        if Cover._default_Zoo is None:
            Cover._default_Zoo = Cover()
        return Cover._default_Zoo

    # ініціалізовуємо атрибути обєктів
    def __init__(self, name, location, area, schedule, support_by_money):
        super().__init__(name, location, area)
        self.schedule = schedule
        self.support_by_money = support_by_money
        self.description()
        self.favorite_food_set = {"Feed for dogs and cats"}

    # реалізація методу
    def description(self):
        print("Name: " + self.name + " Location: " + self.location + " Area: " + str(self.area) + " schedule " + str(self.schedule) + " Support by money: " + str(self.support_by_money))

    # метод конвертації обєкта у стрічку
    def __str__(self):
        return f"Cover: {self.name}, Location: {self.location}, Area: {self.area}, schedule: {self.schedule}, Support by money: {self.support_by_money}"

    # реалізація методу для рахування витрат для
    def calculate_cost_per_month(self):
        print("Money for support cover " + str(self.support_by_money * 30))

