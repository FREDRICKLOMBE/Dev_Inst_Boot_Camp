# 🌟 Exercise 2: Dogs
# Goal:Create a Dog class with methods for barking, running speed, and fighting.


""" Step 1: Create the Dog Class """
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)

    def bark(self):
        return f"{self.name.title()} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        strongest_dog = other_dog[0]
        strongest_power = strongest_dog.run_speed() * strongest_dog.self.weight


        for dog in other_dog[1:]:
            power = dog.run_speed * self.weight
            if power > strongest_power:
                strongest_dog = dog
                strongest_power = power
                print(f"{self.name.title()} is the strongest with {power} KJ")

            if power == strongest_power:
                print(f"We have a tie!")


dog_1 = Dog("sakura", 10, 20)
print(dog_1.bark())
print(dog_1.run_speed())



dog_2 = Dog("gaara", 20, 25)
print(dog_2.bark())
print(dog_2.run_speed())

dog_3 = Dog("madara", 15, 27)
print(dog_3.bark())
print(dog_3.run_speed())

all_dogs = [dog_1, dog_2, dog_3]
dog_1.fight(all_dogs)