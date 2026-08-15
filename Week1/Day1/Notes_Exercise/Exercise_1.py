"""
Exercise 1: Boolean Logic
Instructions: Complete the exercises below by writing an expression in Python
 to answer the question:
"""

# Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

# Write a comment that says "This is a comment."
 # "This is a comment."

# Log a message to the terminal that says "I AM A COMPUTER!"
print('I AM A COMPUTER!')

# Write an if statement that checks if 1 is less than 2 and if 4 is
# greater than 2. If it is, show the message "Math is fun."
if (1 < 2) and (4 > 2):
    print('Math is fun!')

# Assign a variable called nope to an absence of value.
nope = None

# Use the language’s “and” boolean operator to combine the language’s
# “true” value with its “false” value.
print(True and False)

# Calculate the length of the string "What's my length?"
# with the special characters
length = "What's my length?"
print(f'The length of the string is: {len(length)}')

# without the special characters
count = 0

for char in length:
    if char != "'" and char != "?":
        count += 1
print(f'The total is now {count}')

# Convert the string "i am shouting" to uppercase.
string = 'i am shouting'
print(f'The uppercased version is: {string.upper()}')

# Convert the string "1000"to the number 1000.
numb = "1000"
print(int(numb))

#Combine the number 4 with the string "real" to produce "4real".
cha = "real"
print(f"The Concatenation is {str(4) + cha}")

# Record the output of the expression 3 * "cool".
print(3 * 'cool')

#Record the output of the expression 1 / 0.
#print(1 / 0)

# Determine the type of [].
print(type([]))

# Ask the user for their name, and store it in a variable called name.
age = input("What is your name?")

#Ask the user for a number. If the number is negative, show a message that says
# "That number is less than 0!" If the number is positive, show a message that
# says "That number is greater than 0!" Otherwise, show a message that
# says "You picked 0!.
num = int(input("Enter a number"))

if num < 0:
    print('The number is less than 0')
elif num > 0:
    print('The number is greater than 0')
else:
    print('You picked 0!')

# Find the index of "l" in "apple".
fruit = "apple"

 #Find the index of "l"
index_l = fruit.index("l")
print(f'index of l is {index_l}')

 #Alternatively using the find() function
index_l = fruit.find("l")
print(f'index of l is {index_l}') # Output a -1 when the character is absent

# Check whether "y" is in "xylophone".
xy = "xylophone"
print("y" in xy)

xy.find("y")

#Check whether a string called my_string is all in lowercase.
my_string = "Fredrick Lombe"

print(my_string.islower())