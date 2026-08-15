""" BUILD UP STRING """
# 1. Ask for User Input: exactly 10 characters long
string = input("Enter a 10 characters long string: ")

# 2. Check the Length of the String with considering spaces
count = 0
for char in string:
    if char != " ":
        count += 1

 # Checking length after counting is done:
if count == 10:
    print("String perfect")

elif count > 10:
    print("String is too long")

else:
    print("String is too short")

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