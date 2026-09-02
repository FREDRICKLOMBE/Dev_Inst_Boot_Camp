## MINI - PROJECT: HANGMAN ##
import random

# List of possible words
words = ["python", "computer", "programming", "developer", "analytics"]

# Computer chooses a random word
word = random.choice(words)

# Create stars for each letter
hidden_word = ["*"] * len(word)

# Keep track of letters the player has already guessed
guessed_letters = []

# Body parts added after incorrect guesses
body_parts = [
    "head",
    "body",
    "left arm",
    "right arm",
    "left leg",
    "right leg"
]

wrong_guesses = 0

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(" ".join(hidden_word))

# Continue until the player wins or loses
while wrong_guesses < 6 and "*" in hidden_word:

    guess = input("Guess a letter: ").lower()

    # Check that the player entered one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct!")

        # Reveal the letter in all correct positions
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        print("Wrong!")
        print("Adding:", body_parts[wrong_guesses])

        wrong_guesses += 1

    # Display the current state
    print("Word:", " ".join(hidden_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/ 6")
    print()

# Game result
if "*" not in hidden_word:
    print("Congratulations! You solved the word:", word)
else:
    print("Game over!")
    print("The word was:", word)