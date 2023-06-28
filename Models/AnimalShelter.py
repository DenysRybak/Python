from Models.AbstractAnimalHome import AbstractAnimalHome


class AnimalShelter(AbstractAnimalHome):
    _default_Farm = None

    @staticmethod
    def get_instance():
        if AnimalShelter._default_Farm is None:
            AnimalShelter._default_Zoo = AnimalShelter()
        return AnimalShelter._default_Zoo

    # ініціалізовуємо атрибути обєктів
    def __init__(self, name, location, area, number_animals,money_for_repair):
        super().__init__(name, location, area)
        self.favorite_food_set = {"pork"}
        self.number_animals = number_animals
        self.money_for_repair = money_for_repair
        self.description()

    # реалізація методу
    def description(self):
        print("Name: " + self.name + " Location: " + self.location + " Area: " + str(self.area) + " number_animals: " + str(
            self.number_animals) + " Money for repair:" + str(self.number_animals))

    # метод конвертації обєкта у стрічку
    def __str__(self):
        return f"AnimalShelter: {self.name}, Location: {self.location}, Area: {self.area}, number_animals: {self.number_animals}"


    # реалізація методу для рахування витрат
    def calculate_cost_per_month(self):
        print("Money for by food for AnimalShelter : " + str(self.money_for_repair))


