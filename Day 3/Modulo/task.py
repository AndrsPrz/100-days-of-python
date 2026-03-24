print(10 % 3)
number = int("Write a number\n")
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#
#
# # For error typing
# user_input = input("Write a whole number: ")
#
# try:
#     number = int(user_input)
#
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# except ValueError:
#     print("Error: Please enter a valid whole number (e.g., 5, 10, 24).")
#
# #for pro level
# num = int(input("Write a number: "))
# print("Even" if num % 2 == 0 else "Odd")
#
# user_input = input("Write a whole number: ")
#
# try:
#     # Convert input to integer
#     number = int(user_input)
#
#     # The "Ternary Operator" logic (Pythonic style)
#     print("Even" if number % 2 == 0 else "Odd")
#
# except ValueError:
#     # Handles text, symbols, or decimals (like 4.5) gracefully
#     print("Error: That is not a valid whole number.")