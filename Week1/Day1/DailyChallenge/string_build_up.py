""" BUILD UP STRING """
# 1. Ask for User Input: exactly 10 characters long
string = input("Enter a 10 characters long string: ")

# 2. Check the Length of the String with spaces
if len(string) < 10:
    print("String not long enough")
elif len(string) > 10:
    print("String too long")
else:
    print("Perfect string")

#3. Print the First and Last Characters after validation:
    print(f"First letter: {string[0]}"
          f"\nLast letter: {string[-1]}")

# 4. Build the String Character by Characters
    word = ""
    for char in string:
        word += char
        print(word)

 # 5 Shuffling the words
    import random

    words = string.split()  # turns the string into a list of words

    random.shuffle(words)  # shuffles the list in place

    shuffled_sentence = " ".join(words)  # joins the list back into a string
    print(shuffled_sentence)





