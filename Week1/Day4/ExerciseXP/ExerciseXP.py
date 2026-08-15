""" 🌟 Exercise 1: What Are You Learning? """

# Define a Function
def display_message():
    output = "I am learning about functions in Python"
    return output

 # Call the Function
print(display_message())


""" 🌟 Exercise 2: What’s Your Favorite Book? """
 # Define a Function
def favorite_book(title):
    book = f'\nOne of my favorite books is {title.title()}'
    return book

 # Call the Function
print(favorite_book("alice in wonderland"))


""" 🌟 Exercise 3: Some Geography """
 # Define a Function with multiple Parameters
def describe_city(city, country = "Unknown"):
    geography = f'\n{city.title()} is in {country.title()}'
    return geography

 #Call the function
print(describe_city("reykjavik", "iceland"))
print(f'{describe_city("paris")}')



""" 🌟 Exercise 4: Random """

import random

 # Define a function
def import_random():
    user_number = int(input("\nPlease enter a number: "))
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
    print(f'\nMy shirt size is {size.title()} and'
          f'the text display is {text.title()}.')

prompt = '\nChoose your size:'
prompt += '\nSmall (S) | Medium (M) | Large (L) | '
size = input(prompt)
text = input("Write your text: ")

make_shirt(size, text = "Hello")



