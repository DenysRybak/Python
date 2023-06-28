from Models.AbstractAnimalHome import AbstractAnimalHome
from Models.FoodExpection import FoodUnavailableException, NotEnoughFoodException
from Models.Zoo import Zoo
from Models.Farm import Farm
from Models.AnimalShelter import AnimalShelter
from Models.Cover import Cover

class AnimalHomeManager:
    def __init__(self):
        self.animal_homes = []
        self.food_available = True
        self.food_quantity = 0

    # метод додавання обєкту у клас
    def add_animal_home(self, animal_home):
        if isinstance(animal_home, AbstractAnimalHome):
            self.animal_homes.append(animal_home)
        else:
            print("Not added object")

    # перевизначений маг.метод який повертає кількість об'єктів в animal_homes.
    def __len__(self):
        return len(self.animal_homes)

    # перевизначений маг.метод який дозволяє отримати об'єкт з animal_homes за допомогою індексу.
    def __getitem__(self, index):
        return self.animal_homes[index]

    # перевизначений маг.метод який повертає ітератор для ітерації через об'єкти в animal_homes.
    def __iter__(self):
        return iter(self.animal_homes)

    def main(self):
        # Створення об'єктів класів Zoo та Farm
        zoo1 = Zoo("Askania nova", "Lviv", 932, 71, "9 AM - 6 PM", 3400)
        farm1 = Farm("Pig life", "Kyiv", 567, "Pig farm", 321)
        animal_shelter = AnimalShelter("Blago", "Kharkiv", 124, 81, 471)
        cover1 = Cover("Pet friends", "Lviv", 231, "9:00 - 21:00", 1240)

        # Створення списку де зберігаються об'єкти (zoo1 і farm1)
        animal_homes = []

        # Додавання об'єктів до списку
        animal_homes.append(zoo1)
        animal_homes.append(farm1)
        animal_homes.append(animal_shelter)
        animal_homes.append(cover1)

        # Виведення даних на екран зі списку
        for animal_home in animal_homes:
            print(animal_home)
            animal_home.calculate_cost_per_month()

        # Знаходження об'єктів з площею більше 400
        found_names = self.find_animal_home_by_area(animal_homes, 400)
        if found_names:
            print("\nAnimal homes with area greater than 400:")
            for name in found_names:
                print(name)
        else:
            print("\nNo found.")

        # знаходження обєктів за містом
        found_names = list(filter(lambda x: x.location == "Lviv", animal_homes))
        if found_names:
            print("\nAnimal homes located in Lviv:")
            for name in found_names:
                print(name.name)
        else:
            print("\nNo found")

        # виведення результату роботи list comprehension
        results = self.calculate_results(animal_homes)
        print("\nResults work list comprehension:")
        for result in results:
            print(result)

        # результат роботи enumerate
        concatenated_objects = self.concatenate_objects_with_enumerate(animal_homes)
        print("\nConcatenated objects with enumerate:")
        for obj in concatenated_objects:
            print(obj)

        # результат роботи zip
        concatenated_objects_with_zip = self.concatenate_objects_with_zip(animal_homes)
        print("\nConcatenated objects (zip):")
        for obj in concatenated_objects_with_zip:
            print(obj)

        # результат роботи all та any
        conditions = {"all": all(animal_home.area > 500 for animal_home in animal_homes),
                      "any": any(animal_home.location == "Lviv" for animal_home in animal_homes)}

        print("\nConditions:")
        for key, value in conditions.items():
            print(f"{key}: {value}")

    # метод пошуку обєкту за локацією
    def find_animal_home_by_location(self, animal_homes, location):
        found_names = [animal_home.name for animal_home in animal_homes if animal_home.location == location]
        return found_names

    #  метод пошуку обєкту за плошею
    def find_animal_home_by_area(self, animal_homes, area):
        found_names = [animal_home.name for animal_home in animal_homes if animal_home.area > area]
        return found_names

    #Обчислює результати роботи
    def calculate_results(self, animal_homes):
        results = [animal_home.calculate_cost_per_month() for animal_home in animal_homes]
        return results

    #Об'єднує об'єкти за їх індексами
    def concatenate_objects_with_enumerate(self, animal_homes):
        concatenated_objects = [f"{index}: {animal_home}" for index, animal_home in enumerate(animal_homes)]
        return concatenated_objects

    #Об'єднує об'єкти з результатами роботи
    def concatenate_objects_with_zip(self, animal_homes):
        results = self.calculate_results(animal_homes)
        concatenated_objects = [f"{animal_home}: {result}" for animal_home, result in zip(animal_homes, results)]
        return concatenated_objects

    def feed_animal(self):
        if not self.food_available:
            raise FoodUnavailableException('Food is currently unavailable')
        if self.food_quantity < 1:
            raise NotEnoughFoodException('Not enough food available')

        self.food_quantity -= 1
        print('Animal has been fed')


# Створємо об'єкт AnimalHomeManager і викликаємо метод main()
manager = AnimalHomeManager()
manager.main()

zoo = Zoo("Askania nova", "Lviv", 932, 71, "9 AM - 6 PM", 3400)
zoo.feed_animal()

