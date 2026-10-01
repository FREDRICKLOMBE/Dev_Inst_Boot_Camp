Daily Challenge: Text Analysis

Run:
py -E DailyChallenge_TextAnalysis.py

Keep sample_text.txt beside the Python file. No external packages or downloads
are needed. The -E option avoids the conflicting PYTHONHOME setting detected
on this computer. A normally configured installation can also use:
python DailyChallenge_TextAnalysis.py

The solution covers all nine steps, including every bonus method. It follows
DailyChallenge_Circle.py's star headings, short docstrings, explanatory comments,
triple-quoted section labels and examples under a main guard.

Part I
Text stores a string. word_frequency() counts exact whitespace-separated words
and returns None for an absent word. most_common_word() builds a frequency
dictionary and returns the first encountered word if counts are tied. Empty
text returns None. unique_words() uses a set and returns a sorted list of all
distinct words, not just words that occur once.

Analysis is case-sensitive and punctuation-sensitive, as in the assignment's
split() instructions. For example, Python, python and Python! are different
words. The original text is not automatically cleaned.

Part II
from_file() reads a UTF-8 file and returns cls(text). Using cls also lets the
subclass inherit this constructor correctly. sample_text.txt is an original
example supplied with this solution; the assignment specifies no required book.
A missing or unreadable file raises the normal Python file exception.

Bonus
TextModification inherits from Text. Each cleaning method returns a new string;
it does not change self.text, so the examples can run independently.
remove_punctuation() deletes ASCII punctuation using string.punctuation.
remove_stop_words() filters a selected set of common English stop words. Checks
ignore case and surrounding ASCII punctuation; retained words keep their case
and punctuation. Whitespace is normalized by joining the remaining words.
remove_special_characters() uses a regex to delete symbols, punctuation and
underscores while preserving Unicode letters, digits and whitespace.
Deleting punctuation or symbols may join adjacent pieces, e.g. red-blue becomes
redblue. This is literal character removal as requested by the assignment.

The selected stop words are a compact subset, not an exhaustive English list.
Online source consulted for Step 8:
https://github.com/stopwords-iso/stopwords-en
https://raw.githubusercontent.com/stopwords-iso/stopwords-en/master/stopwords-en.txt

Sample_Output.txt contains the actual output from running the script.
