class Animal():
    def __init__(self, name):
        self.name = name
        self.actions = ("sleeping", "eating")

    def sound(self):
        return''''''

class Dog(Animal):
    def sound(self):
        return "bark"

class Cat(Animal):
    def sound(self):
        return "meow"

animal_types = ["Dog", "Cat"]
animal_type = input(f"\nChoose your animal: ({(' or ').join(animal_types)})")
animal_name = input("pet's name")
print(f"Your animal's name is {animal_name}")

if animal_type == "Dog":
    animal = Dog(animal_name)
else:
    animal = Cat(animal_name)

print(f"{animal.name} says {animal.sound()}")