import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choose_difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

number = random.randint(1,100)

def play(attempts, number):
    playing = True

    while playing:
        if attempts == 0:
            playing = False
            print(f"You run out of attempts. The awnser was {number}.")
            break
        elif attempts > 1:
            print(f"You have {attempts} remaining to guess the number.")
        elif attempts == 1:
            print(f"You have {attempts} remainig. This is your last try.")
       
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            playing = False
        elif guess > number:
            print("Too high.")
            attempts -= 1
        else:
            print("Too low.")
            attempts -= 1

play(attempts, number)        