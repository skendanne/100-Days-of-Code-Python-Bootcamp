print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? R$"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))

result = round((bill + ((bill * tip_percentage) / 100)) / people, 2)

print(f"Each person should pay: R${result}")