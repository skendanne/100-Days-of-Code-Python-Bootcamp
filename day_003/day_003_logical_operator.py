# if condition1 & condition2 & condition3:
#     do this
# else:
#     do that

# A and B  -  both need to be True in order to be True.
# C or  D  -  just one of them needs to be True in order to be True.
# not E    -  it reverses. True becomes False and False becomes True.

def rollercoaster():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm?\n"))
    bill = 0

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age?\n"))

        if age < 12:
            bill = 5
            print("Child tickets are $5.")     
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7.")
        elif age >= 45 and age <=55: # Middle Life Crises free ride!
            print("Everything is going to be ok. Have a free ride on us!")
        else:
            bill = 12
            print("Adult tickets are $12.")
        
        wants_photo = input("Do you want a photo taken? Y or N.\n")
        if wants_photo == "Y":
            bill += 3 # same as bill = bill + 3

        print(f"Your final bill is ${bill}.")

    else:
        print("Sorry, you have to grow taller before you can ride.")

# Exercise:

# You are going to write a program that tests the compatibility
# between two people. We're going to use the super scientific recommended
# by BuzzFeed.

# To work out the love score between two people:
#     Take both people's name and check for the number of time the letters
#     in the word TRUE occurs. Them check for the number of times the letter
#     in the word LOVE occurs. Then combine theses numbers to make a
#     2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."

# For love Scores between 40 and 50, the message should be:
# "Your score is y, you are alright together."

# Otherwise, the message will just be their score.
# "Your score is z."

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# .upper()  //  .lower()  //  .count()

name = name1 + name2
lower_name = name.lower()

true_t = lower_name.count("t")
true_r = lower_name.count("r")
true_u = lower_name.count("u")
true_e = lower_name.count("e")

love_l = lower_name.count("l")
love_o = lower_name.count("o")
love_v = lower_name.count("v")
love_e = lower_name.count("e")

true_result = true_t + true_r + true_u + true_e
love_result = love_l + love_o + love_v + love_e

result = int(f"{true_result}" + f"{love_result}")

print("\nchecking...\n")

if result < 10 or result > 90:
    print(f"Your score is {result},  you go together like coke and mentos.")
elif result > 40 and result < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")

# rollercoaster()