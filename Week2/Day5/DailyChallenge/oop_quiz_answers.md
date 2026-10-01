# Daily Challenge: OOP Quiz

## Exercise 1: Answers

1. **Class:** A blueprint that defines the attributes and methods of objects. `Card` defines what information a playing card stores.
2. **Instance:** An individual object created from a class. `Card("Hearts", "A")` creates an instance of `Card`.
3. **Encapsulation:** Grouping data with the methods that operate on it and controlling access to internal state. Python uses conventions such as `_cards` for internal attributes; this is not strict access enforcement.
4. **Abstraction:** Hiding implementation details behind a simple interface. A caller can use `deck.deal()` without knowing how cards are stored or removed.
5. **Inheritance:** Creating a class from a parent class so it can reuse, extend, or override its behavior. For example, `Dog(Animal)` can inherit an `eat()` method.
6. **Multiple inheritance:** Inheriting from more than one parent class, for example `class Duck(Swimmer, Flyer)`.
7. **Polymorphism:** Allowing different objects to respond to the same operation with their own behavior. For example, different classes can implement `speak()`. Python also supports this without a shared parent class through duck typing.
8. **Method Resolution Order (MRO):** The order Python uses to search a class and its ancestors for methods and attributes. Python uses C3 linearization, preserving inheritance ordering consistently. Inspect it with `ClassName.mro()` or `ClassName.__mro__`. `super()` follows this order.

## Exercise 2: Implementation

See `deck_of_cards.py`. `Deck` contains `Card` instances and does not inherit from `Card`.

- A new deck contains exactly 52 unique cards.
- `shuffle()` verifies all expected suit/value combinations before shuffling in place.
- Shuffling an incomplete deck raises `ValueError`. The prompt does not specify whether to restore missing cards; this solution rejects an incomplete deck to avoid returning dealt cards unexpectedly.
- `deal()` removes and returns a card. An empty deck raises `IndexError`.
- The optional menu supports dealing, shuffling, starting a new deck, and quitting.
- Each deal is one round. There are no game points; score presentation reports dealt and remaining cards for the current deck. Starting a new deck resets these counts.

## Run

With Python 3 installed, run:

```sh
python deck_of_cards.py
```

On Windows, you can also use `py deck_of_cards.py`.

Importing the module does not start the menu.
