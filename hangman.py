import random


words = ["python", "hangman", "computer", "program", "coding"]


word = random.choice(words)


guessed_letters = []
attempts = 6
display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")


while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    
    if guess in word:
        print(" Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print(" Wrong guess!")
        attempts -= 1


if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\n Game Over! The word was:", word)
