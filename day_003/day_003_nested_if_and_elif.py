# Nested if / else

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do this

def rollercoaster():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm?\n"))

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age?\n"))

        if age < 12:
            print("Please pay $5.")        
        elif age <= 18:
            print("Please pay $7.")
        else:
            print("Please pay $12.")
    else:
        print("Sorry, you have to grow taller before you can ride.")

# Exercise

# Write a program that interprets the Body Mass Index (BMI)
# based on a user's weight and height.
# It should tell them the interpretation of thei BMI based on the BMI value.

# Under 18.5 they are underweight;
# Over 18.5 but below 25 they have a normal weight;
# Over 25 but below 30 they are overweight;
# over 30 but below 35 they are obese;
# above 35 they are clinically obese.

def bmi():
    height = float(input("Enter your height in m:\n"))
    weight = float(input("Enter your weight in kg:\n"))

    bmi = round(weight / height ** 2, 2)
    print(f"Your BMI equals to {bmi}.")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    elif bmi < 35:
        print("You are Obese.")
    else:
        print("You are clinically obese.")

# Exercise

# Write a program that works out wheter if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in
# February. This is how you work out wheter if a particular year is a leap year:

# On every year that is evenly divisible by 4
#     except every year that is evenly divisible by 100
#         unless the year is also evenly divisible by 400

def leap_year():
    year = int(input("Which year do you want to check?\n"))

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    if leap == True:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} isn't a leap year")

rollercoaster()
bmi()
leap_year()