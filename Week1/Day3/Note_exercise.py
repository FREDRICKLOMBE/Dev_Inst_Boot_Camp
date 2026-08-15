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