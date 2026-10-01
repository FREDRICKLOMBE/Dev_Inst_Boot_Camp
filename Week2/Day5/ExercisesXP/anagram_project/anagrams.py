"""Command-line interface for the anagram checker. Run: python anagrams.py."""

from anagram_checker import AnagramChecker


# === Input validation ========================================================

def validate_word(user_input):
    """Return a cleaned lowercase word, or raise ValueError with a helpful error."""
    word = user_input.strip()

    if not word:
        raise ValueError("Please enter a word; the input cannot be empty.")
    if len(word.split()) != 1:
        raise ValueError("Please enter only one word.")
    if not word.isalpha():
        raise ValueError("Use alphabetic characters only; no numbers or symbols.")

    return word.lower()


# === Result presentation =====================================================

def display_results(checker, word):
    """Print dictionary validity and any anagrams for a well-formed word."""
    print(f'\nYOUR WORD: "{word.upper()}"')

    if checker.is_valid_word(word):
        print("This is a valid English word in the supplied dictionary.")
    else:
        print("This word was not found in the supplied dictionary.")

    # Dictionary membership and valid input are separate checks. A letter
    # sequence absent from the dictionary may still have dictionary anagrams.
    anagrams = checker.get_anagrams(word)
    if anagrams:
        print(f"Anagrams for your word: {', '.join(anagrams)}.")
    else:
        print("No anagrams found in the supplied dictionary.")


# === Menu and application startup ============================================

def main():
    """Load the dictionary once and keep the menu open until the user exits."""
    try:
        checker = AnagramChecker()
    except (OSError, UnicodeError) as error:
        print(f"Could not load the word list: {error}")
        print("Place a readable UTF-8 sowpods.txt beside anagram_checker.py.")
        return

    try:
        while True:
            print("\n=== ANAGRAM CHECKER ===")
            print("1. Enter a word")
            print("2. Exit")
            choice = input("Choose 1 or 2: ").strip()

            if choice == "2":
                print("Goodbye!")
                break
            if choice != "1":
                print("Invalid menu choice. Please choose 1 or 2.")
                continue

            try:
                word = validate_word(input("Enter a word: "))
            except ValueError as error:
                print(f"Invalid input: {error}")
                continue

            display_results(checker, word)
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


# Importing this module should not start an interactive session.
if __name__ == "__main__":
    main()
