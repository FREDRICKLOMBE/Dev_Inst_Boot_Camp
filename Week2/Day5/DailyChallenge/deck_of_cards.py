"""OOP daily challenge: a complete deck with an optional console menu."""

import random


class Card:
    """A playing card with a suit and a value."""

    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit: str, value: str) -> None:
        """Initialize a valid card; return None. Raise ValueError for invalid data."""
        if suit not in self.SUITS or value not in self.VALUES:
            raise ValueError("Invalid card suit or value.")
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        """Return a readable card name, such as 'A of Hearts'."""
        return f"{self.value} of {self.suit}"


class Deck:
    """A collection of cards: composition, rather than inheritance."""

    def __init__(self) -> None:
        """Create all 52 distinct cards; return None."""
        self._cards = [Card(suit, value) for suit in Card.SUITS for value in Card.VALUES]

    def __len__(self) -> int:
        """Return the number of cards remaining in the deck."""
        return len(self._cards)

    def shuffle(self) -> None:
        """Shuffle a complete deck; return None. Raise ValueError if incomplete."""
        expected = {(suit, value) for suit in Card.SUITS for value in Card.VALUES}
        actual = {(card.suit, card.value) for card in self._cards}
        if len(self._cards) != 52 or actual != expected:
            raise ValueError("Shuffling requires all 52 unique cards. Start a new deck first.")
        random.shuffle(self._cards)

    def deal(self) -> Card:
        """Remove and return one Card; raise IndexError if the deck is empty."""
        if not self._cards:
            raise IndexError("The deck is empty. Start a new deck to continue.")
        return self._cards.pop()


# ==================== Choice handling ====================

def get_choice() -> str:
    """Return a validated menu choice ('1', '2', '3', or '4')."""
    while True:
        choice = input("Choose an option: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print("Please enter 1, 2, 3, or 4.")


# ==================== Round logic ====================

def play_round(deck: Deck) -> None:
    """Deal and display one card, or explain that the deck is empty; return None."""
    try:
        card = deck.deal()
    except IndexError as error:
        print(error)
    else:
        print(f"You drew: {card}")


# ==================== Menu ====================

def show_menu() -> None:
    """Print the available actions; return None."""
    print("\n1. Deal a card")
    print("2. Shuffle the complete deck")
    print("3. Start a new shuffled deck")
    print("4. Quit")


# ==================== Score presentation ====================

def show_score(deck: Deck) -> None:
    """Print dealt and remaining card counts for this deck; return None."""
    print(f"Cards dealt: {52 - len(deck)} | Cards remaining: {len(deck)}")


# ==================== Application startup ====================

def main() -> None:
    """Run the menu until quit or input interruption; return None."""
    deck = Deck()
    deck.shuffle()
    print("Deck of Cards")
    show_score(deck)
    try:
        while True:
            show_menu()
            choice = get_choice()
            if choice == "4":
                break
            if choice == "1":
                play_round(deck)
            elif choice == "2":
                try:
                    deck.shuffle()
                    print("Deck shuffled.")
                except ValueError as error:
                    print(error)
            elif choice == "3":
                deck = Deck()
                deck.shuffle()
                print("New deck created and shuffled.")
            show_score(deck)
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended.")
    print("Final counts:")
    show_score(deck)
    print("Goodbye!")


if __name__ == "__main__":
    main()
