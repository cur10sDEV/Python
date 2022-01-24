# The Rock Paper Scissor Game
import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors.")
hand = [rock, paper, scissor]
player1 = int(input("Enter, It's your turn\n"))
player2 = random.randint(0, 2)

if (0 <= player1 <= 2):
    print("\nYou Chose")
    print(hand[player1])
    print("\nComputer Chose")
    print(hand[player2])

    if (player1 == 0 and player2 == 2): print("\nYou Win\n")
    elif (player1 == 2 and player2 == 1): print("\nYou Win\n")
    elif (player1 == 1 and player2 == 0): print("\nYou Win\n")
    elif(player1 == player2): print("\nDraw\n")
    else: print("\nYou Lose\n")
else: print("\nGrow Up, You typed an invalid number, You lose!\n")