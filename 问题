import random

# 1. Print a welcome message
print("🎉 Welcome to the Guess the Number Game!")

# 2. Ask for the player's name
name = input("What is your name? ")
print("Hello, " + name + "! Let's start the game.")

# 3. Define a function to check if a number is even
def is_even(number):
    return number % 2 == 0

# 4. Create a list to store all the guesses
guesses = []

# 5. Generate a random number
secret = random.randint(1, 10)

# 6. Use a while loop to keep asking until correct
guess = 0
while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses.append(guess)  # 7. Save the guess to a list

    # 8. Use if to give hints
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("🎉 Correct! Well done, " + name + "!")

# 9. After game ends, show summary
print("You made", len(guesses), "guesses.")
print("Here are your guesses:", guesses)

# 10. Bonus: Check if secret number was even or odd
if is_even(secret):
    print("The secret number was even.")
else:
    print("The secret number was odd.")
