import random
"""
🌟 Number Guessing Game
A program that lets the user guess a randomly generated number between 1 and 100.
"""

user_number = int(input("Guess a number between 1 and 100: "))
computer_number = random.randint(1,100)

if user_number < 1 or   user_number > 100:
    print ("Incorrect entry. Select a number between 1 - 100")
else:
    if user_number == computer_number:
        print(f"The computer guessed {computer_number}")
        print ("Congrats! You guessed right!")

    elif user_number != computer_number:
        print(f"The computer guessed {computer_number}")
        print("You guessed wrong! Sorry!")



