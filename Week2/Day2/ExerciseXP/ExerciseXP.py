import random
## 🌟 Exercise 1: Pets
# Use the provided Pets and Cat classes to create a Siamese breed,
# instantiate cat objects, and use the Pets class to manage them.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name.title()} is just walking around"

""" Create 3 variety classes that inherits from the Cat class   """
class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"

""" Create Pets instances from all varieties """
bengal_obj = Bengal("Akamaru", 20)
chart_obj = Chartreux("Naruto", 21)
siamese_obj = Siamese("Sasuke", 22)

""" Create a list of cat instances"""
all_cats = [bengal_obj, chart_obj, siamese_obj]

""" Take cats for a walk"""
sara_pets = Pets(all_cats)
sara_pets.walk()

"""  🌟 Exercise 2: Dogs """

class Dog:
    """ Create the Dog Class """
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f'{self.name} wins'

        elif my_power < other_power:
            return f'{other_dog.name} wins'

        else:
            return "Its a tie"

""" Create Dog Instances """
dog_2 = Dog("Sakura", 5, 20)
dog_3 = Dog("Itachi", 7, 30)
dog_4 = Dog("Madara", 6, 40)

""" Test Dog Methods """
# print(dog_4.bark())
# print(dog_2.bark())
# print(dog_3.bark())
#
# print(dog_2.run_speed())
# print(dog_3.run_speed())
# print(dog_4.run_speed())
#
# print(dog_4.fight(dog_2))
# print(dog_3.fight(dog_2))
# print(dog_3.fight(dog_4))


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        Dog.__init__(self, name, age, weight)
        self.trained = trained


    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = []

        for dog in args:
            dog_names.append(dog.name)

        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):

        tricks = ["does a barrel roll",
                  "stands on his back legs",
                  "shakes your hand",
                  "plays dead"]

        if self.trained:
            random_index = random.randint(0, len(tricks) - 1)
            print(f"{self.name} {tricks[random_index]}")


pet = PetDog("Peter", 20, 15, True)
lis = [dog_2, dog_3, dog_4, pet]
pet.train()
pet.do_a_trick()
