# Does python have block scope?

# There is no Block Scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

# If you create a variable whitin a function
# it will only be avaible inside the function

# But if you create a variable whitin a if, while, for
# It will be avaible everywhere

