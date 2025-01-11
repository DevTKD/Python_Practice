import random
"""
🪨, 📄, ✂️Rock-Paper-Scissors Game
- Play a game of rock-paper-scissors against the computer.
"""
print("""
Game Rules:
* Rock beats scissors:Rock blunts scissors
* Scissors beats paper:Scissors cuts paper
* Paper beats rock: Paper covers rock
* Draw: If both players choose the same shape, the turn is a draw and repeated
""")

player_choices = ["rock", "paper", "scissors"]

def determine_winner(player_1, computer_player):
    match (player_1, computer_player):
        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            return "Player 1 wins!"
        case ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper"):
            return "Computer wins!"
        case _ if player_1 == computer_player:
            return "It's a tie!"
        case _:
            return "Invalid input! Try again."
while True:
    print("Rock 🪨, Paper 📄, Scissors ✂️ says shoot!")
    player_1 = input("Select Rock, Paper or Scissors (or type 'exit' to quit): ").lower()
    if player_1 == 'exit':
        print("Thanks for playing!")
        break
    if player_1 not in player_choices:
        print("Invalid input! Try again.")
        continue
    computer_player = random.choice(player_choices).lower()
    result = determine_winner(player_1, computer_player)
    print(f"Player 1 chose {player_1}, Computer chose {computer_player}. {result}")