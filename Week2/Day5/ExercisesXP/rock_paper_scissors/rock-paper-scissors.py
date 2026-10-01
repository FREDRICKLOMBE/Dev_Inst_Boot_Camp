"""Run the Rock Paper Scissors menu and track scores for the current session."""

from game import Game


# === Menu ====================================================================

def get_user_menu_choice():
    """Display and validate the menu; return '1' (play), '2' (scores), or '3' (quit)."""
    while True:
        print("\n=== ROCK PAPER SCISSORS ===")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Choose 1, 2, or 3: ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid menu choice. Please enter 1, 2, or 3.")


# === Score presentation ======================================================

def print_results(results):
    """Print win/loss/draw totals and a thank-you message; return None.

    results must contain integer counts under 'win', 'loss', and 'draw'.
    This function only displays scores; it does not change them.
    """
    print("\n=== SCORES ===")
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print(f"Total rounds: {sum(results.values())}")
    print("Thank you for playing!")


# === Application startup =====================================================

def main():
    """Run the session until quit or interruption, show final scores, and return None."""
    # Initialize once so scores survive each trip through the menu.
    results = {"win": 0, "loss": 0, "draw": 0}

    try:
        while True:
            choice = get_user_menu_choice()
            if choice == "1":
                game = Game()
                result = game.play()
                # Count only completed rounds, using the result as the key.
                results[result] += 1
            elif choice == "2":
                print_results(results)
            else:
                break
    except (EOFError, KeyboardInterrupt):
        print("\nEnding the session.")

    print_results(results)
    print("Goodbye!")


# Importing the module should not start the interactive menu.
if __name__ == "__main__":
    main()
