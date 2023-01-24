import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.00000000 - 0.999999...
random_float = random.random()
print(random_float)

# 0.00000000 - 4.9999...
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"You love score is {love_score}")

# Exercise:

# You are going to write a virtual coin toss program.
# It will randomly toll the user "Heads" or "Tails".

# Important, the first letter should be capitalised
# and spelt exaclty like in the example: Heads not heads.

# There are many ways of doing this. But to practice what we
# learnt in the last lesson, you should generate a random number,
# either 0 or 1. Then use that number to print out Heads or Tails.

def coin_toss():
    random_number = random.randint(0,1)

    if random_number == 1:
        print("Heads")
    else:
        print("Tails")

coin_toss()