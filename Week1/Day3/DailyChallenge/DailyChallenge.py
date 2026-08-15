""" Challenge 1: Letter Index Dictionary """
# Create a dictionary that stores the indices of each letter in a word provided

    # User input
word = input("Enter a word: ")

    # Creating the Dictionary:
dictionary = {}
for index, letter in enumerate(word):
    if letter not in dictionary:
        dictionary[letter] = [index]

    else:
        dictionary[letter].append(index)

print(dictionary)


""" Challenge 2: Affordable Items"""
# Prints a list of items that can be purchased with a given amount of money.
items_purchase = {
    "Water": "$10",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

basket = []

# Data Cleaning
wallet = "$10"
wallet_int = int(wallet.replace("$", ""))

#Determine affordable items
for item, price in items_purchase.items():
    price_int = int(price.replace("$", "").replace(",", ""))

    if price_int <= wallet_int:
        wallet_int -= price_int
        basket.append(item)

# Check if basket is empty
if not basket:
    print("Nothing")

else:
    basket.sort()
    print(basket)


