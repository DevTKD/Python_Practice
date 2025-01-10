import random
"""
🪨, 📄, ✂️Rock-Paper-Scissors Game
- Play a game of rock-paper-scissors against the computer.
"""
player_choices = ["Rock 🪨", "Paper 📄", "Scissors ✂️" ]

player_1 = input("Select Rock, Paper or Scissors: ").capitalize()
computer_player = random.choice(player_choices).capitalize()

# need to add while loop for contentious game play
# add if/else logic for game rules
"""
Game Rules:
* Rock beats scissors:Rock blunts scissors
* Scissors beats paper:Scissors cuts paper
* Paper beats rock: Paper covers rock
* Draw: If both players choose the same shape, the turn is a draw and repeated
"""

if player_1 == "Rock" and computer_player == "Scissors":
    print("Rock 🪨 beats scissors ✂️:Rock blunts scissors")

