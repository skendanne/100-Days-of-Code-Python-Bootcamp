import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# To do 1 - Create a variable called 'lives' to keep track of the number
# of lives left. Set 'lives' to equal 6

# To do 2 - If guess is not a letter in the chosen_word, then reduce 
# 'lives' by 1. If lives goes down to 0 then the game should stop it
# and should print "You lose."

# To do 3 - Print the ASCII art from 'stages' that corresponds to the
# current number of 'lives' the user has remaining.

end_of_game = False
lives = 6
word_list = ["ardvark", "baboon", "camel", "apple"]

chosen_word = random.choice(word_list)
print(chosen_word)
print(stages[lives])

display_list = []
display = ""
world_length = len(chosen_word)

for n in range(world_length):
    display_list.append('_')

def clean_display():
    global display_list
    global display
    display = ""

    for n in display_list:
        display += n

clean_display()
print(display)

def guess():
    global display_list
    global display
    global end_of_game
    global lives

    guess = input("Guess a letter: ").lower()

    for n in range(world_length):
        letter = chosen_word[n]
        if letter == guess:
            display_list[n] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    clean_display()
    print(display)
    print(stages[lives])

    if "_" not in display_list:
        end_of_game = True
        print("You've Won!")


while not end_of_game:
    guess()