from  abc import ABC, abstractmethod

class AbstractAnimalHome(ABC):

    # ініціалізовуємо атрибути обєктів
    def __init__(self, name, location, area):
        self.name = name
        self.location = location
        self.area = area

    # створюємо метод для виведення інфи
    @abstractmethod
    def description(self):
        pass


    # створюємо метод для перерахування витрат на місяць
    @abstractmethod
    def  calculate_cost_per_month(self):
        pass
