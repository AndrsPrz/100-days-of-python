"""
Calculator
----------
A command-line calculator that supports chained operations.
Built as part of the #100DaysOfCode - Python journey (Day 10 Capstone).
"""

import art


# --- Arithmetic Operations ---

def add(n1, n2):
    """Return the sum of n1 and n2."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference of n1 minus n2."""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of n1 and n2."""
    return n1 * n2

def divide(n1, n2):
    """
    Return the result of n1 divided by n2.

    Note: Does not handle division by zero. Input validation
    can be added as a future improvement.
    """
    return n1 / n2


# --- Operations Map ---
# Maps operator symbols to their corresponding functions.
# Easily extensible — add a new symbol and function to support more operations.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# --- Helper Functions ---

def show_operations():
    """Print all available operator symbols to the console."""
    for operation in operations:
        print(operation)

def calculate(n1, operation, n2):
    """
    Apply the selected operation to two numbers.

    Args:
        n1 (float): The first operand.
        operation (str): The operator symbol (e.g. '+', '-', '*', '/').
        n2 (float): The second operand.

    Returns:
        float: The result of the operation.
    """
    return operations[operation](n1, n2)


# --- Main Program ---

print(art.logo)

while True:
    # Start a fresh calculation
    first_number = float(input("What's the first number?: "))
    show_operations()
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

    result = calculate(first_number, operation, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")

    restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    # Chain operations: carry the current result forward as the next first number
    while restart == "y":
        first_number = result
        show_operations()
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))

        result = calculate(first_number, operation, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")

        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")