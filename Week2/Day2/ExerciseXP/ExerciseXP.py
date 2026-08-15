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



