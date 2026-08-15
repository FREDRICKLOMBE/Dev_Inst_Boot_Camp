def greet(name, greeting):
  """ A function that takes a string name and a greeting """
  return f"Hello, {name}!"

print(greet("student", "Hello"))
print(greet(greeting = "Good morning", name = "Rome"))

# Pass multiple argument using a list
def greetings(my_list):
  return f"Hello, {my_list[0], my_list[1]}!"

print(greetings(["Hello", "America"]))







# Using the Reducing
from functools import reduce

my_list = [100, 20, 5, 1000]
def sum_numbers(first, second):
    return first + second
my_magic_sum = (reduce(sum_numbers, my_list))
print(my_magic_sum)
