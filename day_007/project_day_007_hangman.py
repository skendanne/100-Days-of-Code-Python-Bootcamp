import random
import hangman_art as ha
import hangman_words as hw
import os

print(ha.logo)

end_of_game = False
lives = 6

chosen_word = random.choice(hw.word_list)
print(ha.stages[lives])

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

    os.system('cls')

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
    print(ha.stages[lives])

    if "_" not in display_list:
        end_of_game = True
        print("You've Won!")


while not end_of_game:
    guess()