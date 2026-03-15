import random

# List of predefined words
words = ["python", "apple", "chair", "vikash", "plant"]

# Randomly select a word
word = random.choice(words)

# Create blank display
guessed_word = ["_"] * len(word)

# Track guesses
wrong_guesses = 0
max_wrong = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)