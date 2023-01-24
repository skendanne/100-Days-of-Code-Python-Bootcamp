# for loop

# for item in list_of_items:
#     do something to each item

# range

# for number in range(a, b):
#     print(number)

for number in range(1, 11):
    print(number)

total = 0

for number in range(1, 101):
    total += number

print(total)

# Exercise:

def even_numers_to_100():
    # You are goind to write a program that calculates the sum of all
    # the even numbers from 1 to 100, incluiding 1 and 100.

    # Important, there should only be 1 print statetment in your console output.
    # It should just print the final total and not every step of the calculation.

    total = 0

    for number in range(1, 101):
        if number % 2 == 0:
            total += number
        else:
            total = total
    print(total)

    total = 0
    for number in range(2, 101, 2):
        total += number
    print(total)

# even_numers_to_100()

print("")

# You are going to write a program that automatically prints the solution
# to the FizzBuzz game.

# You program should print each number from 1 to 100 in turn.
#     When the number is divisible by 3 then instead of printing the number
#     it should print 'Fizz'.

#     When the number is divisible by 5, then instead of printing the number
#     it should print 'Buzz'.

#     And if the number is divisible by both 3 and 5, then instead of the 
#     number it should print 'FizzBuzz'.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)