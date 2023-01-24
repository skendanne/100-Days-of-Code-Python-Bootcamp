import calculator_art as ca
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(ca.logo)

    n1 = float(input("What's the first number? "))
    for i in operations:
        print(i)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        x = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation or 'exit' to exit: ")
        
        if x == "y":
            n1 = answer
        elif x == "n":
            os.system('cls')
            calculator()
        else:
            should_continue = False

calculator()