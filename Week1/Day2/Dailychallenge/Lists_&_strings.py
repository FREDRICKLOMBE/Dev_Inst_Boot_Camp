"""
Challenge 1: Multiples of a Number

Instructions:
1. Ask the user for two inputs:
A number (integer).
A length (integer).

2. Create a program that generates a list of multiples of the given number.
3. The list should stop when it reaches the length specified by the user.
"""

#1 User input List
length = int(input("Whats your desired list length?"))

number = int(input("Whats your desired number?"))

user_list = []
 #Ask user for the many numbers
for i in range(1, length + 1):
    numb = number * i

    #Append the number to the list
    user_list.append(numb)
print(user_list)


"""
Challenge 2: Remove Consecutive Duplicate Letters


he new string should only contain unique consecutive letters.
"""

# 1. Ask the user for a string.
word = input("Enter your desired word: ")

new_word = ""

#2. Processes the string to remove consecutive duplicate letters.
for letter in word:
    if letter not in new_word:
        new_word += letter

print(new_word)