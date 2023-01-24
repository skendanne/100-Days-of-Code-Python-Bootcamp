# list
# square brackets [ ]

# list = [0, 1, 2, 3, 4]
# fruits = ["item1", item2]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print list
print(states_of_america)

# print first item of the list
print(states_of_america[0])

# print second item of the list
print(states_of_america[1])

# print last item of the list
print(states_of_america[-1])

# change itens of the list
states_of_america[1] = "Pencilvania"
print(states_of_america)

states_of_america[1] = "Pennsylvania"

# add single item to the list
states_of_america.append("Angelaland")
print(states_of_america)

# add multiple itens to the list
states_of_america.extend(["Stalinland", "Pagoland"])
print(states_of_america)

# EXERCISE:

# You are going to write a program which will select a random name
# from a list of names. The person sleected will have to pay for everybody's
# food bill.

# Important: You are not allowed to use the choiche() function.

def banker_roulette():
    names_string = input("Giver me everybody's names, seperated by a comma \",\".\n")
    names = names_string.split(", ")

    import random

    num_items = len(names)
    random_number = random.randint(0, num_items - 1)
    name = names[random_number]
    print(f"{name} is going to buy the meal today:")

# banker_roulette()

def banker_roulette_improved():
    names_string = input("Giver me everybody's names, seperated by a comma \",\".\n")
    names = names_string.split(", ")

    import random

    person_who_will_pay = random.choice(names)
    print(f"{person_who_will_pay} is going to buy the meal today:")

banker_roulette_improved()