import random   # random module use kar rahe hain taaki har baar different word aaye

# List of predefined words (game inhi words me se choose karega)
words = ["python", "apple", "chair", "vikash", "plant"]

# Randomly ek word select karna list me se
word = random.choice(words)

# Blank display create karna (jitne letters utne "_")
# Example: "apple" → ["_", "_", "_", "_", "_"]
guessed_word = ["_"] * len(word)

# Game tracking variables
wrong_guesses = 0        # kitni galat guesses hui
max_wrong = 6            # maximum allowed wrong attempts
guessed_letters = []     # user ke guessed letters store honge

print("Welcome to Hangman Game!")

# Word ka first letter bata rahe hain as a hint
print("Hint: The word starts with:", word[0])

# Main game loop
# Loop tab tak chalega jab tak:
# 1. wrong guesses limit se kam hai
# 2. word complete nahi hua ( "_" present hai )
while wrong_guesses < max_wrong and "_" in guessed_word:

    # Current guessed word display (list ko string me convert karke)
    print("\nWord:", " ".join(guessed_word))

    # User se input lena aur lowercase me convert karna
    guess = input("Enter a letter: ").lower()

    # Check: kya user ne pehle se ye letter guess kiya hai?
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue   # next iteration (same input repeat na ho)

    # New guess ko list me store karna
    guessed_letters.append(guess)

    # Check: guess word ke andar hai ya nahi
    if guess in word:
        print("Correct guess!")

        # Har position check karenge
        # Jaha letter match karega waha "_" replace kar denge
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        # Agar guess galat hai
        wrong_guesses += 1   # wrong counter increase
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# Game result check
# Agar "_" nahi bacha → user ne pura word guess kar liya
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    # Agar chances khatam ho gaye
    print("\nGame Over! The word was:", word)
