"""1. Returning a simple value """

def get_name(first_name, last_name):
    """ Return a full neatly formatted name """
    full_name = first_name + " " + last_name
    return full_name.title()

profile = get_name("fredrick", "martin")
print(profile)


""" 2. Calculation() function to add & subtract two variables """

def calculator(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction

 # Function call
result = calculator(40, 10)
print(result)

"""3. Passing list as function arguments """
def greet_user(users):          ## users should be a list
    for user in users:                   # Because it's a list, loop through it.
        print(f'Hello {user.title()}!')

usernames = ['mutila', 'hazel', 'martin', 'lombe']
greet_user(usernames)


"""4. Modifying a list in a function """

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simulate creating a 3D print from the design.
        print(f"\nPrinting model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):

    ##Show all the models that were printed.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""
5.Using the *args when the number of arguments needed to pass in a 
function is not predefined
"""

#Using (*args) to find the sum
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


print(add_numbers(5, 10, 15, 20))

""" 
6. Using key word arguments (**kwargs) in a function 
**kwargs: is a dictionary of args (keywords).

"""

def sum_numbers(**kwargs):
    total = 0

    for value in kwargs.values():
        total += value

    return total

# Example usage
result = sum_numbers(a=10, b=20, c=30, d=40)
print(result)

"""
7. when using both (**kwargs) and (*args), in a function 
Note: You have to preserve the order ! 

"""
def check_arguments(*args,**kwargs):
    print('*args', args)
    print('**kwargs', kwargs)

f = check_arguments(10,20,30,name='John',surname='Doe')
print(f)

