""" 🌟 Exercise 1: Favorite Numbers """
# Create a set of favorite numbers
my_favorite_number = {2,4,6,8,78,67,45}

#Add two new numbers to the set.
my_favorite_number.update([5, 9])  #Add multiple at once
my_favorite_number.add(10)         #Add one at a time
print(my_favorite_number)

#Remove the last item you added
my_favorite_number.remove(10)
print(my_favorite_number)

#create another list
friend_favorite_number = {2,4,6,8,10,100,57}

#Concatenate the two sets
result = my_favorite_number | friend_favorite_number
print(result)


""" 🌟 Exercise 2: Tuple """
# Given a tuple of integers
my_tuple = (2,4,6,8,10,100,57)

#Try to add more integers to the tuple.
#print(my_tuple.append(4))   #Displays an error

my_tuple = my_tuple + (4,)   #Adding indirectly is supportable
print(my_tuple)


""" 🌟 Exercise 3: List Manipulation """

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

    #Remove "Banana" from the list
basket.remove("Banana")
print(basket)

    #Remove "Blueberries" from the list.
basket.remove("Blueberries")
print(basket)

    #Add "Kiwi" to the end of the list.
basket.append("Kiwi")
print(basket)

    #Add "Apples" to the beginning of the list
basket.insert(0, "Apples")
print(basket)

    #Count how many times "Apples" appear in the list.
item_count = basket.count("Apples")
print(item_count)

    #Empty the list.
basket.clear()

    #Print the final state of the list
print(basket)

""" 🌟 Exercise 4: Floats """

# An integer is a whole number with no decimal part.
# A float represents a number that can have a decimal part.

    #reate a list having a sequence of mixed types: floats and integers:
mixed_numbers = []

for number in range(2, 6):
    mixed_numbers.append(number - 0.5)

    mixed_numbers.append(number)

print(mixed_numbers)


"""  🌟 Exercise 5: For Loop """

    #Write a for loop to print all numbers from 1 to 20, inclusive.
for numb in range(1, 21):
    print(numb)

    #Write another for loop every number from 1 to 20 where the index is even.
numbers = list(range(1, 21))

for index, number in enumerate(numbers):
    if index % 2 == 0:
        print(number)

    #Alternatively
index = 0

for number in numbers:
    if index % 2 == 0:
        print(number)

    index += 1


""" 🌟 Exercise 6: While Loop """

user_name = input("What is your name? ")

    #  check if name is proper (no digits and at least 3 letters long)
while True:
    if not user_name.isdigit() and len(user_name) >= 3:
        print("Thank you")
        break
    else:
        print("Give the correct name")
        user_name = input("What is your name? ")


""" 🌟 Exercise 7: Favorite Fruits """
favourite_fruits = input("Enter your favourite fruits, separated by spaces: ")

favourite_fruits = favourite_fruits.split()

fruit = input("Enter the name of any fruit: ")

if fruit in favourite_fruits:
    print("You chose one of your favourite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


""" 🌟 Exercise 8: Pizza Toppings """
toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + (len(toppings) * topping_price)

print("\nYour pizza toppings:")
for topping in toppings:
    print(topping)

print(f"Total cost: ${total_cost:.2f}")


""" 🌟 Exercise 9: Cinemax Tickets """
total_cost = 0

while True:
    age = input("Enter the age of a family member (or 'done' to finish): ")

    if age.lower() == "done":
        break

    age = int(age)

    if age < 3:
        total_cost += 0
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"Total ticket cost: ${total_cost}")


## BONUS

ages = []

while True:
    age = input("Enter your age (or 'done' to finish): ")

    if age.lower() == "done":
        break

    ages.append(int(age))

for age in ages[:]:
    if age < 16 or age > 21:
        ages.remove(age)

print("Final list of attendees:")
print(ages)