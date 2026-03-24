import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = []
# for nr_letter in range(nr_letters): #for 2 in 2
#     random_letter = random.choice(letters) #choice 1 and store it in a var
#     password.append(random_letter) #add var into list password
# for nr_symbols in range(nr_symbols):
#     random_symbols = random.choice(symbols)
#     password.append(random_symbols)
# for nr_numbers in range(nr_numbers):
#         random_numbers = random.choice(numbers)
#         password.append(random_numbers)
#
#
# print("".join(password))
#
# random_password = []
#
# for i in range(len(password)):
#     new_character = random.choice(password)
#     random_password.append(new_character)
#     password.remove(new_character)
# print("Your password is: " + "".join(random_password))

password = []
for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
for i in range(nr_numbers):
    password.append(random.choice(numbers))

ordered_password = ""
for char in password:
    ordered_password += char
print(f"Your ordered password is: {ordered_password}")
random.shuffle(password)
print("Your random password is: " + "".join(password))



