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
        return f"{self.name} is just walking around"

""" Create 3 variety classes that inherits from the Cat class   """
class Bengal(Cat):
    def sing(self, sounds):
        return sounds

class Chartreux(Cat):
    def sing(self, sounds):
        return sounds

class Siamese(Cat):
    def sing(self, sounds):
        return sounds

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
            return "It's a tie"

# Exercise 3 is in ExerciseXP_PetDog.py.

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(
                        "You are over 18, your parents Jane and John "
                        "accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

        print(f"{first_name} is not a member of this family.")

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for person in self.members:
            print(f"{person.first_name}, {person.age} years old")


if __name__ == "__main__":
    """ Create Pets instances from all varieties """
    bengal_obj = Bengal("Akamaru", 20)
    chart_obj = Chartreux("Naruto", 21)
    siamese_obj = Siamese("Sasuke", 22)

    """ Create a list of cat instances"""
    all_cats = [bengal_obj, chart_obj, siamese_obj]

    """ Take cats for a walk"""
    sara_pets = Pets(all_cats)
    sara_pets.walk()

    """ Create Dog Instances """
    dog_2 = Dog("Sakura", 5, 20)
    dog_3 = Dog("Itachi", 7, 30)
    dog_4 = Dog("Madara", 6, 40)

    """ Test Dog Methods """
    print(dog_4.bark())
    print(dog_2.bark())
    print(dog_3.bark())

    print(dog_2.run_speed())
    print(dog_3.run_speed())
    print(dog_4.run_speed())

    print(dog_4.fight(dog_2))
    print(dog_3.fight(dog_2))
    print(dog_3.fight(dog_4))

    smith_family = Family("Smith")

    smith_family.born("Alex", 20)
    smith_family.born("Maya", 15)
    smith_family.born("Sam", 18)

    smith_family.check_majority("Alex")
    smith_family.check_majority("Maya")
    smith_family.check_majority("Sam")
    smith_family.family_presentation()
