import random
"""
🌟 Number Guessing Game
A program that lets the user guess a randomly generated number between 1 and 100.
"""
computer_number_guessed = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("To end the game type 'exit'")

while True:
    user_input = input("Guess a number between 1 and 100: ")

    if  user_input.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break

    try:
        user_number_guessed = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100 or type 'exit' to quit.")
        continue

    if user_number_guessed < 1 or user_number_guessed > 100:
        print("Incorrect entry. Select a number between 1 - 100")
    else:
        if user_number_guessed < computer_number_guessed:
            print("Your guess is too low! Try again")

        elif user_number_guessed > computer_number_guessed:
            print("Your guess is too high! Try again")

        elif user_number_guessed == computer_number_guessed:
            print("Congrats! You guessed right! You WIN! 🎊 🎉")
            break

