"""Exercise 3: Dogs Domesticated. Keep beside ExerciseXP.py."""

import random

from ExerciseXP import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # The exercise expects dog instances, not strings.
        dogs = [self.name] + [dog.name for dog in args]

        print(f"{', '.join(dogs)} all play together")

    def do_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead",
        ]

        if self.trained:
            print(f"{self.name} {tricks[random.randrange(len(tricks))]}")
        else:
            print(f"{self.name} needs training first")


if __name__ == "__main__":
    fido = PetDog("Fido", 2, 10)
    buddy = PetDog("Buddy", 4, 20)
    max_dog = PetDog("Max", 3, 15)

    fido.train()
    fido.play(buddy, max_dog)
    fido.do_a_trick()
