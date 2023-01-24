import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice == 0:
    print(rock)
    print("Player chose rock!")
elif player_choice == 1:
    print(paper)
    print("Player chose paper!")
elif player_choice == 2:
    print(scissors)
    print("Player chose scissors!")

print("")
print("Computer chose:\n")

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(rock)
    print("Computer chose rock!")
elif computer_choice == 1:
    print(paper)
    print("Computer chose paper!")
else:
    print(scissors)
    print("Computer chose scissors!")

lose = "You Lose."
win = "You Win."
draw = "It's a draw."

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You Lose!")

elif player_choice == 0 and computer_choice == 0:
    print(draw)
elif player_choice == 0 and computer_choice == 1:
    print(lose)
elif player_choice == 0 and computer_choice == 2:
    print(win)

elif player_choice == 1 and computer_choice == 0:
    print(win)
elif player_choice == 1 and computer_choice == 1:
    print(draw)
elif player_choice == 1 and computer_choice == 2:
    print(lose)

elif player_choice == 2 and computer_choice == 0:
    print(lose)
elif player_choice == 2 and computer_choice == 1:
    print(win)
elif player_choice == 2 and computer_choice == 2:
    print(draw)

