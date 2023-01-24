name = "Matheus"
print(name)
print('')

# you can change the value of the variable
print("changing value of variable...")
print('')

name = "Dingoberto"
print(name)
print('')

name = input("What is your name? ")
length = len(name)
print("Your name has " + str(length) + " letters.")

# exercise
print("exercise")
print('')

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c
print("a = " + str(a))
print("b = " + str(b))