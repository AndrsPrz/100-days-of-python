import art

def add(n1, n2):
    return n1 + n2
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(operation):
    operation = operations[operation]
    return operation(first_number, next_number)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)

first_number = float(input("What's the first number?: "))
for operation in operations:
    print(operation)

def choose_operation():
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

choose_operation()

result = print(f"{first_number} {operation} {next_number} = {calculate(operation)}")

restart = input(f"Type 'y' to continue calculating with {calculate(operation)}, or type 'n' to start a new calculation")
if restart == "y":
    first_number = calculate(operation)
    choose_operation()
    calculate(operation)
