# Data types:

# strings - "word"
# integer - 10
# float - 13.41424
# booleans - true / false

# Subscript
# string[0] = s
# string[1] = t
# string[2] = r
# string[3] = i
# string[4] = n
# string[5] = g

# str() - convert to string
# int() - convert to integer
# float() - convert to float
# bool() - covert to boolean

# exercise
# Write a program that adds the digits
# in a 2 digit number. e.g. if the input
# was 35, then the output should be 3 + 5 = 8

number = input("Type a two digit number: ")
digit_1 = int(number[0])
digit_2 = int(number[1])
result = digit_1 + digit_2
print(str(digit_1) + " + " + str(digit_2) + " = " + str(result))
