""" 🌟 Exercise 1: What Are You Learning? """

# Define a Function
def display_message():
    return "I am learning about functions in Python"


 # Call the Function
print(display_message())


""" 🌟 Exercise 2: What’s Your Favorite Book? """
 # Define a Function
def favorite_book(title):
    return f'One of my favorite books is {title.title()}'


 # Call the Function
print(favorite_book("alice in wonderland"))


""" 🌟 Exercise 3: Some Geography """
 # Define a Function with multiple Parameters
def describe_city(city, country = "Unknown"):
    return f'{city.title()} is in {country.title()}'


 #Call the function
print(describe_city("reykjavik", "iceland"))
print(f'{describe_city("paris")}')



""" 🌟 Exercise 4: Random """

import random

 # Define a function
def import_random():
    user_number = int(input("Please enter a number: "))
    number = random.randint(1, 101)

    if user_number == number:
        print("Success! You got it!")
    else:
        print(f"Not the same!"
              f"\nYour guess: {user_number}, Random number: {number}")

 # Call the function
import_random()


""" 🌟 Exercise 5: Let’s Create Some Personalized Shirts! """
# Define a function called make_shirt().
# This function should accept two parameters: size and text.

word = "I Love Python"

def make_shirt(size, text = word):
    """Shirt size and Texts to be printed"""
    print(f'\nThe size of the shirt is {size} and'
          f' the text is {text}.')


make_shirt("large", word)
make_shirt("medium", word)
make_shirt("small", "I'm the terminator")

# (Bonus): Keyword Arguments
make_shirt(size = "small", text = "Hello!")

""" 🌟 Exercise 6: Magicians… """
# Create a List of Magician Names
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

#Create a Function to Display Magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

#Create a Function to Modify the List
def make_great(magicians):
    for magician in magicians:
        print(f'{magician} the Great')

make_great(magician_names)
show_magicians(magician_names)


" 🌟 Exercise 7: Temperature Advice """
# Create the get_random_temp() Function
import random

def get_random_temp():
    return random.randint(-10, 40)


def main():
    random_temp = get_random_temp()
    print(f"The temperature right now is {random_temp} degrees Celsius")

    #Provide Temperature-Based Advice
    if random_temp < 0:
        print("Brr that's freezing! Wear some extra layers today.")

    elif random_temp <= 16:
        print("Quite chilly! Don't forget your coat")

    elif random_temp <= 23:
        print("Nice weather.")

    elif random_temp <= 32:
        print("A bit warm, stay hydrated.")

    else:
        print("It's really hot! Stay cool")

main()

# Floating-Point Temperatures (Bonus)
def mod_get_random_temp():
    return round(random.uniform(-10, 40), 2)

# Month-Based Seasons (Bonus)
def get_month_temp(month):

    if month in [12, 1, 2]:
        season = "Winter"
        temperature = random.uniform(-10, 10)

    elif month in [3, 4, 5]:
        season = "Spring"
        temperature = random.uniform(10, 25)

    elif month in [6, 7, 8]:
        season = "Summer"
        temperature = random.uniform(20, 40)

    elif month in [9, 10, 11]:
        season = "Autumn"
        temperature = random.uniform(10, 30)

    else:
        return None, None

    return f"{season} season with temperature of {round(temperature, 2)} degrees Celsius"

month = int(input("Enter a month (1-12): "))
print(get_month_temp(month))




