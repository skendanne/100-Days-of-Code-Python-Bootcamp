# conditional

# if condition:
#     do this
# else:
#     do this

# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
# Operator        Meaning
#     >          Greater Than
#     <          Less Than
#     >=         Greater than or equal to
#     <=         Less than or equal to
#     ==         Equal to
#     !=         Not equal to

# Exercise

# Write a program that works out wheter if
# a given number is an odd or even number.
# Even numbers can be divide by 2 with no remainder.
# The modulo is written as a percentage sign
# (%) in Python. It gives you the remainder
# after a division.

number = int(input("Which number do you want to check?\n"))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")