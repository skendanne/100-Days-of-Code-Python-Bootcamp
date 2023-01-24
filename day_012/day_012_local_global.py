# Namespace

enemies = 1     #global

def increase_enemies():
    enemies = 2     #local (new variable)
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global Scope

player_health = 10      #Global

def game():
    def drink_potion():
        potion_strength = 2 #Local
        print(player_health)

    drink_potion()

game()
print(player_health)

