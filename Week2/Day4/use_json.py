class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def desribe_restaurant(self):
        print(f"{self.name.title()} is always known for offering unique "
              f"{self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"{self.name.title()} is available at your service")


rest1 = Restaurant("meatbar", "burgers")
rest1.desribe_restaurant()
rest1.open_restaurant()

class Users:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        print(f"\nMy name is {self.first_name.title()} {self.last_name.title()}."
              f"\nI am a {self.age} years old {self.occupation.title()}.")

    def greet_user(self):
        print(f"\nHello, {self.first_name.title()}.")

user = Users("John", "Doe", "19", 'engineer')
user.describe_user()
user.greet_user()
