import random
import string
from datetime import datetime

from faker import Faker

# Install Faker before running: py -m pip install Faker

## 🌟 Exercise 1: Currencies
# Create a Currency class with methods for displaying and adding amounts.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return str(self)

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> "
                    f"and <{other.currency}>"
                )
            return self.amount + other.amount

        if isinstance(other, int):
            return self.amount + other

        return NotImplemented

    def __iadd__(self, other):
        new_amount = self.__add__(other)
        if new_amount is NotImplemented:
            return NotImplemented
        self.amount = new_amount
        return self


""" Create Currency Instances """
c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

""" Test Currency Methods """
print(c1)          # 5 dollars
print(int(c1))     # 5
print(repr(c1))    # 5 dollars
print(c1 + 5)      # 10
print(c1 + c2)     # 15
print(c1)          # 5 dollars

c1 += 5
print(c1)          # 10 dollars

c1 += c2
print(c1)          # 20 dollars

# Catch the expected error so the other exercises can run.
try:
    print(c1 + c3)
except TypeError as error:
    print(f"TypeError: {error}")


""" 🌟 Exercise 2: Import """
# The function is defined in func.py and imported in exercise_one.py.
# Keep all three files in the same folder.
from exercise_one import run_import_example

run_import_example()


""" 🌟 Exercise 3: String module """
letters = string.ascii_letters
random_string = ""

for number in range(5):
    random_string += random.choice(letters)

print(random_string)


""" 🌟 Exercise 4: Current Date """
def current_date():
    today = datetime.now().date()
    print(f"Today's date is {today}")


current_date()


""" 🌟 Exercise 5: Amount of time left until January 1st """
def time_until_january():
    now = datetime.now()
    january_first = datetime(now.year + 1, 1, 1)
    time_left = january_first - now
    print(f"January 1st is in {time_left}")


time_until_january()


""" 🌟 Exercise 6: Birthday and minutes """
def minutes_lived(birthdate):
    # Enter the birthdate as YYYY-MM-DD. The birth time is assumed to be midnight.
    birthday = datetime.strptime(birthdate, "%Y-%m-%d")
    now = datetime.now()

    if birthday > now:
        print("Your birthdate cannot be in the future.")
        return

    time_lived = now - birthday
    minutes = int(time_lived.total_seconds() / 60)
    print(f"You have lived for {minutes:,} minutes.")


minutes_lived("2000-01-01")


""" 🌟 Exercise 7: Faker Module """
faker = Faker()
users = []


def add_users(number_of_users):
    for number in range(number_of_users):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code(),
        }
        users.append(user)


""" Create users and display the list """
add_users(3)
print(users)
