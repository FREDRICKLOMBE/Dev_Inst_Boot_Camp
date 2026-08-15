""" 🌟 Exercise 1: Converting Lists into Dictionaries """

# Convert the given two lists into a dictionary where the first list
# contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)


"""  🌟 Exercise 2: Cinemax #2 """
# Calculate the total cost of movie tickets for a family based on their ages.

family = {
    "rick": 43,
    'beth': 13,
    'morty': 5,
    'summer': 8
}

total_cost = 0
 #Loop through the family dictionary to calculate the total cost
for name, age in family.items():
    if age < 3:
        total_cost += 0
        print(f"The price for {name.title()} is free")

    elif 3 <= age < 12:
        total_cost += 10
        print(f"The price for {name.title()} is $10")

    else:
        total_cost += 15
        print(f"The price for {name.title()} is $15")

print(f"The total cost is ${total_cost}")

""" BONUS """
family = {}

number_of_members = int(input("How many family members? "))

for i in range(number_of_members):
    name = input("Enter family member's name: ")
    age = int(input(f"Enter {name}'s age: "))

    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        print(f"The price for {name.title()} is free")

    elif 3 <= age < 12:
        total_cost += 10
        print(f"The price for {name.title()} is $10")

    else:
        total_cost += 15
        print(f"The price for {name.title()} is $15")

print(f"The total cost is ${total_cost}")


""" 🌟 Exercise 3: Zara """
    #Create a dictionary with the provided data
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "types_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Germany": "red",
        "US": ["pink", "green"]
    }
         }

    # Change the value of number_stores to 2
brand["number_stores"] = 2

    # Print a sentence describing Zara’s clients using the type_of_clothes key.
clients = brand["types_of_clothes"]

print("\nAt Zara we cover for all clients including:")
for client in clients:
    print(f"-- {client.title()}")

    # Add a new key country_creation with the value Spain.
brand["country_creation"] = "Spain"

    #Check if international_competitors exists and, if so, add “Desigual”
brand.get("international_competitors")

brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

    #Delete the creation_date key.
del brand["creation_date"]

    #Print the last item in international_competitors.
last_item = brand["international_competitors"][-1]
print(last_item)

    #Print the major colors in the US.
colors = brand["major_color"]["US"]
print(f'\nThe major colors in the U.S are:')

for color in colors:
    print(f"--{color.title()}")

    #Print the number of keys in the dictionary.
print(f"The number of keys is: {len(brand)}")

    #Print all keys of the dictionary.
for key in brand:
    print(key)

"""BONUS"""
    # Create another dictionary
more_on_zara = {
     "creation_date": 1975,
     "number_stores": 200,
 }

    # Merge the two dictionaries
merged_zara = brand | more_on_zara
print(merged_zara)


""" 🌟 Exercise 4: Disney Characters """
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

    # Create a dictionary that maps characters to their indices:
user_dict = {}
for (index, user) in enumerate(users):
    user_dict.update({user: index})
print(user_dict)

    # Create a dictionary that maps indices to characters:
new_dict = dict(map(reversed, user_dict.items()))
print(new_dict)

    # Create a dictionary where characters are sorted alphabetically
    # and mapped to their indices:
sorted_characters = {
    i: name
    for i, name in enumerate(sorted(new_dict.values()))
}
print(sorted_characters)
