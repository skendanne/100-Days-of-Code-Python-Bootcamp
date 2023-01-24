import random
import hangman_art
import hangman_words

# To do 1 - Update the word list to use the 'word_list' from hagman_words.py.
# Delete this line: word_list = ["ardvark", "baboon", "camel", "apple"]

# To do 2 - Import the logo and stages from hangman_art.py and print it at the
# start of the game.

# To do 3 - If the user has entered a letter they've already guessed, print
# the letter and let them know

# To do 4 - If the letter is not in the chosen_word, print out the letter
# and let them know it's not in the word.

print(hangman_art.logo)

end_of_game = False
lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
print(hangman_art.stages[lives])

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

    if guess in display_list:
        print(f"You've already guessed {guess}.")

    for n in range(world_length):
        letter = chosen_word[n]
        if letter == guess:
            display_list[n] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    clean_display()
    print(display)
    print(hangman_art.stages[lives])

    if "_" not in display_list:
        end_of_game = True
        print("You've Won!")


while not end_of_game:
    guess()