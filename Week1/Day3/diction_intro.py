# create a personal info dictionary
 #first, last, age, program, courses

personal_info = {
    'first_name': 'fredrick',
    'last_name': 'lombe',
    'age': 27,
    'program': 'data analytics',
    'courses': ['full stack dev', 'web dev', 'data science']
}

print(f'my personal info is: \n{personal_info}')
print(f'\nmy first name is: {personal_info["first_name"].title()}')

#Unpacking the dictionary
print(f'\ncomponents: \n{personal_info.items()}')

#Change the value in dictionary
personal_info["last_name"] = 'mutila'

#Adding a key - value pair
personal_info["height"] = 167

#Removing an unwanted key - value pair
del personal_info["height"]
print('height' in personal_info)

#Output the keys or values
for k,v in personal_info.items():
    if k != 'age':
        print(f'\nThe key is {k.title()} and the value is {v}')

#List comprehension
squares = [num**2 for num in range(1, 11) if num % 2 == 0]
print(squares)

# Using the .get() method
print(personal_info.get('age'))

print(personal_info.get('middle', None))  #If a value does not exist:

#Using the set default() function to add info to the dictionary
print(personal_info.setdefault('middle', 'mutila'))

