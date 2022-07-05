import random

number = random.randrange(1,9)
guess = int(input("Guess a number between 1 and 9: "))

while guess != number:
    if guess<number:
        print("WRONG! Guess higher.")
        guess = int(input("\nGuess a number between 1 and 9: "))
    else:
        print("WRONG! Guess lower.")
        guess = int(input("\nGuess a number between 1 and 9: "))

print("CORRECT!")