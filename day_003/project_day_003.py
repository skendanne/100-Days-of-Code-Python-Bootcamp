print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("The Treasure Island is well known by the brave. The island to receive your rewarding after completing your mission...")

life = 1

def action1():
    print("")
    print("As soon you arrive in the Island, you see Blue wainting you below a tree.")
    print('- "Greetings my friend"')
    print("")

    answer1 = input("Please, awnser your friend Blue.\n")

    print("")
    print('- "Good. We need to go to the otherside of the street."')
    print("")
    print("You see two diferent patterns in the street.")
    print("One alternating black and white shapes to the left.")
    print("Other with one dashed line to the right.")
    print("")

    global life
    answer2 = str(input("Wich side you are going to cross the street? Left or Right?\n").lower())

    print('')

    if answer2 == 'left' and life == 1:
        print("You cross the road.")
    elif answer2 == 'right' and life == 1:
        print("Nobody can predict when somebody will cross the road.\nPlease respect the time and location to cross it.")
        print('Game Over.')
        print('')
        life = 0
    else:
        print("Blue starts running.\nTaking you by your arm e crossing the streets away from the crosswalk.\nYou both got hit by a car.")
        print('Game Over.')
        print('')
        life = 0

action1()

def action2():
    print('')
    print('- "Wow, the cars here are so nice. They stoped as soon as I stood here."')
    print("You think as you see that Blue is crossing the road to the right when he gets hit by a car. And now he's floating into a gasoline truck.")
    print('The truck felt in the oposite side from you.')
    print('Falling into the walls of a building, crushing the truck and flooding the street with gasoline.')
    print('')

    print('.')
    print('..')
    print('...')

    print('')
    print("You are a lucking one. After all that you're still alive.")
    print('You look up and see that the crashing made something inside the house blow.')
    print('Little flashed are coming from the inside.')
    print('')
    
    global life
    answer3 = str(input("You have to decide. You are going to SWIN out of the gasoline or you are going to SEE what happens?\n").lower())

    print('')

    if answer3 == 'swin' and life == 1:
        print('You got out of the gasoline.')
    else:
        print("You see a big white light.")
        print('Game Over.')
        print('')
        life = 0

if life == 1:
    action2()

def action3():
    print('')
    print('What is left of the street is now on fire. You start running away from it to the same direction of everyone alive.')
    print("After a brief momento, you think that you dind't got the treasure yet.")
    print('It was so simple, you just had to cross the street and go to the red apartment to get the it.')
    print('Simple.')
    print('')

    print('.')
    print('..')
    print('...')

    print('')
    print('You start running back to the apartment. You had to accomplish your mission.')
    print('You enter.')
    print('Go up by stairs.')
    print('You reach the level.')
    print('The apartment is infact three apartments. Blue had told you that in the last transmission. Now you have three doors.')
    print('One blue door, one red door and one yellow door.')
    print('')

    global life
    answer4 = str(input("Which door you are going open?\n").lower())

    print('')

    if answer4 == 'blue' and life == 1:
        print("This side of this building had already collapsed.\nYou fell on what is left from the structure.")
        print('Game Over.')
        print('')
        life = 0
    elif answer4 == 'red' and life == 1:
        print("This side of this building starts collapsing when you opens the door.\nYou fell with everything.")
        print('Game Over.')
        print('')
        life = 0
    elif answer4 == 'yellow' and life == 1:
        print("You open the door and hear a big noise making you jump into the yellow apartment.")
    else:
        print("You did nothig.\nThe building collapsed and you fell down with everything.")
        print('Game Over.')
        print('')
        life = 0

if life == 1:
    action3()

def action4():
    print('You hit the treasure and pass away.')
    print('')

    print('.')
    print('..')
    print('...')

    print('')
    print('You wake up!')
    print('And now the treasure its yours.')
    print('You decide to go back the ship and get out of the island with your treasure.')
    print('But as soon as you opens the door of the apartment.')
    print('You realize that the building collapsed leaving only the section containing the apartment you were in.')
    print('Now you are stucked with waiting for some help.')
    print('')

if life == 1:
    action4()