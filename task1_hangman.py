import random

# Predefined words
words = ["python", "apple", "flower", "laptop", "school"]

# Select a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts Left:", attempts)

    if "_" not in display:
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess")
    else:
        attempts -= 1
        print("Wrong Guess")

if attempts == 0:
    print("\nGame Over")
    print("The correct word was:", word)
