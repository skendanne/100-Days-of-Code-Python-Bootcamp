import random

# To do 1 - Create an empty list called display. For each letter in the 
# chosen_word, add a "_" to "display". So if the chosen_word was "apple",
# display should be ["_", "_", "_", "_", "_"] with 5 "_" representing
# each letter to guess

# To do 2 - Loop through each position in the chosen_word; if the letter
# at that position matches 'guess' then reveal that letter in the display
# at that position.

# To do 3 - Print 'display' and you should see the guessed letter in the
# correct position and every other letter replace with "_".

word_list = ["ardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

print(chosen_word)

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

guess = input("Guess a letter: ").lower()

for n in range(world_length):
    letter = chosen_word[n]
    if letter == guess:
        display_list[n] = letter

clean_display()
print(display)

