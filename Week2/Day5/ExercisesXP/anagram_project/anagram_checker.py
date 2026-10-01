"""Dictionary loading and anagram logic, independent of the user interface."""

from pathlib import Path


# === Dictionary and anagram logic =============================================

class AnagramChecker:
    """Find anagrams using a dictionary containing one word per line.

    Methods return values without printing or requesting keyboard input.
    """

    def __init__(self, word_list_path=None):
        """Load lowercase words once, removing duplicates and blank lines.

        By default, use sowpods.txt beside this module, regardless of the
        terminal's working directory. A custom path can be supplied for tests.
        File-reading errors are allowed to reach the calling interface.
        """
        if word_list_path is None:
            word_list_path = Path(__file__).resolve().with_name("sowpods.txt")

        with open(word_list_path, encoding="utf-8-sig") as word_file:
            self.words = {
                line.strip().lower() for line in word_file if line.strip()
            }

    def is_valid_word(self, word):
        """Return whether the word is present in the dictionary, ignoring case."""
        return word.strip().lower() in self.words

    def is_anagram(self, word1, word2):
        """Return whether both words have identical letters and letter counts.

        Identical words also match here; get_anagrams excludes the original.
        """
        # Sorting preserves repeated letters; converting to a set would not.
        return sorted(word1.strip().lower()) == sorted(word2.strip().lower())

    def get_anagrams(self, word):
        """Return other dictionary words with matching letters, alphabetically."""
        word = word.strip().lower()
        anagrams = []

        for candidate in self.words:
            if candidate != word and len(candidate) == len(word):
                if self.is_anagram(word, candidate):
                    anagrams.append(candidate)

        # A set has no display order, so sort for predictable, readable output.
        return sorted(anagrams)
