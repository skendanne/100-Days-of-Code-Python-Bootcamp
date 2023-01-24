# Multiple if

# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

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
        else:
            bill = 12
            print("Adult tickets are $12.")
        
        wants_photo = input("Do you want a photo taken? Y or N.\n")
        if wants_photo == "Y" or "y":
            bill += 3 # same as bill = bill + 3

        print(f"Your final bill is ${bill}.")

    else:
        print("Sorry, you have to grow taller before you can ride.")

# Exercise

# Congratulations, you've got a job at Python Pizza.
# Your first job is t o build an automatic pizza order program.

# Based on a user's order, work out their finall bill.
# small pizza = 15
# medium pizza = 20
# large pizza = 25
# pepperoni for small pizza = +2
# pepperoni for medium and large pizza = +3
# Extra cheese for any size pizza = +1

def pizza():
    print("Welcome to Python Pizza Deliveries!")
    bill = 0

    size = input("What size pizza do you want? S, M or L\n").upper()
    add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()

    if size == "S":
        bill += 15
        if add_pepperoni == "Y":
            bill += 2
    elif size == "M":
        bill += 20
        if add_pepperoni == "Y":
            bill += 3
    else:
        bill += 25
        if add_pepperoni == "Y":
            bill += 3

    extra_cheese = input("Do you want extra cheese? Y or N\n").upper()
    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is ${bill}.")

# rollercoaster()
pizza()