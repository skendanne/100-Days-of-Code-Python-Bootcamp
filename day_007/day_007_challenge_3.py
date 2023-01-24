import random

# To do 1 - Use a while loop to let the user guess again. The loop should
# only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user
# they've won.

word_list = ["ardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

print(chosen_word)

end_of_game = False
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

    guess = input("Guess a letter: ").lower()

    for n in range(world_length):
        letter = chosen_word[n]
        if letter == guess:
            display_list[n] = letter

    clean_display()
    print(display)

    if "_" not in display_list:
        end_of_game = True
        print("You've Won!")

while not end_of_game:
    guess()