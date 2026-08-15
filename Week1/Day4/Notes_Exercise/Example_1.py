#MAP FUNCTION
def upper_string(s):
    return s.upper()

fruits = ['apple', 'banana', 'orange', 'mango']
map_object = map(upper_string, fruits)
print(list(map_object))

#FILTER FUNCTION
def starts_with_A(s):
    return s[0] == "A"

fruit = ['Ark', 'Apple', 'banana', 'orange', 'mango']
filtered_list = list(filter(starts_with_A, fruit))
print(list(filtered_list))

#REDUCE() FUNCTION
from functools import reduce

def sum_numbers(num1, num2):
    return num1 + num2

my_list = [1, 2, 3, 4, 5]
print(reduce(sum_numbers, my_list))