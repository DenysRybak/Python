from abc import ABC




def abstractmetjod(args):
    pass


class AbstractAnimalHome(ABC):

    # ініціалізовуємо атрибути обєктів
    def __init__(self, name: str, location: str, area: str):
        self.name = name
        self.location = location
        self.area = area
        self.favorite_food = set()

    def __iter__(self):
        return iter(self.favorite_food_set)

    # створюємо метод для виведення інфи
    @abstractmetjod
    def description(self):
        pass

    # створюємо метод для перерахування витрат на місяць
    @abstractmetjod
    def calculate_cost_per_month(self):
        pass

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}


