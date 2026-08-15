""" 🌟 Exercise 1: Hello World """
 #Print the output using one line of code
print(4 * "HELLO WORLD\n")

""" 🌟 Exercise 2: Some Math"""
 #Write code that calculates the result of:
res = (99**3) * 8
print(res)

""" 🌟 Exercise 3: What is the output? """
 ## Predict the output of the following code snippets:
print(5 < 3)                # False
print(3 == 3)               # True
# print("3" > 3)              # Error
print("3" == 3)             # False
print("Hello" == "hello")   # False

"""  🌟 Exercise 4: Your computer brand """
# Create a computer_brand variable holding the brand name of your computer
computer_brand = "asus F15: tuf gaming"
print(f"I have an {computer_brand.title()} computer!")

""" 🌟 Exercise 5: Your information"""
my_name = "fredrick lombe"
age = 27
shoe_size = 41
info = (f"I am referred to as {my_name.title()} the big footed,"
        f" young Environmentalist because my shoe size is {shoe_size}"
        f" and I am {age} years old. Just Kidding!!!")
print(info)

""" 🌟 Exercise 6: A & B """
a, b = 5, 4

 # If a is bigger than b, have your code print "Hello World".
if a > b:
    print("Hello World")

""" 🌟 Exercise 7: Odd or Even """
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

""" 🌟 Exercise 8: What’s your name? """
# Write code that asks the user for their name and determines whether or not
# you have the same name. Print out a funny message based on the outcome.

user_name = input("Enter your name: ")

if user_name == my_name:
    print("I guess we have the same name")
else:
    print("No! Our names are different")

""" 🌟 Exercise 9: Tall enough to ride a roller coaster"""
height = int(input("Enter your height: "))
print(f"")

user_height = height
if user_height > 145:
    print("Your are eligible for a ride")
else:
    print("Sorry! Grow some more to ride ")