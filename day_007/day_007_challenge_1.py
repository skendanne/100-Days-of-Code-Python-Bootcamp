import random

#step 1

word_list = ["ardvark", "baboon", "camel"]

# To do 1 - Randomly choose a word from the word_list and assign it to a
# variable called chosen_word.

# To do 2 - Ask the user to guess a letter and assign thei answer to a
# variable called guess. Make guess lowercase.

# To do 3 - Check if the letter the user guessed (guess) is one 
# of the letter in the chosen_word

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

for n in chosen_word:
    if n == guess:
        print("Right")
    else:
        print("Wrong")