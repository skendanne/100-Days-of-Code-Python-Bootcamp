states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts", "Maryland", 
                     "South Carolina", "New Hampshire", "Virginia", 
                     "New York", "North Carolina", "Rhode Island", 
                     "Vermont", "Kentucky", "Tennessee", "Ohio", 
                     "Louisiana", "Indiana", "Mississippi", "Illinois", 
                     "Alabama", "Maine", "Missouri", "Arkansas", 
                     "Michigan", "Florida", "Texas", "Iowa", 
                     "Wisconsin", "California", "Minnesota", "Oregon", 
                     "Kansas", "West Virginia", "Nevada", "Nebraska", 
                     "Colorado", "North Dakota", "South Dakota", 
                     "Montana", "Washington", "Idaho", "Wyoming", 
                     "Utah", "Oklahoma", "New Mexico", "Arizona", 
                     "Alaska", "Hawaii"
                     ]

# print(states_of_america[90]) <--- Value above num of itens inside the list

num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])
print("")

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
                "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
                "Celery", "Potatoes"
                ]

fruits = ["Strawberries","Nectarines", "Apples", 
            "Grapes", "Peaches", "Cherries", "Pears" 
            ]

vegetables = ["Spinach", "Kale","Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Exercise:

# You are going to write a program which will mark a spot with an X.
# The map is made of 3 rows of blank squares.
# ⬜⬛⚫◯

def treasure_complicated():
    print("\nHide The treasure!")
    print("To know the position, think with rows and columns.\nFor Example: The middle point is row 2 and column 2; 2, 2.\n")

    row1 = ["⬜", "⬜", "⬜"]
    row2 = ["⬜", "⬜", "⬜"]
    row3 = ["⬜", "⬜", "⬜"]

    print(f"{row1}\n{row2}\n{row3}")

    def change_X():
        if position_row == 1:
            if position_column == 1:
                row1[0] = "X"
            if position_column == 2:
                row1[1] = "X"
            if position_column == 3:
                row1[2] = "X"

        elif position_row == 2:
            if position_column == 1:
                row2[0] = "X"
            if position_column == 2:
                row2[1] = "X"
            if position_column == 3:
                row2[2] = "X"

        elif position_row == 3:
            if position_column == 1:
                row3[0] = "X"
            if position_column == 2:
                row3[1] = "X"
            if position_column == 3:
                row3[2] = "X"

        else:
            return

    position = input("\nWhere do you want to put the treasure? Write \"Row, Column\" with the comma and space.\n")

    treasure = position.split(", ")

    position_row = int(treasure[0])
    position_column = int(treasure[1])

    change_X()

    print(f"{row1}\n{row2}\n{row3}")

    # map[position_row, position_column] = "x"
    # print(f"{row1}\n{row2}\n{row3}")

print("\nHide The treasure!")
print("To know the position, think with columns and rows.\nFor Example: The middle point is column 2 and row 2; 22.\n")

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("\nWhere do you want to put the treasure? Write \"ColumnRow\" without spacing.\n")

print("")

horizontal = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical - 1]      |   ONE WAY OF DOING
# selected_row[horizontal - 1] = "X"    |   ONE WAY OF DOING

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}\n")

