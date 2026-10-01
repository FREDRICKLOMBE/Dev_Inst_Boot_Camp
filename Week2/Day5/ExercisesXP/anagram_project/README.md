# Anagram Checker

A Python mini-project with separate dictionary logic and command-line UI.
No third-party packages are required. Use Python 3.8 or newer.

## Files

- `anagram_checker.py`: the `AnagramChecker` class; never prints or asks for input.
- `anagrams.py`: input validation, formatted results, and the repeating menu.
- `sowpods.txt`: the dictionary supplied by the course, included unchanged.

## Run

Open a terminal in this folder and run:

```sh
python anagrams.py
```

On Windows, you can also use `py anagrams.py`. If your computer has an
incorrect `PYTHONHOME` environment variable and reports an `encodings` startup
error, use `py -E anagrams.py` to ignore Python environment variables.

Choose `1`, enter a word, and read the results. Choose `2` to exit.
The default dictionary path is relative to the Python file, so launching
the script from another directory also works.

## Design notes

- Section headers group imports, validation, presentation, and application flow.
- Module, class, and function docstrings explain responsibilities and behavior.
- Comments explain decisions such as preserving repeated letters and loading once.
- A set removes duplicate dictionary entries and supports fast membership checks.
- Sorting letters detects anagrams while preserving letter counts.
- The original word is excluded; results are returned in alphabetical order.
- Input must be one nonempty alphabetic word; surrounding whitespace is removed.
- Dictionary membership is reported separately from input validity. Validly
  formatted input is searched even if it is absent from the dictionary.
- `is_anagram` compares letter counts, including for identical words, as specified
  in the first set of course instructions. `get_anagrams` excludes identical words.
- Results depend on the supplied dictionary; it can include uncommon words.

## Word-list source

The course links to this archive:
https://github.com/devtlv/Datasets-DA-Bootcamp-2-/raw/refs/heads/main/Week%202%20-%20OOP/W2D5%20-%20Mini-project/sowpods.zip

## Manual checks

Try `MEAT`, ` meat `, an empty input, `two words`, `abc123`, `can't`, and
an invalid menu option. Check that the menu returns after each result or error.
Try `zzzzz` to see the dictionary-miss and no-anagrams messages.

The class also accepts a custom word-list path: `AnagramChecker("my_words.txt")`.
