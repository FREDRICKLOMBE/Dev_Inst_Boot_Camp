import random
from pathlib import Path

## 🌟 Exercise 1: Random Sentence Generator
# Read a word list and generate a lowercase sentence of the requested length.

# Keep the word list beside this script, even when running from another folder.
WORDS_FILE = Path(__file__).resolve().parent / "words.txt"


def get_words_from_file(file_path):
    """Read a text file at file_path and return its words as a list of strings."""
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
    return words


def get_random_sentence(length):
    """Return a lowercase sentence containing an integer length of 2 to 20 words."""
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("The sentence length must be an integer.")
    if not 2 <= length <= 20:
        raise ValueError("The sentence length must be between 2 and 20.")

    words = get_words_from_file(WORDS_FILE)
    if not words:
        raise ValueError("The word list is empty.")

    # Choose each word separately, so the same word can appear more than once.
    selected_words = []
    for _ in range(length):
        selected_words.append(random.choice(words))

    return " ".join(selected_words).lower()


def main():
    """Ask for a sentence length, validate it and display random words; return None."""
    print("This program generates a random sentence using a word list.")

    # Stop after invalid input instead of asking for another value.
    try:
        length = int(input("Enter a sentence length between 2 and 20: "))
    except ValueError:
        print("Error: The sentence length must be an integer.")
        return

    if not 2 <= length <= 20:
        print("Error: The sentence length must be between 2 and 20.")
        return

    try:
        sentence = get_random_sentence(length)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}")
        return

    print(sentence)


if __name__ == "__main__":
    """ Generate a random sentence from user input """
    main()
