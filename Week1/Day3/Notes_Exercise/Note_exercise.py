"""
ACCESSING KEY - VALUE OF A NESTED DICTIONARY
"""
# Access the value of key history

sample = {
   "class": {
      "student": {
         "name": "Mike",
         "marks": {
            "physics": 70,
            "history": 80
         }
      }
   }
}

print(sample["class"]["student"]["marks"]["history"])
print(sample["class"]["student"]["marks"]["physics"])


"""
keys()
The my_dict.keys() method returns a dict_keys of all the keys in my_dict

values()
The my_dict.values() method returns a dict_values of all the values in my_dict

items()
my_dict.items()returns tuples containing the key-value pairs in a dictionary.
"""

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

# Remove multiple keys
keys_to_remove = ['age', 'salary']

for key in keys_to_remove:
        sample_dict.pop(key, None) #None prevents an error if a key is missing.

print(sample_dict)

# For Loops and Dictionaries
my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for key, value in my_books.items():
    print(f"The {key} is {value}\n")

#Enumerate each item in the iterable.
for (index, items) in enumerate ("abcdefg"):
    print(f"At position {index + 1} the letter is {items.upper()}")

#Zip and Concatenate Iterables into a tuple:
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3):
    print(f"{item}\n")