# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3 - it always result in a float
# ** - exponetial

# Order of priority
# Left to Righe --->
# PEMDAS
# 1 - Parentheses ()
# 2 - Exponents **
# 3 - Multiplication *
# 3 - Division /
# 4 - Addition +
# 4 - Subtraction -

# exercise
# Write a program that calculates the body
# Mass Index (BMI) from a user's weight and
# height

height = float(input("Enter your height in m:\n"))
weight = float(input("Enter your weight in kg:\n"))

bmi = int(weight / height ** 2)
print("Your BMI equals " + str(bmi))