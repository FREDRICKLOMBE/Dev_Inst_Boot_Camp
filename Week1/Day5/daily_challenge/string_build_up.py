""" BUILD UP STRING """
# 1. Ask for User Input: exactly 10 characters long
string = input("Enter a 10 characters long string: ")

# 2. Check the Length of the String without considering spaces
count = 0
for char in string:
    if char != " ":
        count += 1

 # Checking length after counting is done:
if count > 10:
    print("String is too long")

elif count < 10:
    print("String is too short")

else:
    print("String perfect")

    #Once the string is validated, print the first and last characters.
    first_char = string[0]
    last_char = string[-1]

    print(f"\nFirst char: {first_char}"
          f"\nLast char: {last_char}")

#3. Build the String Character by Characters
word = ""
for char in string:
    if char != " ":
         word += char
    print(word)

#4 Shuffling the words
import random

sentence = "the quick brown fox jumps"
words = sentence.split()      # turns the string into a list of words

random.shuffle(words)         # shuffles the list in place

shuffled_sentence = " ".join(words)   # joins the list back into a string
print(shuffled_sentence)