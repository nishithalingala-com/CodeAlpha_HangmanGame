import random

words = ["python", "laptop", "science", "keyboard", "project"]
word = random.choice(words)

guessed = []
display = ["_"] * len(word)
attempts = 6

print("\n🎮 HANGMAN GAME 🎮")

while attempts > 0:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed)
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Enter only ONE letter")
        continue

    if guess in guessed:
        print("⚠ Already guessed")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong!")
        attempts -= 1

    if "_" not in display:
        print("\n🎉 You WON! Word:", word)
        break

if "_" in display:
    print("\n😢 You LOST! Word was:", word)
