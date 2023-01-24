# round numbers = round()
# round(number, number of decimal places)
print(round(8 / 3, 2))
print("")
print(round(8 / 3))
print("")

# // - floor division
print(8 // 3)
print('')

# shortcuts
# take the last value and does the operation
# variable += 1 - add 1 to variable
# variable -= 1 - sub 1 to variable
# variable /= 1 - divide 1
# variable *= 1 

score = 0
print("Your score is " + str(score))

score += 1
print("Your score is " + str(score))

# f-String
# syntax - f"string"
print(f"Your score is {score}")

# exercise
# Create a program using maths and f-Strings that tells us
# how many days, weeks, months we heave left if we live until
# 90 years old
# It will take your current age as the input and output a message with
# our time left in this formaat:
# You have x days, y weeks and z months left.
# where x,y and z area replaced with the actual calculated numbers

age = input("what is your current age?\n")
year_day = 365
year_week = 52
year_month = 12

time_left = 90 - int(age)
x = year_day * time_left
y = year_week * time_left
z = year_month * time_left

print(f"You have {x} days, {y} weeks and {z} months left.")