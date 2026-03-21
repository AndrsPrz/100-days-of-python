import art

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

def show_operations():
    for operation in operations:
        print(operation)

def calculate(n1, operation, n2):
    return operations[operation](n1, n2)

print(art.logo)

while True:  
    first_number = float(input("What's the first number?: "))
    show_operations()
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    result = calculate(first_number, operation, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")

    restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    while restart == 'y':  
        first_number = result
        show_operations()
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        result = calculate(first_number, operation, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
