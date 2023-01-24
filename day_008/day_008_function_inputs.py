# Functions

# def my_function():
#     do this
#     then do this
#     finally do this

# my_function()

def greet():
    print("Hello")
    print("How do you do?")
    print("Do you do")
    print("The things that you do")
    print("")

greet()

# Functinos with Inputs

# def my_function(something):       something = parameter
#     do this with something
#     then do this
#     finally do this

# my_function(123)                  123 = argument

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")
    print("")

greet_with_name("Dimas, o Primeiro")

# Function with more that 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    print("")

greet_with("Dimas, o Primeiro", "Capão")

# def my_function(a, b, c):
#     do this with a
#     then do this with b
#     finally do this with c

# # my_function(3, 1, 2)            Postion argument
# my_function(a=1, b=2, c=3)        Key word argument

# Exercise:

# Area Calculation

# You are painting a wall. The instructions on the paint can says that 1
# can of paint can cover 5 square meters of wall. Given a random height
# abd width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height * wall width) / coverage per can

# the result should be rounded up.

import math

def paint_calc(height, width, cover):
    total = (height * width) / cover
    math.ceil(total)
    total = int(total)
    if total < 2:
        print(f"You'll need {total} can of paint")
    else:
        print(f"You'll need {total} cans of paint")

height = float(input("Height of the wall: "))
width = float(input("Width of the wall: "))
coverage = 5

paint_calc(height, width, coverage)



# Prime Number Checker

# Prime number are numbers that can only be clearly divided by itself
# and 1.

# You need to write a function that checks wheter if the number passed
# into it's a prime number or note]

def prime_checker(n):
    checker = True

    for i in range(2, n):
        if n % i == 0:
            checker = False

    if checker == True:
        print(f"{n} it's a prime number")
    else:
        print(f"{n} it's not a prime number")

n = int(input("Check this number: "))
prime_checker(n)