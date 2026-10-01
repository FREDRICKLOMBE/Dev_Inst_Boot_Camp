import re
import string
from pathlib import Path

## 🌟 Daily Challenge: Text Analysis
# Analyze text from a string or file, then remove unwanted words and characters.

# Selected common words from the English stopwords-iso list.
# Source: https://github.com/stopwords-iso/stopwords-en
STOP_WORDS = set("""
a about above after again against all am an and any are as at
be because been before being below between both but by
can could did do does doing down during each few for from further
had has have having he her here hers herself him himself his how
i if in into is it its itself me more most my myself no nor not
of off on once only or other our ours ourselves out over own same
she should so some such than that the their theirs them themselves
then there these they this those through to too under until up very
was we were what when where which while who whom why will with
would you your yours yourself yourselves
""".split())


class Text:
    """Represent a string and analyze its whitespace-separated words."""

    def __init__(self, text):
        """Store a string in the text attribute; return None."""
        if not isinstance(text, str):
            raise TypeError("The text must be a string.")
        self.text = text

    def word_frequency(self, word):
        """Return the exact word's count, or None when it is not found."""
        words = self.text.split()
        frequency = words.count(word)
        return frequency if frequency else None

    def most_common_word(self):
        """Return the most frequent word, the first in a tie, or None for no words."""
        words = self.text.split()
        if not words:
            return None

        # Count each word with a dictionary, keeping its first appearance order.
        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1

        return max(frequencies, key=frequencies.get)

    def unique_words(self):
        """Return all distinct words as a sorted list, including repeated words once."""
        words = self.text.split()
        # Sort the set so the printed result stays consistent between runs.
        return sorted(set(words))

    @classmethod
    def from_file(cls, file_path):
        """Read a UTF-8 file and return an instance of the calling class."""
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return cls(text)


""" 🌟 Bonus: Text Modification """
class TextModification(Text):
    """Return cleaned versions of text without changing the original attribute."""

    def remove_punctuation(self):
        """Return text with the ASCII punctuation in string.punctuation removed."""
        return self.text.translate(str.maketrans("", "", string.punctuation))

    def remove_stop_words(self):
        """Return text without selected English stop words, ignoring their case."""
        words = self.text.split()
        remaining_words = []
        for word in words:
            # Ignore surrounding punctuation when checking a word against the set.
            if word.strip(string.punctuation).lower() not in STOP_WORDS:
                remaining_words.append(word)
        return " ".join(remaining_words)

    def remove_special_characters(self):
        """Return text containing only Unicode letters, digits and whitespace."""
        # The regex removes punctuation, symbols and underscores but keeps spaces.
        return re.sub(r"[^\w\s]|_", "", self.text)


if __name__ == "__main__":
    """ Part I: Analyze a simple string """
    simple_text = Text("A good book would sometimes cost as much as a good house.")
    print("Part I: Analyzing a Simple String")
    print(f"Original text: {simple_text.text}")
    print(f"Frequency of 'good': {simple_text.word_frequency('good')}")  # 2
    print(f"Frequency of 'python': {simple_text.word_frequency('python')}")  # None
    print(f"Most common word: {simple_text.most_common_word()}")  # good
    print(f"Unique words: {simple_text.unique_words()}")

    """ Part II: Analyze text from a file """
    # Resolve the sample file beside the script, regardless of the working folder.
    file_path = Path(__file__).resolve().parent / "sample_text.txt"
    file_text = Text.from_file(file_path)
    print("\nPart II: Analyzing Text from a File")
    print(f"Frequency of 'Python': {file_text.word_frequency('Python')}")  # 3
    print(f"Most common word: {file_text.most_common_word()}")  # Python
    print(f"Unique words: {file_text.unique_words()}")

    """ Bonus: Clean text using the inherited class """
    modified_text = TextModification("Hello, world! This is a Python test with 123 numbers & symbols_@#.")
    print("\nBonus: Text Modification")
    print(f"Original text: {modified_text.text}")
    print(f"Without punctuation: {modified_text.remove_punctuation()}")
    print(f"Without stop words: {modified_text.remove_stop_words()}")
    print(f"Without special characters: {modified_text.remove_special_characters()}")

    """ Create a TextModification instance directly from a file """
    modified_file = TextModification.from_file(file_path)
    print(f"File without stop words: {modified_file.remove_stop_words()}")

    """ Display the results for empty text """
    empty_text = Text("")
    print("\nEmpty Text")
    print(empty_text.word_frequency("word"))  # None
    print(empty_text.most_common_word())      # None
    print(empty_text.unique_words())          # []
