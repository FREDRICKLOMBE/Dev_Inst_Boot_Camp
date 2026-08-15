"""
Mapping in a function
"""
my_list = ["a", "b", "hello", "Z",]

def my_map_function(item):
    if isinstance(item, str):
        if item.islower():
            return item.upper()
        if item.isupper():
            return item.lower()
    return item


map_object = map(my_map_function, my_list)

print(list(map_object))