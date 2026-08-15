""" MANAGE A ZOO """

#Create a class called Animal
class Animal():
    def __init__(self, animal_name, food_consumption, food_type):
        self.name = animal_name
        self.food_consumption = food_consumption
        self.food_type = food_type

    def show_info(self):
        print(f'A {self.name.title()} eats {self.food_consumption} kg of '
              f'{self.food_type} per day')

#Create three classes for different animals
class Wolf(Animal):
    def __init__(self, animal_name):
        super().__init__(animal_name, 2, "meat")

class Parrot(Animal):
    def __init__(self, animal_name):
        super().__init__(animal_name, 0.2, "fruit")

class Chicken(Animal):
    def __init__(self, animal_name):
        super().__init__(animal_name, 0.15, "wheat")


animal1 = Wolf("wolf")
animal2 = Chicken("chicken")
animal3 = Parrot("parrot")
animal1.show_info()
animal2.show_info()
animal3.show_info()

