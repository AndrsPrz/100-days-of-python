# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}, welcome to {location}!")

greet_with("David", "Bogota")

counter_true1 = 0
def calculate_love_score(name1, name2):
    names = (name1 + name2)
    counter1 = 0
    counter2 = 0
    for i in names.lower():
         if i in "TRUE".lower():
             counter1 += 1
         if i in "LOVE".lower():
             counter2 += 1

    print(f"Love Score = {counter1}{counter2}")

calculate_love_score("Kanye West", "Kim Kardashian")