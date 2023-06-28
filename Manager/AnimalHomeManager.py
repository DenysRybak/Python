import AbstractAnimalHome
from Zoo import Zoo
from Farm import Farm
from AnimalShelter import AnimalShelter
from Cover import Cover

class AnimalHomeManager:

    # метод додавання обєкту у клас
    def add_animal_home(self, animal_home):
        if isinstance(animal_home, AbstractAnimalHome):
            self.animal_homes.append(animal_home)
        else:
            print("Not added object")



    def main(self):
        # Створення об'єктів класів Zoo та Farm
        zoo1 = Zoo("Askania nova", "Lviv", 932, 71, "9 AM - 6 PM", 3400)
        farm1 = Farm("Pig life","Kyiv", 567, "Pig farm", 321)
        animal_shelter = AnimalShelter("Blago", "Kharkiv",124, 81, 471)
        cover1 = Cover ("Pet friends","Lviv", 231, "9:00 - 21:00", 1240)


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
        found_names = list(filter(lambda x: x.location == "Львів", animal_homes))
        if found_names:
            print("\nAnimal homes located in Lviv:")
            for name in found_names:
                print(name.name)
        else:
            print("\nNo found")


    # метод пошуку обєкту за локацією
    def find_animal_home_by_location(self, animal_homes, location):
        found_names = [animal_home.name for animal_home in animal_homes if animal_home.location == location]
        return found_names


   #  метод пошуку обєкту за плошею
    def find_animal_home_by_area(self, animal_homes, area):
        found_names = [animal_home.name for animal_home in animal_homes if animal_home.area > area]
        return found_names


# Створємо об'єкт AnimalHomeManager і викликаємо метод main()
manager = AnimalHomeManager()
manager.main()
