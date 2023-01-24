# Modifying Global Scope

enemies = 1     #global

# def increase_enemies():
#     global enemies      # get global variable
#     enemies += 1     # modify global variable
#     print(f"enemies inside function: {enemies}")

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

# Don't call the local and global variable the same name

