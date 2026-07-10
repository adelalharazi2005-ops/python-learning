import random

secret = random.randint(1, 10)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

guess = int(input("Your guess: "))

if guess == secret:
    print("🎉 Congratulations! You guessed correctly.")
else:
    print("❌ Wrong guess.")
    print("The correct number was:", secret)