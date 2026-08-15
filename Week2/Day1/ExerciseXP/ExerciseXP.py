"""
                🌟 Exercise 1: Cats
Use the provided Cat class to create three cat objects.
Then, create a function to find the oldest cat and print its details.
"""
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

 # Create cat objects
cat1 = Cat('Akamaru', 14)
cat2 = Cat('Kiba', 16)
cat3 = Cat('Kabuto', 17)

 # Create a Function to Find the Oldest Cat
def oldest_cat(cart1, cart2, cart3):
    oldest = cart1

    if cart2.age > oldest.age:
        oldest = cart2

    if cart3.age > oldest.age:
        oldest = cart3

    return oldest

 # Print the oldest cat's details
def display_oldest_cat(oldest):
    print(f"The oldest cat is {oldest.name.title()} with an age of"
          f" {oldest.age} years old")

display_oldest_cat(oldest_cat(cat1, cat2, cat3))



"""
                🌟 Exercise 2 : Dogs
Create a Dog class with methods for barking and jumping.
Instantiate dog objects, call their methods, and compare their sizes.
"""
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = int(height)

     # Create a bark() method
    def bark(self):
        print(f"{self.name.title()} goes woof!")

    # Create a jump() method
    def jump(self):
        print(f"{self.name.title()} jumps up to {self.height * 2} cm high!")

 #Creating dog objects
davids_dog = Dog('Dora', 20)
sarahs_dog = Dog('spotty', 45)

 #Print Dog Details and Call Methods
print(f"The first dog is {sarahs_dog.name.title()} with an height of "
      f"{sarahs_dog.height} Cm."
      f"\nThe second dog is {davids_dog.name.title()} with an height of "
      f"{davids_dog.height} Cm.")

 #Call the bark() and jump() methods for each dog.
sarahs_dog.bark()
sarahs_dog.jump()

davids_dog.bark()
davids_dog.jump()

 #Compare Dog sizes in height
if sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name.title()} is taller than {davids_dog.name.title()}"
          f"by {sarahs_dog.height - davids_dog.height}Cm.")

elif davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name.title()} is taller than {sarahs_dog.name.title()}"
          f"by ({davids_dog.height - sarahs_dog.height}Cm.")

else:
    print("Both dogs are of the same height")



"""    
            🌟 Exercise 3 : Who’s the song producer?
Create a Song class with a method to print song lyrics line by line.          
"""
# Create the song class
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    #Create a printing method for each lyric
    def sing_the_song(self):
        for line in self.lyrics:
            print(line)

 #Create a song object and pass the lyrics
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
    ])

stairway.sing_the_song()


"""
            🌟 Exercise 4 : Afternoon at the Zoo
Create a Zoo class to manage animals. The class should allow adding animals, 
displaying them, selling them, and organizing them into alphabetical groups
"""
 # Step 1: Define the Zoo class
class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

 # Add one or more animals to the zoo
    def add_animal(self, *new_animal):
        for animal in new_animal:
            if animal not in self.animals:
                self.animals.append(animal)

                print(f"{animal} has been added to the zoo.")

            else:
                print(f"{animal} already exists in the zoo.")













































































































