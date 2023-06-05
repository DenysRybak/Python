from Manager.AnimalHomeManager import AnimalHomeManager
from Models.AnimalShelter import AnimalShelter


class SetManager:
    def __init__(self, AnimalHomeManager):
        self.regular_manager = AnimalHomeManager
        self.total_length = sum(len(animal.favorite_food_set) for animal in AnimalHomeManager.animal_homes)

    # Перевизначений метод який дозволяє ітерувати по множині
    def __iter__(self):
        for animal_home in self.regular_manager.animal_homes:
            if isinstance(animal_home, AnimalShelter):
                yield from animal_home.favorite_food_set

    #  Перевизначений метод який повертає загальну довжину множини
    def __len__(self):
        return self.total_length

    # Перевизначений метод який дозволяє отримувати елементи множини
    def __getitem__(self, index):
        if index < 0 or index >= self.total_length:
            raise IndexError("Index out of range")

        for animal_home in self.regular_manager.animal_homes:
            if isinstance(animal_home, AnimalShelter):
                if index < len(animal_home.favorite_food_set):
                    return list(animal_home.favorite_food_set)[index]
                index -= len(animal_home.favorite_food_set)

    # Метод, який дозволяє ітерувати по множині за допомогою ітератора
    def __next__(self):
        for animal_home in self.regular_manager.animal_homes:
            if isinstance(animal_home, AnimalShelter):
                for food in animal_home.favorite_food_set:
                    yield food



regular_manager = AnimalHomeManager()

set_manager = SetManager(regular_manager)
for food in set_manager:
    print(food)

print(len(set_manager))
print(set_manager[10])
