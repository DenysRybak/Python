from Models.AbstractAnimalHome import AbstractAnimalHome


class Zoo(AbstractAnimalHome):
    __default_Zoo = None

    @staticmethod
    def get_instance():
        if Zoo._default_Zoo is None:
            Zoo._default_Zoo = Zoo()
        return Zoo._default_Zoo

    # ініціалізовуємо атрибути обєктів
    def __init__(self, name, location, area, capacity, time_work, money_for_zoo):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.time_work = time_work
        self.money_for_zoo = money_for_zoo
        self.description()
        self.favorite_food_set = {"Meat"}

    # реалізація методу
    def description(self):
        print("Name: " + self.name + " Location: " + self.location + " Area: " + str(self.area) + " Capacity: " + str(
            self.capacity) + " Time work: " + str(self.time_work) + " Money for zoo: " + str(self.money_for_zoo))

    # метод конвертації обєкта у стрічку
    def __str__(self):
        return f"Zoo: {self.name}, Location: {self.location}, Area: {self.area}, Capacity: {self.capacity}, Time Work: {self.time_work}, Money for Zoo: {self.money_for_zoo}"

    # реалізація методу для рахування витрат для зоопарку
    def calculate_cost_per_month(self):
        print("Money for support zoo: " + str(self.money_for_zoo * 30))

