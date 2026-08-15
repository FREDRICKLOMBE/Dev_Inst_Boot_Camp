class Farm():
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    #Add animals to the farm
    def add_animal(self, animal_type, count = 1):
        if animal_type in self.animals:
            self.animals[animal_type] += count

        else:
            self.animals[animal_type] = count

    #Display farm information
    def get_info(self):
        info = f"{self.name}'s farm\n"

        for animal, count in self.animals.items():
            info += f"{animal:<10}: {count}\n"

        info += "\n   E-I-E-I-O!"
        return info

    # Return animal types alphabetically
    def get_animal_types(self):
        return sorted(self.animals.keys())

    #Display a short descriptio
    def get_short_info(self):
        animals = self.get_animal_types()

        animal_list = []

        for animal in animals:
            if self.animals[animal] > 1:
                animal += "s"
            animal_list.append(animal)

        return f"{self.name}'s farm has {', '.join(animal_list[:-1])} and {animal_list[-1]}."

#Create the farm
macdonald = Farm("Macdonald")

#Add animals
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("pig")
macdonald.add_animal("goat", 12)

# Display information
print(macdonald.get_info())

# Bonus
print(macdonald.get_short_info())
