"""Handle player choices and the rules for one Rock Paper Scissors round."""

import random


class Game:
    """Play one round against the computer; session scores belong to the menu."""

    ITEMS = ("rock", "paper", "scissors")
    # Each key beats its corresponding value.
    BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    # === Choice handling =====================================================

    def get_user_item(self):
        """Prompt until valid; return 'rock', 'paper', or 'scissors' in lowercase."""
        while True:
            item = input("Choose rock, paper, or scissors: ").strip().lower()
            if item in self.ITEMS:
                return item
            print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_item(self):
        """Return a randomly selected 'rock', 'paper', or 'scissors'."""
        return random.choice(self.ITEMS)

    # === Round logic =========================================================

    def get_game_result(self, user_item, computer_item):
        """Return 'win', 'draw', or 'loss' from the user's perspective.

        Both arguments must be lowercase choices from ITEMS. Raise ValueError
        for unsupported choices so invalid data cannot silently count as a loss.
        """
        if user_item not in self.ITEMS or computer_item not in self.ITEMS:
            raise ValueError("Both choices must be rock, paper, or scissors.")
        if user_item == computer_item:
            return "draw"
        if self.BEATS[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self):
        """Play and display one round; return 'win', 'draw', or 'loss'."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        messages = {"win": "You win!", "draw": "It is a draw!", "loss": "You lose!"}
        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(messages[result])
        return result
