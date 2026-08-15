""" 🌟 Example: Dog function! """
# Define a function called dog_name().
import random

dog_actions = ["sleeping", "eating", "barking"]

def dog_name(name):
    """ Print out the name of a dog """
    print(f"Your dog's name is {name}")

    # Randomise the choices
    choice = random.choice(dog_actions)

    print(f"\n{name.title()} is {choice}")

prompt = "\nWhat is your dog's name?:"
name = input(prompt)

dog_name(name)


while True:
    choice = random.choice(dog_actions)
    print(f"\n{name.title()} is {choice}")
    if input("Continue? (y/n) ").lower() != "y":
        break


