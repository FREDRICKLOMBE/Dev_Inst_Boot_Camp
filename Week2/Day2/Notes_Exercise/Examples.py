class Shape:
    """ Class attributes (like this) are shared by every instance of the class
     — they're set once, when the class is defined, not per-object."""
    sides = 4               #first property
    name = "Square"         #Second property

    """ method defined """
    def description(self):
        return "A shape with 4 sides"

s1 = Shape()
print(f"Name of shape is {s1.name}")
print(f"Number of sides is {s1.sides}")
print(s1.description())

"""
Exercise on Inheritance and Composition: Door class
"""
class Door:
    def __init__(self, is_opened):
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

"""
Override the parent class's functions of open_door() and close_door()
To raise an Error that a blocked door cannot be opened or closed
"""
class BlockedDoor(Door):
    def open_door(self):
        raise Exception("A blocked door cannot be opened.")

    def close_door(self):
        raise Exception("A blocked door cannot be closed.")

door_1 = BlockedDoor(True)
door_1.open_door()

